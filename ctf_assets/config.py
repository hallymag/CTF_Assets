# config.py

import os
import warnings

# Cache for the OpenAI API key
_openai_api_key = None

# Load environment variables from .env file if it exists

def fetch_openai_key(strict: bool = True) -> str | None:
    """
    Fetch the OpenAI API key from the environment variables, cached for reuse.

    This function retrieves the API key from the environment variables or `.env` file
    if not already cached, and caches it for future use. If the key is missing, it raises
    an exception or logs a warning depending on the `strict` parameter.

    Args:
        strict (bool): Determines the behavior if the API key is missing.
            - If `strict=True`, a `RuntimeError` is raised.
            - If `strict=False`, a warning is logged, and `None` is returned.
            Defaults to `True`.

    Returns:
        str | None: The OpenAI API key if found, otherwise `None` if `strict=False`.

    Raises:
        RuntimeError: If `strict=True` and the API key is missing.

    Example:
        >>> fetch_openai_key()
        'your-openai-api-key'

        >>> fetch_openai_key(strict=False)
        None
    """
    global _openai_api_key

    if _openai_api_key is None:
        # Fetch the key from the environment variables
        key = os.getenv("OPENAI_API_KEY")

        if not key:
            message = (
                f"OPENAI_API_KEY is missing! "
                "Set it in your system environment variables or .env file."
            )
            if strict:
                raise RuntimeError(message)
            warnings.warn(f"{message} Returning None.")
            return None

        # Cache the key for future use
        _openai_api_key = key

    return _openai_api_key
