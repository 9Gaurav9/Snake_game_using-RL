import numpy as np
from game import SnakeGame
from agent import DQNSnake

def main():
    state_size = 4  # Example state size, change according to your actual state size
    action_size = 4  # Example action size, change according to your actual action size
    agent = DQNSnake(state_size, action_size)
    agent.load("snake-dqn-final")
    game = SnakeGame()
    
    while True:
        state = game.reset()
        state = np.reshape(state, [1, state_size])
        while True:
            action = agent.act(state)
            next_state, reward, done, _ = game.step(action)
            next_state = np.reshape(next_state, [1, state_size])
            state = next_state
            if done:
                break

if __name__ == "__main__":
    main()
