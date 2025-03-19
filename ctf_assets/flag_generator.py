"""
Module for generating flags for CTF challenges.

This module constructs prompts and interacts with LLM API to
generate flags based on a theme, tone, and other arguments.

Functions:
    - generate_flags: Generates flags based on theme, tone, and additional arguments.

Example:
    - generate_flags(
        theme="Hackaton", 
        tone="neutral", 
        amt=1, 
        model="gpt-4o-mini", 
        flag_format="ctf{..}", 
        language="es-PR", 
        additional_instructions="flags must be less than 50 characters",
        additional_system_instructions="You are an assistant that does not make things up."
        )
Example using the CLI:
    ctf-assets flags generate_flags --theme "Hackaton" --tone "neutral" --amt 1 --model "gpt-4o" --flag-format "upr{..}" --language "es-PR" --additional-instructions "flags must be less than 50 characters" --additional-system-instructions "You are an assistant that does not make things up."    


"""

from ctf_assets.utils.helpers import validate_openai_model
from ctf_assets.utils.initialize_client import initialize_openai_client
from ctf_assets.utils.prompts import flag_prompt

def generate_flags(
    theme: str="",
    tone: str = "neutral",
    amt: int = 1,
    model: str = "gpt-4o-mini",
    flag_format: str = "ctf{..}",
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = "",
    temperature  = 0.55, 
    ):    
    '''
    Generates CTF flags based on a provided theme and tone.
    
    Args:
        theme (str): The theme for the challenge. Defaults to "".
        tone (str): The tone to use when generating the flags.Defaults to "neutral".
        amt: int: The amount of flags to generate. Defaults to 1.
        model (str): The model to use (e.g. "o1-mini"). Defaults to "gpt-4o-mini".
        flag_format (str): The format of the flags. Defaults to ctf{..}" 
        language (str): The language to use to generate flags. Defaults to es-PR.
        additional_instructions (str): Additional instructions for flag generation. Defaults to "".
        additional_system_instructions (str): Additional system level constaints or guidelines. Defaults to "".
        temperature (float): The temperature for the model. Defaults to 0.55.
    Returns:
        flags (dic): The generated flags. Defaults to JSON.
    '''
    
    # Validate model. If not supported, default to "gtp4o-mini"
    model = validate_openai_model(model_name=model)
    
    # Initialize the OpenAI API client
    client = initialize_openai_client()
    
    if client is None:
        return "OpenAI client failed to initialized. Exiting."

    # Create the user's role content (prompt)
    prompt = flag_prompt(
        theme = theme,
        tone = tone,
        amt = max(1, int(amt)), # Handle case 0 or less amt was entered
        flag_format = flag_format,
        language = language,
        additional_instructions = additional_instructions,
        additional_system_instructions = additional_system_instructions,
    )
    
    # Send request to OpenAI
    response = client.chat.completions.create(
        model = model,
        temperature = temperature,
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