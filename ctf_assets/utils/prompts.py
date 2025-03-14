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
        f"{additional_system_instructions}"
    )

    return prompt

def flag_prompt(
    theme="",
    tone = "neutral", 
    amt = 1,
    flag_format = "ctf{..}",
    response_format = "JSON",
    language = "es-PR",
    additional_instructions= "",
    additional_system_instructions="",
    ) -> str:
    """
    Generates a structured prompt with instructions for generating flags.
     
    Constructs a prompt to guide flag generation based on theme, tone,
    and additional parameters.

    Args:
        theme (str): The theme of the challenge. Defaults to "".
        tone (str): The tone of the flags. Defaults to "neutral".
        amt (int): The amount of flags to generate. Defaults to 1.
        flag_format (str): The format of the flags. Defaults to "ctf{..}".
        response_format (str): The format for the response. Defaults to "JSON".
        language (str): The language used to generate flags. Defaults to "es-PR".
        additional_instructions (str): Additional instructions for flag generation. Defaults to "".
            
    Returns:
        str: A string with all instructions to generate a flag.
    """
    # Handle the case where passes 0 or a negative number
    amt = max(1, amt)

    prompt =  (
        f"{additional_system_instructions}"
        f"Provide {amt} {tone} unique flags in {language}. "
        f"that are directly related to the theme: {theme}. "
        f"Respond in a {tone} tone and language. "
        f"Flags must have this format: {flag_format}. "
        f"Reply in valid {response_format} only with the flag. "
        f"The flags are coherent phrases or sentences or phrases."
        f"Do not include any additional information. "
        f"{additional_instructions}"
    )

    return prompt

def story_prompt(
    theme="",
    tone = "neutral", 
    amt = 1,
    language = "es-PR",
    additional_instructions= "",
    additional_system_instructions="",
    ) -> str:
    """
    Generates a structured prompt with instructions for generating stories.
     
    Constructs a prompt to guide story generation based on theme, tone,
    and additional parameters.

    Args:
        theme (str): The theme of the challenge. Defaults to "".
        tone (str): The tone of the flags. Defaults to "neutral".
        amt (int): The amount of flags to generate. Defaults to 1.
        response_format (str): The format for the response. Defaults to "JSON".
        language (str): The language used to generate flags. Defaults to "es-PR".
        additions_instructions (str): Further instructions on how to generate the flag. Defaults to "".
            
    Returns:
        str: A string with instructions to generate a flag.
    """
    amt = max(1, amt)

    prompt =  (
        f"{additional_system_instructions}"
        f"Generate {amt} {tone} stories about {theme} in {language}. "
        f"Do not mix double and single quotes. "
        f"Return them as a JSON list under the key 'stories'. "
        f"Reply only with the stories. Do not include a title or any additional information. "
        f"Do not add any extra explanations, just return the stories as a JSON list."
        f"{additional_instructions}"
        )

    return prompt

def story_prompt_with_title(
    theme="",
    tone = "neutral", 
    amt = 1,
    language = "es-PR",
    additional_instructions= "",
    additional_system_instructions="",
    ) -> str:
    """
    Generates a structured prompt with instructions for generating stories.
     
    Constructs a prompt to guide story generation based on theme, tone,
    and additional parameters.

    Args:
        theme (str): The theme of the challenge. Defaults to "".
        tone (str): The tone of the flags. Defaults to "neutral".
        amt (int): The amount of flags to generate. Defaults to 1.
        response_format (str): The format for the response. Defaults to "JSON".
        language (str): The language used to generate flags. Defaults to "es-PR".
        additions_instructions (str): Further instructions on how to generate the flag. Defaults to "".
            
    Returns:
        str: A string with instructions to generate a flag.
    """
    amt = max(1, amt)

    prompt =  (
        f"{additional_system_instructions}"
        f"Generate {amt} {tone} stories about {theme} in {language}. "        
        f"Do not mix double and single quotes. "
        f"Return them as a JSON list under the key 'stories'. "
        f"Do not add any extra explanations, just return the stories as a JSON list."
        f"{additional_instructions}"
        )

    return prompt