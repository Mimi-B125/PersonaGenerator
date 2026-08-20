import random
from typing import Dict, Tuple

RELATIONSHIP_STATUSES = [
    {"Single": "Not in a relationship."}, 
    {"Complicated": "Unresolved boundaries."}, 
    {"In a Relationship": "Committed to a partner."},
    {"Friends with Benefits": "Sexual interactions without commitment."}
]

CONTENTMENT_LEVELS = [
    {"Happy": "Generally satisfied."}, 
    {"Content": "Comfortable."}, 
    {"Dissatisfied": "Unhappy with certain aspects."}
]

FAMILY_DYNAMICS = ['Close-knit Family', 'High-conflict Family', 'Absent Caregiver Dynamic', 'Secretive Family']

FASHION_SENSES = ["Casual", "Trendy", "Minimalist", "Vintage", "Bohemian", "Preppy", "Edgy", "Glamorous"]

def get_random_lifestyle_profile() -> Tuple[Dict[str, str], str, str]:
    """Returns a randomized: (Social Life Dict, Fashion Sense, Tech Level)"""
    chosen_status = random.choice(RELATIONSHIP_STATUSES)
    status_key = next(iter(chosen_status.keys()))
    status_desc = chosen_status[status_key]

    chosen_content = random.choice(CONTENTMENT_LEVELS)
    content_key = next(iter(chosen_content.keys()))
    content_desc = chosen_content[content_key]

    social_life = {
        'Relationship Status': f"{status_key} ({status_desc})",
        'Contentment Level': f"{content_key} ({content_desc})",
        'Family Dynamics': random.choice(FAMILY_DYNAMICS)
    }
    
    tech_level = random.choice(['Beginner', 'Intermediate', 'Advanced', 'Expert'])
    
    return social_life, random.choice(FASHION_SENSES), tech_level
