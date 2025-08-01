def return_action(sensor_data):
    """
    Enkel AI:
    - Hvis det er en hindring rett foran, sving høyre
    - Hvis ikke, akselerer
    """
    front = sensor_data.get("front", 1000)
    left = sensor_data.get("front_left_front", 1000)
    right = sensor_data.get("front_right_front", 1000)

    if front < 300:
        if left > right:
            return ["STEER_LEFT"]
        else:
            return ["STEER_RIGHT"]
    else:
        return ["ACCELERATE"]
