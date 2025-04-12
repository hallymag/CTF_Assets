

def get_flag_schema():
    return {
        "format": {
            "type": "json_schema",
            "name": "FlagResponse",
            "schema": {
                "type": "object",
                "properties": {
                    "flags": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of generated flags",
                    },
                }, 
                "required": ["flags"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    }

def get_story_schema():
    return {
        "format": {
            "type": "json_schema",
            "name": "StoryResponse",
            "schema": {
                "type": "object",
                "properties": {
                    "stories": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of generated stories",
                    },
                },
                "required": ["stories"],
                "additionalProperties": False,
            },
            "strict": True,
        }
    }

def get_titled_story_schema():
    return {
        "format": {
            "type": "json_schema",
            "name": "StoryResponse",
            "schema": {
                "type": "object",
                "properties": {
                    "stories_with_titles": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "The title of the story."
                                },
                                "story": {
                                    "type": "string",
                                    "description": "The content of the story."
                                }
                            },
                            "required": ["title", "story"],
                            "additionalProperties": False
                        },
                        "description": "List of stories with titles"
                    }
                },
                "required": ["stories_with_titles"],
                "additionalProperties": False
            },
            "strict": True
        }
    }


