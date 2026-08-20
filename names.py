import random
from typing import List, Dict

# Complete gender-correlated dictionary mapping 
NAMES_BY_GENDER: Dict[str, List[str]] = {
    "man": [
        "Liam", "Noah", "Oliver", "Elijah", "James",
        "William", "Benjamin", "Lucas", "Henry", "Alexander",
        "Mason", "Ethan", "Michael", "Daniel", "Jacob",
        "Logan", "Jackson", "Sebastian", "Jack", "Aiden",
        "Owen", "Samuel", "Matthew", "Joseph", "Levi",
        "David", "John", "Wyatt", "Carter", "Julian",
        "Thomas", "Nathan", "Caleb", "Christopher", "Joshua",
        "Andrew", "Ryan", "Isaac", "Adam", "Nathaniel"
    ],
    "woman": [
        "Olivia", "Charlotte", "Amelia", "Sophia", "Mia",
        "Penelope", "Abigail", "Ella", "Hazel", "Nora",
        "Layla", "Lily", "Aurora", "Zoe", "Stella",
        "Ivy", "Victoria", "Emilia", "Naomi", "Hannah",
        "Scarlett", "Grace", "Chloe", "Isabella", "Evelyn",
        "Aria", "Ellie", "Madison", "Avery", "Sofia",
        "Camila", "Harper", "Luna", "Paisley", "Savannah",
        "Willow", "Brooklyn", "Claire", "Elena", "Autumn",
        "Violet", "Lucy", "Ruby", "Eva", "Alice",
        "Aubrey", "Bella", "Sadie", "Mila", "Delilah",
        "Caroline", "Anna", "Natalie", "Gabriella", "Leah",
        "Isla", "Eliza", "Jade", "Maya", "Juliet",
        "Faith", "Rose", "Lydia", "Mariah", "Josephine", 
        "Margaret", "Clara", "Phoebe", "Eleanor", "Genevieve",
        "Catherine", "Audrey", "Vivian", "Madeline", "Sienna",
        "Everly", "Quinn", "Adelaide"
    ],
    "non-binary": [
        "Taylor", "Jordan", "Alex", "Casey", "Morgan",
        "Riley", "Skyler", "Quinn", "Avery", "Rowan"
    ]
}

def get_random_name_by_gender(gender: str) -> str:
    """
    Returns a random name based on the specified gender key string.
    """
    # Normalize mapping connections
    clean_gender = gender.lower().strip()
    if clean_gender == "female":
        clean_gender = "woman"
    elif clean_gender == "male":
        clean_gender = "man"

    if clean_gender not in NAMES_BY_GENDER:
        raise ValueError(f"Invalid gender '{gender}'. Must be 'man', 'woman', or 'non-binary'.")
    
    return random.choice(NAMES_BY_GENDER[clean_gender])

def get_all_names() -> Dict[str, List[str]]:
    """
    Returns the complete structured names dictionary catalog.
    """
    return NAMES_BY_GENDER
