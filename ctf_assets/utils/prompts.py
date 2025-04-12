"""
Module for generating structured prompts for Capture the Flag (CTF) challenges.

This module provides functions to create prompts for both system and user roles. 
These prompts help generate various types of CTF challenge content, including flags 
and short stories, while ensuring adherence to security and ethical guidelines.

Functions:
    - system_prompt: Constructs string with system level constraints which include
        making sure it does not generate illegal contetn and that it is
        appropriate for under 18, high-school students.
    - flag_prompt: Constructs a string with the user instructions to generate flags.
    - story_prompt: Constructs a string with user level instructions to generate stories.

Examples:
    from openai import openai
    from prompts import system_prompt, flag_prompt
    
    system_content = system_prompt("Ensure all content is beginner-friendly.")
    flag_content = flag_prompt(theme="Space Exploration", tone="funny", amt=3, language="en")
    story_content = story_prompt(theme="Cybersecurity Adventure", tone="dramatic", amt=1, language="en")
"""

def compose_partial_text(amt=1, asset_type="", theme="", tone="neutral", language="es-PR", title=False) -> str:
    """
    Constructs a prompt string using the provided parameters.
    
    If amt is 1, converts the provided plural noun to its singular form.
    Otherwise, uses the provided noun as is. Optionally includes a theme clause.
    
    Args:
        amt (int): The number of items to generate.
        theme (str): The theme of the challenge.
        tone (str): The tone to use.
        language (str): The language for the prompt.
        noun (str): The noun (should be passed in plural, e.g., "flags" or "stories").
        
    Returns:
        str: The constructed prompt string.
    """
    # Create a mapping for converting plural to singular
    plural_to_singular = {
        "flags": "flag",
        "stories": "story"        
    }
    
    # If amt == 1, convert the noun to singular; otherwise, use the noun as given.
    if amt == 1:
        noun_form = plural_to_singular.get(asset_type.lower(), asset_type)
    else:
        noun_form = asset_type
    
    # If theme is provided, include the related clause.
    if theme:
        related = f" related to the theme: {theme}. "
    else:
        related = "about a random subject"
    
    # If title is True, include the title clause.
    if title:
        title = "with title"
    else:
        title = ""
  
    return f"Generate exactly {amt} {tone} {noun_form} {title} {related} in {language}. "

def system_prompt(additional_system_instructions = "") -> str:
    """
    Generates system level constraints for content generation. 

    This function creates a system level prompt to guide the model so
    it doesn't generate illegal or under-18 year old high school level content.
    It also allows the user to add additional constraints or guidelines.
    
    Args:
        additional_system_instructions (str): Additional constraints or guidelines. Defaults to "".        
        
    Returns:
        str: The formatted string containing the system level constraints and guidelines.
    """
    prompt = (
        "You are an expert cybersecurity assistant. "
        "You do not generate illegal or under-18 inappropiate content. "
        "You help generate content for Capture the Flag (CTF) challenges. "
    )

    if additional_system_instructions:
        prompt += f"{additional_system_instructions} "

    return prompt

def flag_prompt(
        asset_type="flags",   
        theme="",
        tone= "neutral", 
        amt=1,
        flag_format= "ctf{..}",
        language= "es-PR",
        additional_instructions: str="",
        additional_system_instructions: str="",
        ) -> str:
    """
    Generates a structured prompt with instructions for generating flags.
    Returns the prompt string which can be used directly in the LLM API call.

    Args:
        theme (str): The theme of the challenge. Defaults to "".
        tone (str): The tone of the flags. Defaults to "neutral".
        amt (int): The amount of flags to generate. Defaults to 1.
        flag_format (str): The format of the flags. Defaults to "ctf{..}".
        language (str): The language used to generate flags. Defaults to "es-PR".
        additional_instructions (str): Additional instructions for flag generation. Defaults to "".
        additional_system_instructions (str): Additional system-level constraints or guidelines. Defaults to "".

    Returns:
        str: The structured prompt string.
    """

    # Make sure amt is a positive integer
    amt = max(1, int( amt))

    partial_prompt = compose_partial_text(asset_type=asset_type, amt=amt, theme=theme, tone=tone, language=language)

    sys_prompt = system_prompt(additional_system_instructions=additional_system_instructions)

    prompt =  (
        f"{sys_prompt} "
        "You are tasked with generating flags for a CTF challenge. "
        f"{partial_prompt} "
        f"Each flag should be in the format: {flag_format}. "
        "Do not include any other information. "
    )

    if additional_instructions:
        prompt += f" {additional_instructions}"

    return prompt

def story_prompt(
        asset_type="stories",
        theme="",
        tone = "neutral", 
        amt = 1,
        language = "es-PR",
        title = False,
        additional_instructions= "",
        additional_system_instructions=""
) -> str:
    """
    Generates a structured prompt with instructions for generating stories.
     
    Constructs a prompt to guide story generation based on theme, tone,
    and additional parameters.

    Args:
        theme (str): The theme of the challenge. Defaults to "".
        tone (str): The tone of the flags. Defaults to "neutral".
        amt (int): The amount of flags to generate. Defaults to 1.
        language (str): The language used to generate flags. Defaults to "es-PR".
        additions_instructions (str): Further instructions on how to generate the flag. Defaults to "".
            
    Returns:
        str: A string with instructions to generate a flag.
    """
    # Make sure amt is a positive integer
    amt = max(1, int( amt))

    partial_prompt = compose_partial_text(amt=amt, asset_type=asset_type, theme=theme, tone=tone, language=language, title=title)

    sys_prompt = system_prompt(additional_system_instructions=additional_system_instructions)

    if title:
        partial_prompt += "Include titles for the stories. "

    prompt = (
        f"{sys_prompt} "
        "You are tasked with generating stories for CTF challenges. "
        f"{partial_prompt} "
        "Do not mix double and single quotes. "
        "Do not add any extra explanations. "
    )
     
    if additional_instructions:
        prompt += f" {additional_instructions}"

    return prompt