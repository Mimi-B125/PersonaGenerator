from typing import Dict

PHYSICAL_TRAITS = {
    "hair_color": ["Blonde", "Brown", "Black", "Red", "Gray", "White"],
    "eye_color": ["Blue", "Green", "Brown", "Hazel", "Gray"],
    "height": ["Short (under 5'4\")", "Average (5'4\" to 5'9\")", "Tall (over 5'9\")"],
    "body_type": ["Slim", "Athletic", "Curvy", "Stocky", "Average"],
    "distinctive_features": ["Scar on face", "Tattoo on arm", "Freckles", 
                             "Birthmark on neck", "Pierced nose"]
}

def get_random_physical_traits() -> Dict[str, str]:
    import random
    return {trait: random.choice(values) for trait, values in PHYSICAL_TRAITS.items()}
