"""
Module for generating Capture the Flag (CTF) challenge flags.

This module constructs flag prompts and interacts with LLM API to
generate flags based on user provided theme and tone.

Functions
---------  
`create_system_prompt(additional_instructions = "") -> str:`
    Creates system's role content, allowing users to add additional
    instructions.

`create_flag_prompt(
    theme: str,
    tone: str,
    amt: int,
    flag_format: str = "ctf{}",
    response_format: str = "JSON",
    language: str = "es-PR",
    additional_flag_instructions: str = "",
    additional_system_instructions: str = "",
) -> str:`
    Creates user's role content, allowing users to add additional 
    instructions.
"""

from ctf_assets.utils.helpers import validate_openai_model
from ctf_assets.utils.initialize_client import initialize_openai_client
from ctf_assets.utils.prompts import flag_prompt

def generate_flags(
    theme: str="",
    tone: str = "",
    amt: int = 1,
    model: str = "gpt-4o-mini",
    flag_format: str = "ctf{}",
    response_format: str = "JSON",
    language: str = "es-PR",
    category: str = "",   
    tags: str = "",
    additional_flag_instructions: str = "",
    additional_system_instructions: str = "",
    ):    
    '''Generates Capture the Flag (CTF) flags using OpenAI API.
    
    Args:
        theme (str): The theme of the challenge.
        amt: int: The amount of flags to generate.
        model (str): The OpenAI model to use.
        flag_format (str): The format of the flags. Defaults to ctf{}" 
        response_format (str): Response format. Defaults to JSON.
        tone (str): The tone of the flags.
        language (str): The language to use to generate flags. Defaults to Spanish (Puerto Rico).
        category (str): The category of the challenge.
        tags (str, optional): The skills required to solve the challenge.
        additional_flag_instructions (str, optional): Additional constraints or 
            guidelines for flag generation.
        additional_system_instructions (str, optional): Additional constraints or 
            guidelines for the system.
        
    Returns:
        flags (dic): The generated flags.
    '''
    
    # Validate model. If not supported, defualt to "gtp4o-mini"
    model = validate_openai_model(model_name=model)
    
    # Initialize the OpenAI API client
    client = initialize_openai_client()
    
    if client is None:
        return "OpenAI client failed to initialized. Exiting."

    # Create the user's role content (prompt)
    prompt = flag_prompt(
        theme = theme,
        tone = tone,
        amt = amt,
        flag_format = flag_format,
        response_format = response_format,
        language = language,
        category = category, 
        tags = tags,
        additional_flag_instructions = additional_flag_instructions,
        additional_system_instructions = additional_system_instructions,
    )
    
    # Send request to OpenAI
    response = client.chat.completions.create(
        model = model,
        temperature=0.55,
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens = 2048,
    )

    # Extract response
    return response.choices[0].message.content.strip()