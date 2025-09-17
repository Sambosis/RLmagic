Welcome to EasyRL
==================

EasyRL is a user-friendly Python library that simplifies the implementation and experimentation 
with various Reinforcement Learning (RL) algorithms. It serves as a wrapper around established 
RL frameworks such as Stable-Baselines3 and Ray RLlib, allowing users to leverage these without 
deep knowledge of their internals.

Supported Algorithms
---------------------

EasyRL supports a selection of popular RL methods, including:

- Q-Learning
- SARSA
- Deep Q-Networks (DQN)
- Proximal Policy Optimization (PPO)
- Advantage Actor-Critic (A3C)
- Soft Actor-Critic (SAC)

Users can switch between these algorithms by providing a simple configuration dictionary 
or JSON/YAML file, specifying the algorithm type, hyperparameters, and environment details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   tutorials
   installation
   usage_examples

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`