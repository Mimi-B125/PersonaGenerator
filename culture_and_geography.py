# culture_and_geography.py
import random
from typing import Dict, Any, Tuple

# Comprehensive, geographically bound matrix ensuring cultural and linguistic realism
REGIONAL_MATRIX: Dict[str, Dict[str, Any]] = {
    "Northeast": {
        "accent": "Northeast (Boston/New York variant)",
        "slang": "Wicked, bubbler, yis guys, down-city",
        "languages": {"English": 0.75, "Spanish": 0.15, "French": 0.07, "Mandarin": 0.03},
        "ethnicities": {"Caucasian": 0.65, "African American": 0.15, "Hispanic": 0.12, "Asian": 0.08}
    },
    "Southeast": {
        "accent": "Southern Drawl",
        "slang": "Y’all, fixin’ to, bless your heart, directly",
        "languages": {"English": 0.90, "Spanish": 0.08, "French": 0.02},
        "ethnicities": {"African American": 0.40, "Caucasian": 0.50, "Hispanic": 0.08, "Indigenous": 0.02}
    },
    "Southwest": {
        "accent": "Southwestern English",
        "slang": "Hella, dusty, out-here, ranch-style",
        "languages": {"English": 0.60, "Spanish": 0.35, "Indigenous (Navajo/Zuni)": 0.05},
        "ethnicities": {"Hispanic": 0.45, "Caucasian": 0.40, "Indigenous": 0.10, "Asian": 0.05}
    },
    "Pacific Northwest": {
        "accent": "Pacific Northwest Standard",
        "slang": "The 253, sun-break, micro-brew, spendy",
        "languages": {"English": 0.85, "Mandarin": 0.05, "Japanese": 0.05, "Spanish": 0.05},
        "ethnicities": {"Caucasian": 0.70, "Asian": 0.15, "Hispanic": 0.10, "African American": 0.05}
    },
    "Upper Midwest": {
        "accent": "North-Central American (Minnesota/Wisconsin variant)",
        "slang": "Uff da, dontcha know, hotdish, ope",
        "languages": {"English": 0.92, "German": 0.04, "Spanish": 0.02, "Hmong": 0.02},
        "ethnicities": {"Caucasian": 0.82, "Eastern European": 0.08, "Indigenous": 0.04, "Asian": 0.06}
    }
}

# Culturally independent or global spiritual choices
RELIGIONS = ["Christian", "Buddhist", "Agnostic", "Atheist", "Spiritual but not religious"]

def get_random_cultural_profile() -> Tuple[str, Dict[str, str], Dict[str, Any]]:
    """
    Generates a geographically grounded, realistic cultural profile.
    
    Returns: 
        Tuple[str, Dict[str, str], Dict[str, Any]]: 
        (Region Name, Region Data Dict, Cultural Background Dict)
    """
    # 1. Select the geographic anchor
    region_name = random.choice(list(REGIONAL_MATRIX.keys()))
    meta = REGIONAL_MATRIX[region_name]

    # 2. Extract weighted distributions derived from chosen region
    lang_choices, lang_weights = list(meta["languages"].keys()), list(meta["languages"].values())
    eth_choices, eth_weights = list(meta["ethnicities"].keys()), list(meta["ethnicities"].values())

    # 3. Deterministically sample characteristics using regional weights
    chosen_language = random.choices(lang_choices, weights=lang_weights, k=1)[0]
    chosen_ethnicity = random.choices(eth_choices, weights=eth_weights, k=1)[0]
    chosen_religion = random.choice(RELIGIONS)

    # 4. Format objects to match your exact downstream expectations
    region_data = {
        "Accents": meta["accent"],
        "Slang": meta["slang"]
    }

    background = {
        "ethnicity": chosen_ethnicity,
        "religion": chosen_religion,
        "languages": [chosen_language]  # Structured inside a list to retain original variable type
    }

    return region_name, region_data, background
