# careers_and_finance.py
import random
from typing import Tuple, Dict, Any

# Structural Definition of Occupations mapped to realistic financial and educational boundaries
OCCUPATION_MATRIX: Dict[str, Dict[str, Any]] = {
    "Teacher": {
        "education_pool": ["Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.2, "middle-class": 0.8, "wealthy": 0.0}
    },
    "Nurse": {
        "education_pool": ["Associate Degree in Nursing", "Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.0, "middle-class": 0.9, "wealthy": 0.1}
    },
    "Engineer": {
        "education_pool": ["Bachelor's Degree", "Master's Degree", "Ph.D."],
        "income_weights": {"low-income": 0.0, "middle-class": 0.6, "wealthy": 0.4}
    },
    "Stay-at-home parent": {
        "education_pool": ["High School Diploma", "Bachelor's Degree", "Master's Degree", "Ph.D."],
        "income_weights": {"low-income": 0.4, "middle-class": 0.5, "wealthy": 0.1}
    },
    "Chef": {
        "education_pool": ["High School Diploma", "Culinary Arts Degree", "Bachelor's Degree"],
        "income_weights": {"low-income": 0.2, "middle-class": 0.7, "wealthy": 0.1}
    },
    "Writer": {
        "education_pool": ["High School Diploma", "Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.5, "middle-class": 0.4, "wealthy": 0.1}
    },
    "Artist": {
        "education_pool": ["High School Diploma", "Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.6, "middle-class": 0.3, "wealthy": 0.1}
    },
    "Designer": {
        "education_pool": ["Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.1, "middle-class": 0.7, "wealthy": 0.2}
    },
    "Barista": {
        "education_pool": ["High School Diploma", "Some College", "Bachelor's Degree"],
        "income_weights": {"low-income": 0.8, "middle-class": 0.2, "wealthy": 0.0}
    },
    "Software Developer": {
        "education_pool": ["Self-Taught / Bootcamp", "Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.0, "middle-class": 0.5, "wealthy": 0.5}
    },
    "Paralegal": {
        "education_pool": ["Associate Degree", "Bachelor's Degree"],
        "income_weights": {"low-income": 0.1, "middle-class": 0.8, "wealthy": 0.0}
    },
    "Accountant": {
        "education_pool": ["Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.0, "middle-class": 0.8, "wealthy": 0.2}
    },
    "Librarian": {
        "education_pool": ["Master's Degree"],  # Standard industry requirement (MLIS)
        "income_weights": {"low-income": 0.2, "middle-class": 0.8, "wealthy": 0.0}
    },
    "Project Manager": {
        "education_pool": ["Bachelor's Degree", "Master's Degree"],
        "income_weights": {"low-income": 0.0, "middle-class": 0.7, "wealthy": 0.3}
    }
}

def get_random_career_profile() -> Tuple[str, str, str]:
    """
    Generates a coherent, logically linked career profile.
    Returns: (Occupation, Income Level, Education Tier)
    """
    # 1. Select the core occupation anchor
    occupation = random.choice(list(OCCUPATION_MATRIX.keys()))
    meta = OCCUPATION_MATRIX[occupation]
    
    # 2. Select an industry-appropriate education tier
    education = random.choice(meta["education_pool"])
    
    # 3. Extract the weighted choices for income distribution
    income_choices = list(meta["income_weights"].keys())
    income_weights = list(meta["income_weights"].values())
    
    # 4. Sample income using the structural probabilities
    income_level = random.choices(income_choices, weights=income_weights, k=1)[0]
    
    return occupation, income_level, education
