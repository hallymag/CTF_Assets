# CTF_Assets
Library for using LLMs to generate assets for CTF capture the flag challenges.

This software is set to require Python >=3.10

# Installation
## **Clone app from github to a local folder**
```bash
git clone https://github.com/hallymag/CTF-Assets.git
cd CTF_Assets
```  
## **Create virtual environment and upgrade python package manager**

### If you will be using your system Python
Use venv

Example:
```bash
python -m venv venv  # Create virtual env from inside CTF_Assets  
source venv/bin/activate  # Activate virtual env
python -m pip install -U pip  # Update pip
python -m pip install -e .  # Install project ctf-assets
```
To deactivate environment type ```deactivate``` 

### If you want to use many python versions
Use pyenv

Installation and configuration instruction at https://github.com/pyenv/pyenv

In linux you can install **pyenv** with
```bash
curl -fsSL https://pyenv.run | bash
```
If you are missing system dependencies see:
https://github.com/pyenv/pyenv/wiki#suggested-build-environment

To create virtual environment:
```bash
# Checkhis allows you to update the package by just pulling the changes from the repository instead o that pyenv and pyenv virtualenv is installed
pyenv --version
pyenv virtualenv --version

# List installe versions of python
pyenv versions

# If you need to list the possible versions of Python to install
pyenv versions --list

# If you need to install one
# example: peynv install 3.13.7
pyenv install <version>

# To create a virtual environment
# example: pyenv virtualenv 3.13.7 ctf-assets-3.13.7
pyenv virtualenv <python version> <virtual environment name>

# Set the local environment so that it auto activates when you move into the folder
# example: pyenv local ctf-assets-3.13.7
pyenv local <virtual environment>

# Install package in editable mode
python -m install -U pip
python -m pip install -e .
```
Example:
```bash
pyenv install 3.13.7
pyenv virtualenv 3.13.7 ctf-3.13.7
pyenv local ctf-3.13.7
python3 -m pip install -U pip
python3 -m pip install -e .
```
To deactivate environment move away from the CTF_Folder 

## To install app in a folder and have the source in a different folder: 
For example, install code to /src and run application from /app:

```bash
mkdir ~/src
cd ~/src
git clone https://github.com/hallymag/CTF_Assets.git

# Install the application to another folder in editable form. 
mkdir ~/app
cd ~/app
python -m venv venv
source venv/bin/activate 
python -m pip install -U pip
pip install -e ~/src/CTF_Assets/
```

## Set API Key
Create a .env file at the root of your project directory. Inside the file set the key.

Example:
```bash
cd ~/CTF_Assets
touch .env

# Use your editor of choice to add the following inside the file
nano .env

## Write the following inside the .env file:
OPENAI_API_KEY=<your key in here>

# Do not leave spaces before or after the "="  
# Save amd exit
```
**Remember to add the .env file to the .gitignore file to avoid stealing of keys if you decide to push your code to github.**

# Using from CLI

## Example for flags
```bash
ctf-assets flags generate-flags --amt 1 --theme "NASA" --tone "funny"
```
#### Example for Stories
```bash
ctf-assets stories generate-stories --amt 1 --theme "NASA" --tone "informational"
```
#### Example for Stories with Titles
```bash
ctf-assets stories generate-stories-with-titles --theme "Mars" --tone "Sci-Fi story" --amt 2 --additional-instructions "Stories must have at least 300 words"

# or 

ctf-assets stories generate-stories --amt 2 --theme "NASA" --tone "consipirationa theorist" --title
```
#### Example for Images
```bash
ctf-assets images generate-images --amt 1 --theme "Star Wars" --tone "funny"
```
This will return the path where the file is downloaded

### As a package:  

Example (using pyenv):
```bash
mkdir ~/myprojects
cd myprojects
git clone https://github.com/hallymag/CTF_Assets.git
mkdir thisproject
cd thisproject
pyenv install 3.13.7
pyenv virtualenv 3.13.7 ctf-assets
pyenv local ctf-assets
python -m pip install -e ../CTF_Assets
```
Create in your thisproject a file named .env that has the OPENAI_API_KEY inside
```bash
# from your thisproject directory
touch .env
```
Inside the .env type the following replacing your_key_here with your actual OPENAI key: 
OPENAI_API_KEY=your_key_here

Create your python code in file named main.py inside your thisproject directory
Content of main.py:

```python
from dotenv import load_dotenv
from ctf_assets.flag_generator import generate_flags
from ctf_assets.story_generator import generate_stories

def main():
    load_dotenv()
    flags = generate_flags(
        amt=2,
        theme="Pirates",
        tone="funny",
    )

    stories = generate_stories(
        amt=1,
        theme="Cryptography",
        title=True,
        additional_instructions="Story must have more than 500 words",
        tone="Factual",
    )

    print("FLAGS:")
    for f in flags:
        print("-", f)

    print("\nSTORIES:")
    for s in stories:
        print("-", s)

if __name__ == "__main__":
    main()
```
then run with ```python3 main.py```



   


