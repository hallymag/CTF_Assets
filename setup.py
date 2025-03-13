from setuptools import setup, find_packages

setup(
    name="ctf_assets",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ctf-assets=ctf_assets.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.9",
)
