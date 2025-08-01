from typing import Dict, List
from kalman_filter import KalmanFilter1D

try:
    from stable_baselines3 import PPO
except Exception:  # pragma: no cover - library optional
    PPO = None

# Map discrete action index to game action string
ACTION_MAP = {
    0: "NOTHING",
    1: "ACCELERATE",
    2: "DECELERATE",
    3: "STEER_LEFT",
    4: "STEER_RIGHT",
}

class PPOAgent:
    """Load a PPO policy and predict actions from sensor observations."""

    def __init__(self, model_path: str = "models/ppo_model.zip"):
        self.model = None
        if PPO is not None:
            try:
                self.model = PPO.load(model_path)
            except FileNotFoundError:
                pass
        # Initialize Kalman filters for all sensors
        self.filters: Dict[str, KalmanFilter1D] = {}

    def _ensure_filters(self, sensor_names: List[str]):
        for name in sensor_names:
            if name not in self.filters:
                self.filters[name] = KalmanFilter1D()

    def _filter_observation(self, sensors: Dict[str, float]) -> List[float]:
        self._ensure_filters(list(sensors.keys()))
        obs = []
        for name, val in sensors.items():
            filt = self.filters[name]
            if val is None:
                val = 1000.0
            obs.append(filt.update(float(val)))
        return obs

    def predict(self, sensors: Dict[str, float]) -> List[str]:
        """Return a batch of actions from the PPO policy."""
        obs = self._filter_observation(sensors)

        # Fallback rule-based logic if PPO model not available
        if self.model is None:
            front = sensors.get("front", 1000)
            left = sensors.get("front_left_front", 1000)
            right = sensors.get("front_right_front", 1000)
            if front < 300:
                return ["STEER_LEFT"] if left > right else ["STEER_RIGHT"]
            return ["ACCELERATE"]

        action_idx, _ = self.model.predict(obs, deterministic=True)
        action = ACTION_MAP.get(int(action_idx), "NOTHING")
        return [action]
