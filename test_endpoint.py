from typing import Dict

def return_action(request_dict: Dict) -> list[str]:
    """Return a simple action based on nearby sensor readings."""

    sensors = request_dict.get("sensors", {})
    front = sensors.get("front", 1000)
    left = sensors.get("front_left_front", 1000)
    right = sensors.get("front_right_front", 1000)

    # If an obstacle is close in front, steer towards the side with the most room
    if front < 300:
        if left > right:
            return ["STEER_LEFT"]
        elif right > left:
            return ["STEER_RIGHT"]
        else:
            return ["DECELERATE"]  # If both sides are blocked

    return ["ACCELERATE"]
