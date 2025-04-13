import os
import re

# To DO: 
#   Use regex instead of creating valid_char
#   use re.compile to compile the regex pattern once and use it multiple times
#   
def remove_invalid_chars(filename: str) -> str:
    # re.compile
    pass


def sanitize_filename(filename: str) -> str:
    """
    Sanitize the filename by removing invalid characters.

    Args:
        filename (str): The original filename.

    Returns:
        str: The sanitized filename.
    """
    # Define a set of valid characters
    valid_chars = "-_.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Remove invalid characters
    return ''.join(c for c in filename if c in valid_chars)

def create_file(file_path: str, content: str, filename: str) -> None:
    """
    Create a file with the specified content.

    Args:
        file_path (str): The path where the file will be created.
        content (str): The content to write into the file.

    Raises:
        OSError: If there is an error creating or writing to the file.
    """
    arr = list(content)
    
    try:
        with open(file_path, 'w') as file:
            pass

    except OSError as e:
            raise OSError(f"Error creating file {file_path}: {e}")
