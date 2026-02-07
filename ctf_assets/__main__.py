import argparse
import importlib    # To import modules at runtime instead of hardcoding them
import inspect  #
import sys
from dotenv import load_dotenv, find_dotenv

def main():
    parser = argparse.ArgumentParser(description="CTF Assets Generator CLI")

    # Choose the module for asset generation
    parser.add_argument(
        "asset_category", 
        type=str, 
        choices=["flags", "stories", "images"],
        help= "Module to use to generate assets (e.g. flags, stories, images)"
    )

    # Choose the function to call to generate assets
    parser.add_argument(
        "function",
        type=str,
        help="Function to call to generate assets. One of generate-flags, generate-stories, generate-images"
    )

    # Common parameters that can be used for all modules
    parser.add_argument("--theme", type=str, default= "", help= "Theme for the CTF challenge")
    parser.add_argument("--tone", type=str, default="neutral", help="Tone to use (e.g. neutral, funny, formal)")
    parser.add_argument("--amt", type=int, default=1, help="How many to generate")
    parser.add_argument("--title", action="store_true", help="Wheter to include a title in the generated stories")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="OpenAI model to use")
    parser.add_argument("--temperature", type=float, default=0.65, help="Temperature. Value range [0,2] Higher values give more randomness")
    parser.add_argument("--flag-format", type=str, default="ctf{...}", help="Format of the flag (e.g., ctf{...})")
    parser.add_argument("--language", type=str, default="es-PR", help="Language for the generated flag")
    parser.add_argument("--additional-instructions", type=str, default="", help="Additional user instructions for the generator")
    parser.add_argument("--additional-system-instructions", type=str, default="", help="Additional system level constraints or guidelines")

    # Image-specific parameters
    parser.add_argument("--image-model", type=str, default="dall-e-3", help="Image model to use (dall-e-2 or dall-e-3)")
    parser.add_argument("--prompt-model", type=str, default="gpt-4o-mini", help="Text model to generate the image prompt")
    parser.add_argument("--size", type=str, default="1024x1024", help="Image size (e.g., 1024x1024)")
    parser.add_argument("--quality", type=str, default="standard", help="Image quality (dall-e-3 only; standard or hd)")
    parser.add_argument("--style", type=str, default="vivid", help="Image style (dall-e-3 only; vivid or natural)")
    parser.add_argument("--output-dir", type=str, default="downloaded_images", help="Directory to write images to")
    parser.add_argument("--filename-prefix", type=str, default=None, help="Optional filename prefix for saved images")
    parser.add_argument("--prompt-override", type=str, default=None, help="Optional: provide your own image prompt instead of generating one")
    parser.add_argument("--return-prompt", action="store_true", help="For images: also print the final prompt used")

    args = parser.parse_args()

    # Back-compat: if user sets --model for images, treat it as --prompt-model.
    if args.asset_category == "images" and "--model" in sys.argv and "--prompt-model" not in sys.argv:
        args.prompt_model = args.model

    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path:
        load_dotenv(dotenv_path, override=False)
    else:
        print(
        "[ctf-assets] Note: No .env file found (searched upward from the current working directory). "
        "Set OPENAI_API_KEY in your environment or create a .env file.",
        file=sys.stderr,
    )

    mappings = {
        "flags": "ctf_assets.flag_generator",
        "stories": "ctf_assets.story_generator",
        "images": "ctf_assets.image_generator",
    }

    # retrieve the module name from the mappings dictionary
    module_name = mappings[args.asset_category]

    # Only allow these functions to be called from the CLI for security reasons
    allowed_functions = {
        "flags": {"generate_flags"},
        "stories": {"generate_stories", "generate_stories_with_titles"},
        "images": {"generate_images"},
    }

    try:
        # Import the module at runtime
        module = importlib.import_module(module_name)

        # Replace in the function name the hyphens with underscores
        function_name = args.function.replace("-", "_")

        if function_name not in allowed_functions.get(args.asset_category, set()):
            raise AttributeError

        # Get the function to call from the module
        func = getattr(module, function_name)

        # Check if a 'function' was passed in the module
        if not inspect.isfunction(func):
            raise AttributeError

        # Get function parameters and pass only valid arguments
        func_params = inspect.signature(func).parameters
        func_args = {k: v for k, v in vars(args).items() if k in func_params}

        # Call the function with valid arguments only (excluding 'asset_category' and 'function')
        result = func(**func_args)
        
        # Output result
        print(result)

    except ImportError:
        print(f"[ERROR] Module '{module_name}' could not be imported. Check if it exists.")
    except AttributeError:
        print(f"[ERROR] Function '{args.function}' not found in '{module_name}'.")
    except TypeError as e:
        print(f"[ERROR] TypeError: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

if __name__ == "__main__":
    main()
