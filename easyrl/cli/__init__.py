"""
EasyRL CLI Package

This package provides command-line interface components for the EasyRL library,
including functions for interactive setup and code generation.
"""

from .cli import generate_code, cli_setup

__all__ = [
    'generate_code',
    'cli_setup'
]