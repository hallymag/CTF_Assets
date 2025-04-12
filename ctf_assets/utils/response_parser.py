import json

def parse_flags(response: str | dict) ->  list[str]:
    # If response is a dictionary, get the "flags" If it doesn't exist, return an empty list.
    if isinstance(response, dict):
        try:
            return response.get("flags", [])
        except KeyError:
            return []
        
    # If response is a string, try to parse it as JSON. If it is not valid JSON, return an empty list.
    try:
        parsed = json.loads(response)
        return parsed.get("flags", [])
    except json.JSONDecodeError:
        return []
    

def parse_stories(response: str | dict) -> list[str]:
    # If response is a dictionary, get the "stories" If it doesn't exist, return an empty list.
    if isinstance(response, dict):
        try:
            stories= response.get('stories', [])
            return []
        except KeyError:
            return []
        
    # If response is a string, try to parse it as JSON. If it is not valie JSON, return an empty list.
    try:
        parsed= json.loads(response)
        return parsed.get("stories", [])
    
    except json.JSONDecodeError:
        return []
    

def parse_titled_stories(response: str | dict) -> list[list[str]]:
    # If the response is already a dictionary, process it directly.
    if isinstance(response, dict):
        try:
            stories = response.get("stories_with_titles", [])
            return [[story["title"], story["story"]] for story in stories]
        except KeyError:
            return []

    # Try to parse the JSON string response.
    try:
        parsed = json.loads(response)
        stories = parsed.get("stories_with_titles", [])
        return [[story["title"], story["story"]] for story in stories]
    
    except json.JSONDecodeError:
        return []

