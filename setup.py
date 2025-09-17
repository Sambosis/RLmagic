"""
setup.py

This file defines the package setup for the EasyRL Python library using setuptools.
It specifies package metadata, dependencies, and entry points for the command-line interface.
"""

from setuptools import setup, find_packages

# Package metadata
NAME = "easyrl"
VERSION = "0.1.0"
AUTHOR = "EasyRL Team"  # Placeholder author
AUTHOR_EMAIL = "team@easyrl.dev"  # Placeholder email
DESCRIPTION = "A user-friendly Python library for Reinforcement Learning."
URL = "https://github.com/username/easyrl"  # Placeholder URL
LICENSE = "MIT"  # Placeholder license
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Operating System :: OS Independent",
]
KEYWORDS = "reinforcement-learning rl machine-learning ai easyrl"
PYTHON_REQUIRES = ">=3.8"

# Dependencies
INSTALL_REQUIRES = [
    "stable-baselines3",
    "gymnasium",
    "torch",
    "ray[rllib]",
    "typer",
    "rich",
    "sphinx",
    "pytest",
    "numpy",
    "tensorboard",
]

# Entry points for console scripts (CLI)
ENTRY_POINTS = {
    "console_scripts": [
        "easyrl=easyrl.cli.cli:app",  # Assumes the CLI app is defined in easyrl.cli.cli as 'app'
    ],
}

# Package discovery (finds packages under easyrl/)
PACKAGES = find_packages()

# Additional files
PACKAGE_DATA = {
    # Include any data files if needed, e.g., configs, but for now empty
}

# Setup function call
setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=open("README.md").read() if "README.md" in setup.__dict__.get("__builtins__", {}).keys() else "",  # Read README if available
    long_description_content_type="text/markdown",
    url=URL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=KEYWORDS,
    packages=PACKAGES,
    package_data=PACKAGE_DATA,
    install_requires=INSTALL_REQUIRES,
    python_requires=PYTHON_REQUIRES,
    entry_points=ENTRY_POINTS,
    # Optional: extras_require if there are optional dependencies
    # extras_require={
    #     "dev": ["black", "flake8"],
    # },
    # But keeping it simple as per description
)