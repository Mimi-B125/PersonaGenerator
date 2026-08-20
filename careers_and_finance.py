import random
from typing import List, Tuple

OCCUPATIONS = [
    "Teacher", "Nurse", "Engineer", "Stay-at-home parent", "Chef", 
    "Writer", "Artist", "Designer", "Barista", "Software Developer", 
    "Paralegal", "Accountant", "Librarian", "Project Manager"
]

INCOME_LEVELS = ["low-income", "middle-class", "wealthy"]

EDUCATION_TIERS = ["High School Diploma", "Bachelor's Degree", "Master's Degree", "Ph.D."]

def get_random_career_profile() -> Tuple[str, str, str]:
    """Returns a randomized: (Occupation, Income Level, Education Tier)"""
    return (
        random.choice(OCCUPATIONS),
        random.choice(INCOME_LEVELS),
        random.choice(EDUCATION_TIERS)
    )
