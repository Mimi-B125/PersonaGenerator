# social_and_lifestyle.py
import random
from typing import Dict, Tuple, Any

# Defining core archetypes that link family patterns, relationship habits, and tech expressions
LIFESTYLE_ARCHETYPES: Dict[str, Dict[str, Any]] = {
    "Secure / Connected": {
        "family_dynamics": ["Close-knit Family", "Supportive but Distant Family"],
        "relationship_pool": {
            "In a Relationship": "Committed to a partner; built on stable foundations.",
            "Single": "Comfortable with independence; open to meaningful connection."
        },
        "contentment_distribution": {"Happy": 0.7, "Content": 0.3, "Dissatisfied": 0.0},
        "fashion_preferences": ["Minimalist", "Preppy", "Casual", "Trendy"],
        "tech_affinity": {"Intermediate": 0.5, "Advanced": 0.4, "Expert": 0.1}
    },
    "Avoidant / Independent": {
        "family_dynamics": ["Absent Caregiver Dynamic", "Secretive Family"],
        "relationship_pool": {
            "Single": "Not in a relationship; heavily prioritizing personal autonomy.",
            "Friends with Benefits": "Sexual interactions bound by strict personal limits."
        },
        "contentment_distribution": {"Content": 0.6, "Happy": 0.2, "Dissatisfied": 0.2},
        "fashion_preferences": ["Minimalist", "Edgy", "Vintage"],
        "tech_affinity": {"Advanced": 0.4, "Expert": 0.5, "Beginner": 0.1}
    },
    "Anxious / Intense": {
        "family_dynamics": ["High-conflict Family", "Secretive Family"],
        "relationship_pool": {
            "Complicated": "Unresolved boundaries with fluctuating emotional cycles.",
            "In a Relationship": "Highly committed; frequently seeking reassurance."
        },
        "contentment_distribution": {"Dissatisfied": 0.6, "Content": 0.3, "Happy": 0.1},
        "fashion_preferences": ["Trendy", "Bohemian", "Glamorous", "Edgy"],
        "tech_affinity": {"Beginner": 0.3, "Intermediate": 0.5, "Advanced": 0.2}
    }
}

def get_random_lifestyle_profile() -> Tuple[Dict[str, str], str, str]:
    """
    Generates a psychologically cohesive social and lifestyle profile.
    
    Returns:
        Tuple[Dict[str, str], str, str]: (Social Life Dict, Fashion Sense, Tech Level)
    """
    # 1. Select the root behavioral anchor
    archetype_name = random.choice(list(LIFESTYLE_ARCHETYPES.keys()))
    meta = LIFESTYLE_ARCHETYPES[archetype_name]
    
    # 2. Extract specific relationship variables
    rel_status = random.choice(list(meta["relationship_pool"].keys()))
    rel_desc = meta["relationship_pool"][rel_status]
    
    # 3. Pull weighted contentment distribution based on relationship archetype
    cont_choices = list(meta["contentment_distribution"].keys())
    cont_weights = list(meta["contentment_distribution"].values())
    contentment_status = random.choices(cont_choices, weights=cont_weights, k=1)[0]
    
    # Mapping static text values to match down-stream output expectations cleanly
    contentment_glossary = {
        "Happy": "Generally satisfied with current life path.",
        "Content": "Comfortable, steady, and stabilizing.",
        "Dissatisfied": "Actively feeling restricted or unfulfilled."
    }
    
    # 4. Generate social payload
    social_life = {
        "Relationship Status": f"{rel_status} ({rel_desc})",
        "Contentment Level": f"{contentment_status} ({contentment_glossary[contentment_status]})",
        "Family Dynamics": random.choice(meta["family_dynamics"])
    }
    
    # 5. Extract aligned structural aesthetics and technical proficiencies
    fashion_sense = random.choice(meta["fashion_preferences"])
    
    tech_choices = list(meta["tech_affinity"].keys())
    tech_weights = list(meta["tech_affinity"].values())
    tech_level = random.choices(tech_choices, weights=tech_weights, k=1)[0]
    
    return social_life, fashion_sense, tech_level
