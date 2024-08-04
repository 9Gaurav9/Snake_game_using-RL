# Snake Game with Reinforcement Learning

This project implements a Snake game using Reinforcement Learning (RL) techniques. The RL agent learns to play the game by interacting with the environment, receiving rewards, and improving its performance over time.

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Code Structure](#code-structure)
7. [License](#license)
8. [Acknowledgments](#acknowledgments)

## Overview

The Snake game is a classic arcade game where the player controls a snake that moves around the screen to eat food and grow longer. The objective is to avoid collisions with the walls or itself while achieving the highest possible score.

This implementation uses a Deep Q-Learning (DQN) algorithm to train an agent to play the Snake game. The agent learns from its experiences and improves its policy to maximize the score.

## Features

- **Reinforcement Learning**: Uses DQN to train the agent.
- **Game Environment**: Implemented using Pygame for visualization.
- **Training and Testing**: Includes scripts for training the agent and testing its performance.
- **Model Saving and Loading**: Save and load trained models.

## Requirements

- Python 3.12 or higher
- TensorFlow 2.x
- Keras
- Pygame
- NumPy

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/9Gaurav9/Snake_game_using-RL.git
    cd snake_rl
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Train the Agent**:
    ```bash
    python train.py
    ```

2. **Test the Agent**:
    ```bash
    python test.py
    ```

   Ensure that you have a trained model saved as `snake-dqn-final.weights.h5` or update the filename in `test.py` accordingly.

## Code Structure

- `train.py`: Script for training the DQN agent.
- `test.py`: Script for testing the trained agent.
- `agent.py`: Contains the implementation of the DQN agent.
- `game.py`: Contains the implementation of the Snake game environment using Pygame.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Pygame for the game development framework.
- TensorFlow and Keras for the reinforcement learning implementation.
