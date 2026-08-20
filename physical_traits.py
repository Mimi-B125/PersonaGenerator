# physical_traits.py
import random
from typing import Dict, List, Any

# Demographic distributions driven by biological sex and age boundaries
HAIR_BY_AGE = {
    "young_adult": ["Blonde", "Deep Brown", "Jet Black", "Auburn Red", "Dyed Platinum", "Faded Copper"],
    "middle_aged": ["Blonde", "Deep Brown", "Jet Black", "Auburn Red", "Salt and Pepper", "Early Gray"],
    "senior": ["Silver Gray", "Snow White", "Thinning Slate", "Dyed Dark Brown"]
}

HEIGHT_BY_SEX = {
    "female": ["Petite (under 5'3\")", "Average (5'4\" to 5'7\")", "Tall (over 5'8\")"],
    "male": ["Short (under 5'6\")", "Average (5'7\" to 5'11\")", "Tall (over 6'0\")"]
}

BODY_BY_SEX = {
    "female": {"Slim": 0.2, "Athletic": 0.2, "Curvy / Voluptuous": 0.3, "Average": 0.3},
    "male": {"Slim": 0.2, "Athletic / Toned": 0.3, "Stocky / Broad-Shouldered": 0.3, "Average": 0.2}
}

EYE_COLORS = ["Piercing Blue", "Emerald Green", "Warm Brown", "Deep Hazel", "Stormy Gray"]

DISTINCTIVE_FEATURES = [
    "Faint scar across the left eyebrow", "Intricate sleeve tattoo on the forearm", 
    "Splayed freckles across the bridge of the nose", "Prominent birthmark on the side of the neck", 
    "Discreet nose piercing", "Fine laugh lines around the eyes", "Calloused hands from manual work",
    "Consistently wears classic wire-rimmed glasses"
]

def get_random_physical_traits(sex: str = "female", age: int = 35) -> Dict[str, str]:
    """
    Generates a realistic, highly descriptive, and demographically consistent 
    dictionary of physical traits based on biological sex and age metrics.
    """
    # 1. Normalize structural input parameters
    sex_clean = sex.lower() if sex.lower() in ["female", "male"] else "female"
    
    if age < 30:
        age_group = "young_adult"
    elif age < 55:
        age_group = "middle_aged"
    else:
        age_group = "senior"

    # 2. Extract tailored trait configurations
    hair_pool = HAIR_BY_AGE[age_group]
    height_pool = HEIGHT_BY_SEX[sex_clean]
    
    body_matrix = BODY_BY_SEX[sex_clean]
    body_choices = list(body_matrix.keys())
    body_weights = list(body_matrix.values())

    # 3. Compile the structural physical payload
    return {
        "hair_color": random.choice(hair_pool),
        "eye_color": random.choice(EYE_COLORS),
        "height": random.choice(height_pool),
        "body_type": random.choices(body_choices, weights=body_weights, k=1)[0],
        "distinctive_features": random.choice(DISTINCTIVE_FEATURES)
    }
