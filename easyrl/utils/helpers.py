"""
easyrl/utils/helpers.py

This module provides utility functions for preprocessing observations and logging
in the EasyRL library. It includes functions to preprocess observations with
normalization or clipping, and to log rewards to TensorBoard for monitoring.

External dependencies:
- numpy: For numerical operations on observations.
- torch: For integration with TensorBoard logging (via torch.utils.tensorboard).
"""

import numpy as np
from torch.utils.tensorboard import SummaryWriter


def preprocess_obs(obs: np.ndarray, method: str, **kwargs) -> np.ndarray:
    """
    Applies preprocessing to the observation based on the specified method.

    Args:
        obs (np.ndarray): The observation array to preprocess (e.g., from Gym environment).
        method (str): The preprocessing method to apply. Supported: 'normalize', 'clip'.
        **kwargs: Additional parameters for preprocessing.
            - For 'normalize': 'mean' (float, default 0.0), 'std' (float, default 1.0) for z-score normalization (obs - mean) / std.
            - For 'clip': 'min_val' (float, default 0.0), 'max_val' (float, default 1.0) to clip to this range.

    Returns:
        np.ndarray: The preprocessed observation.

    Raises:
        ValueError: If the method is unsupported or input is not a numpy array.
        RuntimeError: If preprocessing fails (e.g., division by zero in normalization).
    """
    if not isinstance(obs, np.ndarray):
        raise ValueError("obs must be a numpy array.")
    
    method = method.lower()
    if method == "normalize":
        mean = kwargs.get("mean", 0.0)
        std = kwargs.get("std", 1.0)
        if std == 0:
            raise RuntimeError("Standard deviation cannot be zero for normalization.")
        return (obs - mean) / std
    elif method == "clip":
        min_val = kwargs.get("min_val", 0.0)
        max_val = kwargs.get("max_val", 1.0)
        return np.clip(obs, min_val, max_val)
    else:
        raise ValueError(f"Unsupported preprocessing method: {method}. Supported: 'normalize', 'clip'.")


def log_to_tensorboard(logger: SummaryWriter, rewards: float, step: int) -> None:
    """
    Logs the reward value to TensorBoard at the specified step, if TensorBoard is available.

    This function checks if the logger is a valid SummaryWriter instance and logs the rewards.
    If not, it silently skips logging (e.g., if TensorBoard is not set up).

    Args:
        logger (SummaryWriter): The TensorBoard SummaryWriter instance for logging.
        rewards (float): The reward value to log (e.g., mean reward).
        step (int): The training step at which to log the reward.

    Raises:
        ValueError: If logger is not a SummaryWriter instance or inputs are invalid.
    """
    if not isinstance(logger, SummaryWriter):
        raise ValueError("logger must be a torch.utils.tensorboard.SummaryWriter instance.")
    if not isinstance(step, int) or step < 0:
        raise ValueError("step must be a non-negative integer.")
    if not isinstance(rewards, (float, int)):
        raise ValueError("rewards must be a numeric value.")
    
    # Log the reward
    try:
        logger.add_scalar("Rewards", rewards, step)
    except Exception as e:
        # If logging fails (e.g., TensorBoard not installed or file issues), silently pass
        pass