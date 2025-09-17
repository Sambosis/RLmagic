# -*- coding: utf-8 -*-
"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

# Add the project root directory to sys.path to allow importing modules
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../easyrl'))

# -- Project information -----------------------------------------------------

project = 'EasyRL'
copyright = '2023, EasyRL Team'
author = 'EasyRL Team'
release = '1.0.0'
version = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',      # Automatically extract docstrings from modules
    'sphinx.ext.viewcode',     # Add source code links to documentation
    'sphinx.ext.napoleon',     # Support for Google/NumPy style docstrings
    'sphinx.ext.intersphinx',  # Link to external documentation (e.g., Python stdlib)
    'sphinx.ext.todo',         # Support for todo items
    'sphinx.ext.autosummary',  # Generate autosummary tables
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = {
    '.rst': None,
    '.md': None,
}

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'  # A clean, responsive theme; can be changed to 'default' or 'sphinx_rtd_theme' if preferred

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration --------------------------------------------------

# -- Options for autodoc extension --------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# -- Options for intersphinx extension ---------------------------------------
# Reference to external documentation
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'gymnasium': ('https://gymnasium.farama.org/', None),
    'stable_baselines3': ('https://stable-baselines3.readthedocs.io/en/master/', None),
}

# -- Options for napoleon extension ------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

# -- Options for HTML output with alabaster theme -----------------------------
html_theme_options = {
    'description': 'A user-friendly Python library for Reinforcement Learning',
    'github_user': 'username',  # Placeholder; update with actual GitHub username
    'github_repo': 'easyrl',    # Placeholder; update with actual repository name
    'github_banner': True,
    'show_powered_by': False,
    'extra_nav_links': {
        'Installation': 'installation.html',
        'API Reference': 'api.html',
    },
}