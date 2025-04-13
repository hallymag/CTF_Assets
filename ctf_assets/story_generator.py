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

from openai import OpenAI, OpenAIError
from ctf_assets.config import fetch_openai_key
from ctf_assets.utils.helpers import validate_openai_model
from ctf_assets.utils.prompts import story_prompt
from ctf_assets.utils.helpers import get_reasoning_openai_models
from ctf_assets.schema.json_schema import get_story_schema
from ctf_assets.schema.json_schema import get_titled_story_schema
from ctf_assets.utils.response_parser import parse_stories, parse_titled_stories
def generate_stories(
        amt: int = 1,
        theme: str="",
        tone: str = "neutral",
        title: bool = False,
        model: str = "gpt-4o-mini",
        language: str = "es-PR",
        additional_instructions: str = "",
        additional_system_instructions: str = "",
        temperature: float = 0.65  # Default temperature
    ) -> list[str] | list[list[str]]:    

    # Validate model. If not supported, defualt to "gtp4o-mini"
    model = validate_openai_model(model=model)
    
    # Initialize the OpenAI API client
    client = OpenAI(api_key=fetch_openai_key(strict=True))
    
    if client is None:
        return "OpenAI client failed to initialized. Exiting."

    # Create the user's role content (prompt)
    prompt = story_prompt(
        asset_type="stories",
        title= title,
        theme = theme,
        tone = tone,
        amt = max(1, amt),
        language = language,
        additional_instructions = additional_instructions,
        additional_system_instructions = additional_system_instructions,
    )

    openai_reasoning_models = get_reasoning_openai_models()

    if title:
        story_schema = get_titled_story_schema()
    else:
        story_schema = get_story_schema()

    responses_parameters = {
        "model": model,
        "input": prompt,
        "text": story_schema,
    }


    if model not in openai_reasoning_models:
        # Add the temperature parameter to the responses_parameters dictionary
        responses_parameters["temperature"] = temperature  

    try:
        if model not in openai_reasoning_models: 
            response = client.responses.create( 
                model=model,
                temperature=temperature,
                input=prompt,
                text=story_schema
            )
        else:
            # Generate flags using OpenAI Completions
            response = client.responses.create( 
                model=model,
                input=prompt,
                text=story_schema
            )

    except OpenAIError as e:
        print(f"[ERROR] OpenAI API error: {e}")
        return 1
    
    if title:
        return parse_titled_stories(response=response.output_text) 
    else:
        return parse_stories(response=response.output_text)
    

