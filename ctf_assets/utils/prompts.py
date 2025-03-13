"""
Module for generating structured prompts for Capture the Flag (CTF) challenges.

This module provides functions to create prompts for both system and user roles. 
These prompts help generate various types of CTF challenge content, including flags 
and short stories, while ensuring adherence to security and ethical guidelines.

Functions:
----------
- system_prompt(additional_instructions: str = "") -> str
    Generates the content for the system's role, with optional additional instructions.
- system_prompt: Constructs a structured prompt for OpenAI API extra constraints at the system level.
- flag_prompt: Constructs a structured prompt for OpenAI API to generating flags.
- story_prompt: Constructs a structured prompt for OpenAI to generating stories.
Usage Example:
--------------
    from prompts import system_prompt, flag_prompt
    
    system_content = system_prompt("Ensure all content is beginner-friendly.")

    user_content = flag_prompt(theme="Space Exploration", tone="funny", amt=3, language="en")

Notes:
------
- The `system_prompt` function cannot be used in o1 or o1-mini models. In 
    these models you must include the system role in the flag_prompt.
- The `flag_prompt` function structures the request to ensure adherence 
    to theme and tone.
"""

def system_prompt(additional_system_instructions = "") -> str:
    """Generates a strig with the system's role content and allows for  
    additional instructions.

    This function creates text that guides the model.It includes 
    instructions to ensure it doesn't provide illegal content, and 
    that responses are appropriate for under-18 high school students.
    
    Args
    -----
        additional_system_instructions (str, optional): Additional constraints
        or guidelines.
        
    Returns
    -------
        str: The system's role content string with any additional instructions.
    """
    prompt = (
        f"You are an expert cybersecurity assistant. "
        f"You do not generate illegal or under-18 inappropiate content. "
        f"You help generate content for Capture the Flag (CTF) challenges. "
        f"{additional_system_instructions}"
    )

    return prompt

def flag_prompt(
    theme="",
    tone = "", 
    amt = 1,
    flag_format = "ctf{}",
    response_format = "JSON",
    language = "es-PR",
    category = "", 
    tags = "",
    additional_flag_instructions= "",
    additional_system_instructions="",
    ) -> str:
    """Generates a structured prompt for creating CTF flaggs.

    This function constructs a prompt that provides instructions for 
    generating CTF flags using a specified theme, tone, language, 
    flag_format, amount of flags, and a format for the response.
    
    Args
    ----
        theme (str, optional): The theme of the challenge. Defaults to "".
        tone (str, optional): The tone of the flags. Defaults to "".
        amt (int, optional): The amount of flags to generate. Defaults to 1.
        flag_format (str, optional): The format of the flags. Defaults to "ctf{}".
        response_format (str, optional): The format for the response. Defaults to "JSON".
        language (str, optional): The language to use to generate flags. Defaults to "es-PR".
        add_instructions_flags (str, optional): Further instructions on how to generate the flag.
            
    Returns
    -------
        str: A formatted string containing the structured prompt for flag generation.
    
    Raises
    ------
        ValueError: if amt is less than 1.

    """
    if amt < 1:
        raise ValueError("The amount of flags to generate must be at least 1.")

    # prompt = (
    #     f"You are an expert cybersecurity assistant who does not generate illegal or under-18 inappropriate content. "
    #     f"You are tasked with creating flags for a cybersecurity Capture the Flag (CTF) challenge. "
    #     f"Use this language to create the flags: {language}. "
    #     f"Ensure flags have this tone: {tone}. "
    #     #f"Do not make things up. "
    #     f"Use information on the theme '{theme}' to create the flag. "
    #     f"Provide exactly {amt} {tone} flags. "
    #     f"Do not repeat flags. "
    #     f"Ensure flags are coherent sentences or phrases. "
    #     f"Ensure flags have this format: {flag_format}. "
    #     f"Reply in valid {response_format} format with only the flags. "
    #     f"Do not include any additional information in the response. "
    #     f"{additional_flag_instructions}"
    # )
    prompt =  (
        f"Provide {amt} {tone} unique flags in spanish for a Capture the Flag (CTF) cybersecurity competition "
        f"that are directly related to the theme: {theme}. "
        f"Respond in a {tone} tone and language. "
        f"Flags must have this format: {flag_format}. "
        f"The flags are coherent phrases or sentences or phrases."
        f"Reply in valid {response_format} only with the flag. "
        f"Do not include any additional information. "
        f"{additional_flag_instructions}"
    )

    return prompt

def story_prompt(
    theme="",
    tone = "", 
    amt = 1,
    response_format = "JSON",
    language = "es-PR",
    category = "", 
    tags = "",
    additional_story_instructions= "",
    additional_system_instructions="",
    ) -> str:
    """Generates a structured prompt for creating CTF flaggs.

    This function constructs a prompt that provides instructions for 
    generating CTF stories using a specified theme, tone, language, 
    flag_format, amount of stories, and a format for the response.
    
    Args
    ----
        theme (str, optional): The theme of the challenge. Defaults to "".
        tone (str, optional): The tone of the stories. Defaults to "".
        amt (int, optional): The amount of stories to generate. Defaults to 1.
        response_format (str, optional): The format for the response. Defaults to "JSON".
        language (str, optional): The language to use to generate stories. Defaults to "es-PR".
        additional_story_instructions (str, optional): Extra constraint for story generation.
            
    Returns
    -------
        str: A formatted string containing the structured prompt for flag generation.
    
    Raises
    ------
        ValueError: if amt is less than 1.

    """
    if amt < 1:
        raise ValueError("The amount of stories to generate must be at least 1.")

    # )
    prompt =  (
            f"{additional_system_instructions}"
            f"that are directly related to the theme: {theme}. "
            f"Respond with a story that is or sounds {tone}. "
            f"Reply in valid {response_format} ."
            f"Reply only with the story. Do not include additional information. "
            f"Example: Once upon a time.\n"
            f"In a land like no other, there was a young hacker named Alice. "
            f"She was a brilliant coder who found herself trapped in the digital world. "
            f"In order to escape, she had to solve a series of cybersecurity challenges. "
            f"Each challenge gave her hints on where to look. She did not want to be "
            f"be stuck there for one second longer so she thought to herself, "
            f"Where do users usually write down their passwords? "
            f"Then she remembered that users often write down their passwords under their keyboard. "
            f"And there it was. In a power move, she shouted, FREEDOM! and was back in the real world. "
            f"{additional_story_instructions}"
        )

    return prompt