import random
from typing import Dict, List, Tuple

ETHNICITIES = ["Caucasian", "African American", "Hispanic", "Asian", "Eastern European", "Indigenous"]
RELIGIONS = ["Christian", "Buddhist", "Agnostic", "Atheist", "Spiritual but not religious"]
LANGUAGES = ["English", "Spanish", "French", "Chinese", "German", "Japanese"]

REGIONS = {
    'Northeast': {'Accents': 'Northeast Accents', 'Slang': 'Bubbler, yous guys'},
    'Southeast': {'Accents': 'Southern Accent', 'Slang': 'Y’all, fixin’ to'},
    'Midwest': {'Accents': 'Midwestern English', 'Slang': 'You betcha, pop'},
    'Southwest': {'Accents': 'Southwestern English', 'Slang': 'Hella, dude'},
    'West': {'Accents': 'Western American', 'Slang': 'Gnarly, no worries'},
    'Pacific Northwest': {'Accents': 'Pacific Northwest', 'Slang': 'The 253'},
    'Upper Midwest': {'Accents': 'Upper Midwest', 'Slang': 'Uff da, Dontcha know'}
}

def get_random_cultural_profile() -> Tuple[str, Dict[str, str], Dict[str, List[str]]]:
    """Returns a randomized: (Region Name, Region Data Dict, Cultural Background Dict)"""
    chosen_region = random.choice(list(REGIONS.keys()))
    background = {
        'ethnicity': random.choice(ETHNICITIES),
        'religion': random.choice(RELIGIONS),
        'languages': random.sample(LANGUAGES, k=1)
    }
    return chosen_region, REGIONS[chosen_region], background
