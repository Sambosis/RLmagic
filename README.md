```markdown
# EasyRL

EasyRL is a user-friendly Python library that simplifies the implementation and experimentation with various Reinforcement Learning (RL) algorithms. It serves as a wrapper around established RL frameworks such as Stable-Baselines3 (for PyTorch-based algorithms) and Ray RLlib (for scalable distributed training), allowing users to leverage these powerful tools without needing deep knowledge of their internal workings.

## Features

- **Supported Algorithms**: Easily switch between popular RL methods including Q-Learning, SARSA, Deep Q-Networks (DQN), Proximal Policy Optimization (PPO), Advantage Actor-Critic (A3C), and Soft Actor-Critic (SAC) via simple configuration.
- **Environment Integration**: Compatible with OpenAI Gym interfaces, with automatic handling of environment wrapping and preprocessing (e.g., normalizing observations, stacking frames for Atari-like environments).
- **Ease of Use**: High-level API for instantiating agents with configs and calling `train()` or `evaluate()` methods. Modular configs allow easy swapping of models (e.g., MLP or CNN architectures).
- **Documentation**: Comprehensive Sphinx-generated docs with API references, tutorials, and examples.
- **Python API**: Importable and usable in Python scripts, e.g., `from easyrl import RLAgent; agent = RLAgent(config); agent.train(env)`.
- **Command-Line Tool**: Interactive CLI using Typer for setting up experiments, generating code, and running training with enhanced visuals via Rich.
- **Additional Features**: JSON configs, PyTorch backend, logging with TensorBoard support, custom environment support, Python 3.8+ compatibility, and unit tests with pytest.

## Installation

EasyRL now uses [uv](https://github.com/astral-sh/uv) for dependency management. Create an isolated environment and install the
package in editable mode:

```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

The installation command will resolve and install all runtime and development dependencies defined in `pyproject.toml`, such as
Stable-Baselines3, Ray RLlib, Gymnasium, PyTorch, Typer, and Rich.

## Usage Examples

### Basic Python API Usage

1. **Import the Library**:
   ```python
   from easyrl import RLAgent
   ```

2. **Create an Agent with a Config**:
   ```python
   config = {
       "algorithm": "ppo",
       "hyperparams": {
           "learning_rate": 3e-4,
           "gamma": 0.99,
           "batch_size": 64
       },
       "model_type": "mlp",
       "env_config": {
           "env_name": "CartPole-v1"
       }
   }
   agent = RLAgent(config)
   ```

3. **Train the Agent**:
   ```python
   metrics = agent.train(env, steps=10000)
   print("Training metrics:", metrics)
   ```

4. **Evaluate the Agent**:
   ```python
   performance = agent.evaluate(env, episodes=10)
   print("Evaluation metrics:", performance)
   ```

### Using the Command-Line Interface

Run the CLI for interactive setup:

```bash
python -m easyrl.cli
```

The CLI will guide you through selecting an algorithm, inputting hyperparameters (with defaults), and generating ready-to-run Python code files saved to a specified directory.

## API Overview

- `RLAgent`: Core class for RL agents. Initialize with a config dict, then use `train()` and `evaluate()` methods.
- `Environment`: Wrapper class for managing RL environments and preprocessing.
- `Config`: Class for parsing and validating configuration dictionaries.
- `load_config(file_path)`: Load a JSON config file.
- Utility functions in `easyrl.utils.helpers` for preprocessing and logging.

For detailed API documentation, see the [full docs](docs/index.html).

## Supported Algorithms Overview

- **Q-Learning**: Value-based off-policy algorithm for discrete action spaces.
- **SARSA**: On-policy version of Q-Learning.
- **DQN**: Deep neural network extension of Q-Learning, suitable for high-dimensional spaces.
- **PPO**: Policy optimization algorithm with stability guarantees.
- **A3C**: Asynchronous advantage actor-critic for parallel training.
- **SAC**: Off-policy maximum entropy RL for exploration.

Configure via the `"algorithm"` key in your config dict.

## Documentation

- [API Reference](docs/api.html)
- [Tutorials and Examples](docs/tutorials.html)
- [Contributing Guide](docs/contributing.html)

Build the docs locally with Sphinx:

```bash
cd docs
make html
```
```