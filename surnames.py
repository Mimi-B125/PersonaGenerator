import random

SURNAMES = [
    "Black", "Vance", "Thorne", "Mercer", "Sinclair", "Sterling", 
    "Devon", "Garrick", "Winter", "Hawthorne", "Cross", "St. Clair",
    "Miller", "Blackwood", "Valentin", "Russo", "Kingsley", "Hale"
]

def get_random_surname() -> str:
    """
    Returns a randomized surname for profile isolation.
    """
    return random.choice(SURNAMES)
