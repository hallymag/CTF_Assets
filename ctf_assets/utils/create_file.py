from __future__ import annotations

from pathlib import Path
import re

_INVALID_CHARS = re.compile(r"[^A-Za-z0-9._-]+")

def sanitize_filename(filename: str) -> str:
    """Return a filesystem-safe filename (keeps A-Z a-z 0-9 . _ -)."""
    filename = filename.strip().replace(" ", "_")
    filename = _INVALID_CHARS.sub("", filename)
    # avoid empty names
    return filename or "output"


def create_file(file_path: str | Path, content: str, *, encoding: str = "utf-8") -> Path:
    """Create (or overwrite) a file and write content. Returns the Path."""
    path = Path(file_path).expanduser().resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)
    return path
