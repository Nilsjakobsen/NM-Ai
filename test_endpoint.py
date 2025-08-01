def return_action(request_dict):
    """Very simple rule based agent used for connection tests."""

    sensors = request_dict.get("sensors", {})
    front = sensors.get("front", 1000)
    left = sensors.get("front_left_front", 1000)
    right = sensors.get("front_right_front", 1000)

    if front < 300:
        if left > right:
            return ["STEER_LEFT"]
        return ["STEER_RIGHT"]
    return ["ACCELERATE"]
