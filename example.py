import pygame
from src.game.core import initialize_game_state, game_loop
import src.game.core as core
from ppo_agent import PPOAgent


'''
Set seed_value to None for random seed.
Within game_loop, change get_action() to your custom models prediction for local testing and training.
'''


# Instantiate the PPO agent once so its model and filters persist
agent = PPOAgent()

def agent_action():
    """Return a single action for the current game state."""
    sensors = {s.name: s.reading for s in core.STATE.sensors}
    return agent.predict(sensors)[0]




if __name__ == '__main__':
    seed_value = 12345
    pygame.init()
    initialize_game_state("http://example.com/api/predict", seed_value)
    # Override the default manual control with our agent policy
    core.get_action = agent_action
    game_loop(verbose=True)  # For pygame window
    pygame.quit()
