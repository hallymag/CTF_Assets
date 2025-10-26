# CTF_Assets
Library for using LLMs to generate assets for CTF capture the flag challenges.

Install a Python Version Manager such as pyenv. This software is set to require Python >=3.12.9

## Installation
#### Clone app from github to a local folder
```bash
git clone https://github.com/hallymag/CTF-Assets.git
cd CTF_Assets
```
### 1. Create virtual environment and upgrade python package manager

```bash
python -m venv venv
source venv/bin/activate
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```

### 2. Install python app to run from a local path
#### Clone app from github to a local folder
```bash
git clone https://github.com/hallymag/CTF_Assets.git
```
#### Install package.
Install package as editable since it is still in development. 
This allows you to update the package by just pulling the changes from the repository instead of reinstalling it. When the package is finalized it will be published to PyPi
```bash
pip install -e /path/to/package/
```
### 2. Set API Key
Create ```.env``` file in the project root folder and add your OpenAI API key

#### Windows
Save API key as environment variable in Windows

```PowerShell
$ENV:OPENAI_API_KEY = "<your-key-value-here>"
```

#### Linux or macOS

Create a .env file at the root of your project directory. Inside the file set the key

```bash
cd /root/to/project

# create and activate your virtual environment with prefered tool python, conda, poetry, virtualenv, etc
python -m venv venv 
source venv/bin/activate  # For Linux

touch .env

# Use your editor of choice to add the following inside the file
vim .env
```
Write the following inside the .env file:
```bash
OPENAI_API_KEY=<your key in here>
```
Do not leave spaces before or after the "="  
**Remember to add the .env file to the .gitignore file to avoid stealing of keys if you decide to push your code to github.**

## Usage
### From the CLI
#### Example for flags
```bash
ctf-assets flags generate-flags --amt 1 --theme "NASA" --tone "funny"
```
#### Example for Stories
```bash
ctf-assets stories generate-stories --amt 1 --theme "NASA" --tone "informational"
```
#### Example for Stories with Titles
```bash
ctf-assets stories generate-stories --amt 2 --theme "NASA" --tone "consipirationa theorist" --title True
```
#### Example for Images
```bash
ctf-assets images generate-images --amt 1 --theme "Star Wars" --tone "funny"
```
### As a package:  
Import the package
Examples:
If you did: ```git clone https://github.com/hallymag/CTF_Assets.git```
```bash
from CTF_Assets.ctf_assets.flag_generator import generate_flags
flags = generate_flags(theme="NASA", tone-"funny", amt=10)
```



   


