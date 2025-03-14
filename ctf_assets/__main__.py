import argparse
import importlib    # To import modules at runtime instead of hardcoding them
import inspect  #

def main():
    parser = argparse.ArgumentParser(description="CTF Assets Generator CLI")

    # Choose the module for asset generation
    parser.add_argument(
        "module", 
        type=str, 
        choices=["flags", "stories", "images"],
        help= "Module to use to generate assets (e.g. flags, stories, images)"
    )

    # Choose the function to call to generate assets
    parser.add_argument(
        "function",
        type=str,
        help="Function to call to generate assets. One of generate_flags, generate_stories, generate_images"
    )

    # Common parameters that can be used for all modules
    parser.add_argument("--theme", type=str, default= "", help= "Theme for the CTF challenge")
    parser.add_argument("--tone", type=str, default="neutral", help="Tone to use (e.g. neutral, funny, formal)")
    parser.add_argument("--amt", type=int, default=1, help="How many to generate")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="OpenAI model to use")
    parser.add_argument("--temperature", type=float, default=0.55, help="Temperature. Value range [0,2] Higher values give more randomness")
    parser.add_argument("--flag-format", type=str, default="ctf{...}", help="Format of the flag (e.g., ctf{...})")
    parser.add_argument("--response-format", type=str, default="JSON", help="Format of the response (e.g. JSON or [item1, item2, item3])")
    parser.add_argument("--language", type=str, default="es-PR", help="Language for the generated flag")
    parser.add_argument("--additional-instructions", type=str, default="", help="Additional user instructions for the generator")
    parser.add_argument("--additional-system-instructions", type=str, default="", help="Additional system level constraints or guidelines")

    args = parser.parse_args()

    mappings = {
        "flags": "ctf_assets.flag_generator",
        "stories": "ctf_assets.story_generator",
        "images": "ctf_assets.image_generator",
    }

    # retrieve the module name from the mappings dictionary
    module_name = mappings[args.module]

    try:
        # Import the module at runtime
        module = importlib.import_module(module_name)

        # Get the function to call from the module
        func = getattr(module, args.function)

        # Check if that a function was passed in the module
        if not inspect.isfunction(func):
            raise AttributeError

        # Get function parameters and pass only valid arguments
        func_params = inspect.signature(func).parameters
        func_args = {k: v for k, v in vars(args).items() if k in func_params}

        # Call the function with valid arguments only (excluding 'module' and 'function')
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