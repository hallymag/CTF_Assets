"""
Module for generating structured prompts for Capture the Flag (CTF) challenges.

This module provides structured prompts to guide LLM content generation. It includes prompts for
flag generation, story creation, and image descriptions, ensuring adherence to security and ethical guidelines.

Functions:
    - system_prompt: Constructs a structured system-level prompt.
    - flag_prompt: Constructs a structured prompt for flag generation.
    - story_prompt: Constructs a structured prompt for story generation.
    - story_prompt_with_title: Constructs a structured prompt for story generation with titles.
    - image_prompt: Constructs a structured prompt for AI-generated images.

Example:
    from prompts import system_prompt, flag_prompt
    
    system_content = system_prompt("Ensure all content is beginner-friendly.")
    flag_content = flag_prompt(theme="Space Exploration", tone="funny", amt=3, language="en")

Notes:
    Some models may not require a system prompt, as they are pre-trained to avoid generating 
    inappropriate content. However, it is useful for providing additional guidelines or constraints.
"""
# TODO: Refactor the prompts to have a generic generate_prompt that handles prompts that are simim
# and also use .join() to concatenate strings to improve performance

def system_prompt(additional_system_instructions: str = "") -> str:
    """
    Generates a system-level prompt to ensure generated content is appropriate 
    for high school students and adheres to cybersecurity CTF guidelines.

    Args:
        additional_system_instructions (str, optional): Extra constraints for the system prompt. Defaults to "".

    Returns:
        str: A detailed system-level prompt.
    """
    return (
        "You are an expert cybersecurity assistant. "
        "Ensure all content is legal and suitable for high school students under 18. "
        "You generate content for Capture the Flag (CTF) challenges. "
        f"{additional_system_instructions}"
    )

def flag_prompt(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    flag_format: str = "ctf{..}",
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = ""
) -> str:
    """
    Generates a structured prompt for flag generation, ensuring adherence to the given theme, tone, and format.

    Args:
        theme (str, optional): Theme of the flags. Defaults to "".
        tone (str, optional): Tone of the flags (e.g., "serious", "playful"). Defaults to "neutral".
        amt (int, optional): Number of flags to generate (must be ≥ 1). Defaults to 1.
        flag_format (str, optional): Format of the flags (e.g., "ctf{...}"). Defaults to "ctf{..}".
        language (str, optional): Language of the flags. Defaults to "es-PR".
        additional_instructions (str, optional): Extra constraints for flag generation. Defaults to "".
        additional_system_instructions (str, optional): System-level constraints. Defaults to "".

    Returns:
        str: A structured prompt for generating flags.
    """
    amt = max(1, amt)
    sys_prompt = system_prompt(additional_system_instructions)

    return (
        f"{sys_prompt} Generate exactly {amt} unique CTF flags in {language}, based on the theme: '{theme}'. "
        f"Apply tone: '{tone}' if specified. Each flag must follow this format: '{flag_format}'. "
        f"Make sure that within the flag text, any multi-word parts are separated by spaces (e.g., 'ctf{{el hacker se ofusco}}') instead of underscores. "
        f"Output must be valid JSON with 4 spaces indents: {{\"flags\": [\"flag 1\", ..., \"flag {amt}\"]}}. "
        f"Do not include any extra text outside of JSON. {additional_instructions}"
    )

def story_prompt(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = ""
) -> str:
    """
    Generates a structured prompt for story generation, ensuring theme and tone adherence.

    Args:
        theme (str, optional): Theme of the stories. Defaults to "".
        tone (str, optional): Tone of the stories (e.g., "mysterious", "cheerful"). Defaults to "neutral".
        amt (int, optional): Number of stories to generate (must be ≥ 1). Defaults to 1.
        language (str, optional): Language of the stories. Defaults to "es-PR".
        additional_instructions (str, optional): Extra constraints for story generation. Defaults to "".
        additional_system_instructions (str, optional): System-level constraints. Defaults to "".

    Returns:
        str: A structured prompt for generating stories.
    """
    amt = max(1, amt)
    sys_prompt = system_prompt(additional_system_instructions)

    prompt = (
        f"{sys_prompt} Generate {amt} unique stories in {language} on the theme: '{theme}'. "
        f"Apply tone: '{tone}' if specified. Titles are excluded. "
        f"Output must be valid JSON 4 spaces indents: {{\"stories\": [{{\"story\": \"Story content...\"}}, ...]}}. "
        f"Do not include any extra text outside of JSON. {additional_instructions}"
    )

    return prompt

def story_prompt_with_title(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = ""
) -> str:
    """
    Generates a structured prompt for story generation with titles, ensuring adherence to theme and tone.

    Args:
        theme (str, optional): Theme of the stories. Defaults to "".
        tone (str, optional): Tone of the stories (e.g., "mysterious", "cheerful"). Defaults to "neutral".
        amt (int, optional): Number of stories to generate (must be ≥ 1). Defaults to 1.
        language (str, optional): Language of the stories. Defaults to "es-PR".
        additional_instructions (str, optional): Extra constraints for story generation. Defaults to "".
        additional_system_instructions (str, optional): System-level constraints. Defaults to "".

    Returns:
        str: A structured prompt for generating stories with titles.
    """
    amt = max(1, amt)
    sys_prompt = system_prompt(additional_system_instructions)

    return (
        f"{sys_prompt} Generate {amt} unique stories in {language} on the theme: '{theme}', including titles. "
        f"Apply tone: '{tone}' if specified. "
        f"Output must be valid JSON with 4 spaces indents: {{\"stories\": [{{\"title\": \"Story Title 1\", \"story\": \"Story content...\"}}, ...]}}. "
        f"Do not include any extra text outside of JSON. {additional_instructions}"
    )

def image_prompt(
    theme: str,
    tone: str = "neutral",
    language: str = "es-PR"
) -> str:
    """
    Generates a structured prompt for AI image generation based on a theme and tone.

    Args:
        theme (str): Theme for the image (e.g., "cybersecurity hacker", "futuristic University").
        tone (str, optional): Mood of the image (e.g., "dark and mysterious", "cheerful"). Defaults to "neutral".
        language (str, optional): Language for any text appearing in the image. Defaults to "es-PR".

    Returns:
        str: A structured prompt for AI-generated images.
    """
    return (
        f"You are an AI assistant generating detailed image prompts for AI models. "
        f"Theme: '{theme}', Tone: '{tone}'. "
        f"Ensure the prompt includes a vivid scene description, lighting, atmosphere, depth, "
        f"camera perspective, and composition style. If the image contains text, it must be in {language}."
    )