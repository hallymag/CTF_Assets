from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from openai import OpenAI, OpenAIError

from ctf_assets.config import fetch_openai_key
from ctf_assets.utils.prompts import image_prompt


def image_directory(dir_name: str = "downloaded_images") -> Path:
    """Create (if needed) and return the directory used to store generated images."""
    outdir = (Path.cwd() / dir_name).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    return outdir


@dataclass(frozen=True)
class ImageResult:
    files: list[str]
    prompt: str


def _timestamp() -> str:
    return datetime.now().astimezone().strftime("%Y-%m-%d_%I-%M-%S_%p")


def generate_images(
    image_model: str = "dall-e-3",
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    style: str = "vivid",
    quality: str = "standard",
    size: str = "1024x1024",
    prompt_model: str = "gpt-4o-mini",
    language: str = "es-PR",
    output_dir: str | Path = "downloaded_images",
    filename_prefix: Optional[str] = None,
    prompt_override: Optional[str] = None,
    return_prompt: bool = False,
) -> list[str] | ImageResult:
    """Generate images and write them to files.

    Returns:
        - list[str]: paths of images written to disk (default)
        - ImageResult: (files, prompt) if return_prompt=True
    """
    api_key = fetch_openai_key(strict=True)
    client = OpenAI(api_key=api_key)

    # Normalize / validate
    image_model = (image_model or "dall-e-3").lower()
    if image_model not in {"dall-e-2", "dall-e-3"}:
        image_model = "dall-e-3"

    amt = int(amt) if amt and int(amt) > 0 else 1
    if image_model == "dall-e-3":
        # DALL·E 3 currently supports n=1
        amt = 1
    else:
        # DALL·E 2 supports 1..10
        amt = max(1, min(10, amt))

    outdir = Path(output_dir).expanduser().resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    # 1) Build or override the text-to-image prompt
    strip_prompt_override = (prompt_override or "").strip()
    if strip_prompt_override:
        prompt_t2i = strip_prompt_override
    else:
        prompt_for_llm = image_prompt(
            theme=theme,
            tone=tone,
            amt=amt,
            language=language,
        )
        try:
            resp = client.responses.create(
                model=prompt_model,
                input=prompt_for_llm,
            )
        except OpenAIError as e:
            raise RuntimeError(f"OpenAI API error while generating image prompt: {e}") from e

        prompt_t2i = (resp.output_text or "").strip()
        if not prompt_t2i:
            raise RuntimeError("Empty prompt generated for image creation.")

    # 2) Generate images
    try:
        img_resp = client.images.generate(
            model=image_model,
            prompt=prompt_t2i,
            n=amt,
            size=size,
            quality=quality if image_model == "dall-e-3" else None,
            style=style if image_model == "dall-e-3" else None,
            response_format="b64_json",
        )
    except TypeError:
        # Some SDK versions don't accept None for these params; retry without them.
        try:
            img_resp = client.images.generate(
                model=image_model,
                prompt=prompt_t2i,
                n=amt,
                size=size,
                response_format="b64_json",
            )
        except OpenAIError as e:
            raise RuntimeError(f"OpenAI API error while generating images: {e}") from e
    except OpenAIError as e:
        raise RuntimeError(f"OpenAI API error while generating images: {e}") from e

    # 3) Write to files
    prefix = (filename_prefix or theme or "image").strip().replace(" ", "_")
    prefix = "".join(ch for ch in prefix if ch.isalnum() or ch in "-_") or "image"
    stamp = _timestamp()

    files: list[str] = []
    for i, item in enumerate(getattr(img_resp, "data", []) or []):
        if isinstance(item, dict):
            b64 = item.get("b64_json")
        else:
            b64 = getattr(item, "b64_json", None)
        if not b64:
            # If the API returned URLs instead, we can't download without internet in this library.
            # Fail clearly so caller can switch response_format.
            raise RuntimeError("Image response did not include base64 data (b64_json).")

        data = base64.b64decode(b64)
        filename = f"{stamp}_{prefix}_{i}.png"
        path = outdir / filename
        path.write_bytes(data)
        files.append(str(path))

    return ImageResult(files=files, prompt=prompt_t2i) if return_prompt else files
