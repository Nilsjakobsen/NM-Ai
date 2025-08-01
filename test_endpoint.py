from typing import Dict
from ppo_agent import PPOAgent

# Global agent instance reused between calls
agent = PPOAgent()


def return_action(request_dict: Dict) -> list[str]:
    """Return next actions for the car using a PPO policy with Kalman filtering."""
    sensors = request_dict.get("sensors", {})
    return agent.predict(sensors)
