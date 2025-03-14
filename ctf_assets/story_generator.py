"""
Module for generating stories.

This module constructs prompts and interacts with LLM API to
generate stories based on a theme and tone. It replies in JSON format.

Functions:
    - generate_stories- Generates stories based on theme and tone.
    - generate_stories_with_titles- Generates stories with titles based on theme and tone.

Usage Example:
    - generate_stories(theme="Cyberattacks", tone="dramatic", amt=1, model="o1-mini", language="en")
    - generate_stories_with_titles(theme="Cybersecurity", tone="dramatic", amt=1, model="gpt-4o-mini", language="es-PR")    
"""
from ctf_assets.utils.helpers import validate_openai_model
from ctf_assets.utils.initialize_client import initialize_openai_client
from ctf_assets.utils.prompts import story_prompt, story_prompt_with_title

def generate_stories(
    theme: str="",
    tone: str = "neutral",
    amt: int = 1,
    model: str = "gpt-4o-mini",
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = "",
    temperature: float = 0.55,  # Default temperature
    ):    
    '''
    Generates stories based on the theme, tone, and additional arguments.
    
    Args:
        theme (str): The theme of the challenge.
        amt: int: The amount of stories to generate.
        model (str): The model to use. Defaults to "gpt-4o-mini". 
        response_format (str): Response format. Defaults to JSON.
        tone (str): The tone of the stories.
        language (str): The language to use to generate stories. Defaults to Spanish (Puerto Rico).
        category (str): The category of the challenge.
        tags (str, optional): The skills required to solve the challenge.
        additional_instructions (str, optional): Additional constraints or 
            guidelines for story generation.
        additional_system_instructions (str, optional): Additional constraints or 
            guidelines for the system.
        temperature (float): The temperature for the model. Defaults to 0.55.
        
    Returns:
        stories (dic): The generated stories.
    '''
    
    # Validate model. If not supported, defualt to "gtp4o-mini"
    model = validate_openai_model(model_name=model)
    
    # Initialize the OpenAI API client
    client = initialize_openai_client()
    
    if client is None:
        return "OpenAI client failed to initialized. Exiting."

    # Create the user's role content (prompt)
    prompt = story_prompt(
        theme = theme,
        tone = tone,
        amt = max(1, amt),  # Handle case 0 or less amt
        language = language,
        additional_instructions = additional_instructions,
        additional_system_instructions = additional_system_instructions,
    )
    
    # Send request to OpenAI
    response = client.chat.completions.create(
        model = model,
        temperature=temperature,
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

def generate_stories_with_titles(
    theme: str="",
    tone: str = "neutral",
    amt: int = 1,
    model: str = "gpt-4o-mini",
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = "",
    temperature: float = 0.55,  # Default temperature
    ):    
    '''
    Generates stories based on the theme, tone, and additional arguments.
    
    Args:
        theme (str): The theme of the challenge.
        amt: int: The amount of stories to generate.
        model (str): The model to use. Defaults to "gpt-4o-mini". 
        response_format (str): Response format. Defaults to JSON.
        tone (str): The tone of the stories.
        language (str): The language to use to generate stories. Defaults to Spanish (Puerto Rico).
        category (str): The category of the challenge.
        tags (str, optional): The skills required to solve the challenge.
        additional_instructions (str, optional): Additional constraints or 
            guidelines for story generation.
        additional_system_instructions (str, optional): Additional constraints or 
            guidelines for the system.
        temperature (float): The temperature for the model. Defaults to 0.55.
        
    Returns:
        stories (dic): The generated stories.
    '''
    
    # Validate model. If not supported, defualt to "gtp4o-mini"
    model = validate_openai_model(model_name=model)
    
    # Initialize the OpenAI API client
    client = initialize_openai_client()
    
    if client is None:
        return "OpenAI client failed to initialized. Exiting."

    # Create the user's role content (prompt)
    prompt = story_prompt_with_title(
        theme = theme,
        tone = tone,
        amt = max(1, amt),  # Handle case 0 or less amt
        language = language,
        additional_instructions = additional_instructions,
        additional_system_instructions = additional_system_instructions,
    )
    
    # Send request to OpenAI
    response = client.chat.completions.create(
        model = model,
        temperature=temperature,
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