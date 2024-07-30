import numpy as np
from game import SnakeGame
from agent import DQNSnake

EPISODES = 1000

def main():
    state_size = 4  # Example state size, change according to your actual state size
    action_size = 4  # Example action size, change according to your actual action size
    agent = DQNSnake(state_size, action_size)
    batch_size = 32
    game = SnakeGame()

    for e in range(EPISODES):
        state = game.reset()
        state = np.reshape(state, [1, state_size])
        for time in range(500):
            action = agent.act(state)
            next_state, reward, done, _ = game.step(action)
            reward = reward if not done else -10
            next_state = np.reshape(next_state, [1, state_size])
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                print(f"episode: {e}/{EPISODES}, score: {time}, e: {agent.epsilon:.2}")
                break
            if len(agent.memory) > batch_size:
                agent.replay(batch_size)
        if e % 50 == 0:
            agent.save(f"snake-dqn-{e}")

if __name__ == "__main__":
    main()
