import json
import os


class Config:
    """
    Class to parse and validate configuration dictionaries for Reinforcement Learning experiments.

    Attributes:
        algorithm (str): The RL algorithm to use (e.g., 'ppo', 'dqn'). Default is 'ppo'.
        hyperparams (dict): Dictionary of hyperparameters for the algorithm. Default is an empty dict.
        model_type (str): The model architecture (e.g., 'mlp', 'cnn'). Default is an empty string (to be determined or overridden).
        env_config (dict): Configuration for the environment, such as name and settings. Default is an empty dict.

    Supported algorithms: 'q_learning', 'sarsa', 'dqn', 'ppo', 'a3c', 'sac'.
    """

    SUPPORTED_ALGORITHMS = {'q_learning', 'sarsa', 'dqn', 'ppo', 'a3c', 'sac'}

    def __init__(self, config_dict=None):
        """
        Initializes the Config instance from a configuration dictionary.

        Args:
            config_dict (dict, optional): Dictionary containing configuration options. If None, uses defaults.

        Raises:
            ValueError: If 'algorithm' is provided but not in the list of supported algorithms,
                        or if any required attributes are of incorrect type.
        """
        if config_dict is None:
            config_dict = {}

        # Set algorithm with default and validation
        self.algorithm = config_dict.get('algorithm', 'ppo').lower()
        if self.algorithm not in self.SUPPORTED_ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {self.algorithm}. Supported: {', '.join(sorted(self.SUPPORTED_ALGORITHMS))}")

        # Set other attributes with defaults
        self.hyperparams = config_dict.get('hyperparams', {})
        self.model_type = config_dict.get('model_type', '')
        self.env_config = config_dict.get('env_config', {})

        # Basic type checks
        if not isinstance(self.hyperparams, dict):
            raise ValueError("hyperparams must be a dictionary.")
        if not isinstance(self.env_config, dict):
            raise ValueError("env_config must be a dictionary.")
        if not isinstance(self.model_type, str):
            raise ValueError("model_type must be a string.")


def load_config(file_path):
    """
    Loads and parses a JSON configuration file into a dictionary.

    Args:
        file_path (str): Path to the JSON file to load.

    Returns:
        dict: The parsed configuration dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error parsing JSON in {file_path}: {e.msg}", e.doc, e.pos)