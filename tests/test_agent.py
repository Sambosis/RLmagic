"""
tests/test_agent.py

This module contains unit tests for the RLAgent class using pytest.
The tests cover the initialization, training, and evaluation functionalities of the RLAgent.

Test coverage includes:
- Initialization with valid configuration.
- Training for a short number of steps to avoid long execution times.
- Evaluation over a small number of episodes.
- Error handling for invalid inputs.

Fixtures are used to set up test environments and agents efficiently.
"""

import pytest
import gymnasium as gym
from unittest.mock import Mock

from easyrl.core.agent import RLAgent
from easyrl.core.environment import Environment
from easyrl.core.config import Config


# Fixture to create a sample valid config for RLAgent
@pytest.fixture
def sample_config():
    """
    Fixture that returns a sample configuration dictionary for testing RLAgent.

    Returns:
        dict: A valid configuration with supported algorithm, hyperparameters, model type, and env config.
    """
    return {
        "algorithm": "ppo",
        "hyperparams": {"learning_rate": 0.001, "gamma": 0.99, "batch_size": 32},
        "model_type": "mlp",
        "env_config": {"env_name": "Pendulum-v1"}  # Simple continuous action environment for fast tests
    }


# Fixture to create a sample RLAgent instance
@pytest.fixture
def sample_agent(sample_config):
    """
    Fixture that initializes and returns an RLAgent instance with sample config.

    Args:
        sample_config (dict): Sample configuration dictionary.

    Returns:
        RLAgent: Initialized RLAgent instance.

    Raises:
        pytest.skip: If gymnasium environment cannot be created, skipping tests to avoid failures in headless environments.
    """
    try:
        return RLAgent(sample_config)
    except Exception as e:
        pytest.skip(f"Failed to initialize RLAgent due to environment issue: {e}")


# Fixture to create a sample Environment instance compatible with RLAgent
@pytest.fixture
def sample_env(sample_config):
    """
    Fixture that initializes and returns an Environment instance.

    Args:
        sample_config (dict): Sample configuration dictionary.

    Returns:
        Environment: Initialized Environment instance.
    """
    try:
        return Environment(sample_config["env_config"])
    except Exception as e:
        pytest.skip(f"Failed to initialize Environment due to issue: {e}")


def test_rl_agent_init_valid_config(sample_config):
    """
    Test RLAgent initialization with a valid configuration dictionary.

    Verifies that:
    - RLAgent initializes without errors.
    - Attributes are set correctly based on config.
    - Model is None initially.
    - Backend is 'stable_baselines3' for supported algorithms.
    """
    # Test with dict config
    agent = RLAgent(sample_config)
    assert isinstance(agent.config, Config)
    assert agent.config.algorithm == "ppo"
    assert agent.config.model_type == "mlp"
    assert agent.model is None
    assert agent.backend == "stable_baselines3"

    # Test with Config instance
    config_obj = Config(sample_config)
    agent2 = RLAgent(config_obj)
    assert agent2.config == config_obj
    assert agent2.backend == "stable_baselines3"


def test_rl_agent_init_invalid_config():
    """
    Test RLAgent initialization with invalid configurations.

    Verifies error handling for:
    - Unsupported algorithm.
    - Invalid config types.
    """
    # Invalid algorithm
    invalid_config = {"algorithm": "invalid_alg", "hyperparams": {}, "model_type": "mlp", "env_config": {}}
    with pytest.raises(ValueError, match="Unsupported algorithm"):
        RLAgent(invalid_config)

    # Invalid config type
    with pytest.raises(ValueError, match="config must be a dict or Config instance"):
        RLAgent("invalid")


def test_rl_agent_train(sample_agent, sample_env):
    """
    Test RLAgent training with a short number of steps.

    Verifies that:
    - Training completes without errors.
    - Returns a dictionary with expected keys.
    - Model is initialized after training.
    """
    steps = 100  # Short training for unit tests
    metrics = sample_agent.train(sample_env, steps)
    assert isinstance(metrics, dict)
    assert "steps" in metrics
    assert "mean_reward" in metrics
    assert metrics["steps"] == steps
    assert sample_agent.model is not None  # Model should be initialized


def test_rl_agent_train_invalid_steps(sample_agent, sample_env):
    """
    Test RLAgent train method with invalid steps.

    Verifies error handling for negative or zero steps.
    """
    with pytest.raises(ValueError, match="steps must be a positive integer"):
        sample_agent.train(sample_env, -1)
    
    with pytest.raises(ValueError, match="steps must be a positive integer"):
        sample_agent.train(sample_env, 0.5)


def test_rl_agent_evaluate(sample_agent, sample_env):
    """
    Test RLAgent evaluation after training.

    Verifies that:
    - Evaluation requires a trained model (skips if not trained).
    - Returns a dictionary with mean and std reward.
    - Handles model not initialized.
    """
    # Skip if model not trained; otherwise, train briefly
    if sample_agent.model is None:
        sample_agent.train(sample_env, 10)  # Quick train
    
    episodes = 2  # Small number for tests
    eval_metrics = sample_agent.evaluate(sample_env, episodes)
    assert isinstance(eval_metrics, dict)
    assert "mean_reward" in eval_metrics
    assert "std_reward" in eval_metrics
    assert isinstance(eval_metrics["mean_reward"], (float, type(None)))


def test_rl_agent_evaluate_untrained_model(sample_agent, sample_env):
    """
    Test RLAgent evaluation with untrained (None) model.

    Verifies ValueError is raised when model is None.
    """
    # Wipe model for test
    sample_agent.model = None
    with pytest.raises(ValueError, match="Model not initialized"):
        sample_agent.evaluate(sample_env, 2)


def test_rl_agent_evaluate_invalid_episodes(sample_agent, sample_env):
    """
    Test RLAgent evaluate method with invalid episodes.

    Verifies error handling for invalid episode counts.
    """
    with pytest.raises(ValueError, match="episodes must be a positive integer"):
        sample_agent.evaluate(sample_env, -1)
    
    with pytest.raises(ValueError, match="episodes must be a positive integer"):
        sample_agent.evaluate(sample_env, 0.5)