"""
EasyRL: A user-friendly Python library for simplifying Reinforcement Learning implementations.

This package provides wrappers around popular RL frameworks, offering a high-level API
for easy experimentation with algorithms like Q-Learning, SARSA, DQN, PPO, A3C, and SAC.
It includes support for environment integration compatible with OpenAI Gym, modular configurations,
and a CLI tool for interactive setup and code generation.

Main exports:
- RLAgent: Core class for RL agents, handling initialization, training, and evaluation.
- Environment: Wrapper class for RL environments with preprocessing.
- Config: Class for parsing and validating RL experiment configurations.
- load_config: Function to load configurations from JSON files.
- generate_code: CLI function to generate Python code for RL agents.
- cli_setup: Function for interactive CLI configuration gathering.
"""

# Core components
from .core.agent import RLAgent
from .core.environment import Environment
from .core.config import Config, load_config

# CLI tools
# from .cli.cli import generate_code, cli_setup  # Commented to avoid typer import

__version__ = "1.0.0"  # Placeholder version; update as needed.