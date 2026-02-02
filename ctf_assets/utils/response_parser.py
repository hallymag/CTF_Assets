import json
from typing import Any

def _loads_if_json(s: str) -> dict[str, Any] | None:
    try:
        obj = json.loads(s)
    except json.JSONDecodeError:
        return None
    return obj if isinstance(obj, dict) else None


def parse_flags(response: str | dict) -> list[str]:
    """Parse a Responses JSON-schema output into a list of flags."""
    if isinstance(response, dict):
        flags = response.get("flags", [])
        return flags if isinstance(flags, list) else []
    if isinstance(response, str):
        obj = _loads_if_json(response)
        if obj is None:
            return []
        flags = obj.get("flags", [])
        return flags if isinstance(flags, list) else []
    return []


def parse_stories(response: str | dict) -> list[str]:
    """Parse a Responses JSON-schema output into a list of stories."""
    if isinstance(response, dict):
        stories = response.get("stories", [])
        return stories if isinstance(stories, list) else []
    if isinstance(response, str):
        obj = _loads_if_json(response)
        if obj is None:
            return []
        stories = obj.get("stories", [])
        return stories if isinstance(stories, list) else []
    return []


def parse_titled_stories(response: str | dict) -> list[dict[str, str]]:
    """Parse titled stories into a list of {'title': ..., 'story': ...}."""
    def _coerce(items: Any) -> list[dict[str, str]]:
        if not isinstance(items, list):
            return []
        out: list[dict[str, str]] = []
        for it in items:
            if isinstance(it, dict) and isinstance(it.get("title"), str) and isinstance(it.get("story"), str):
                out.append({"title": it["title"], "story": it["story"]})
        return out

    if isinstance(response, dict):
        return _coerce(response.get("stories_with_titles", []))
    if isinstance(response, str):
        obj = _loads_if_json(response)
        if obj is None:
            return []
        return _coerce(obj.get("stories_with_titles", []))
    return []
