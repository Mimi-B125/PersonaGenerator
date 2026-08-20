from faker import Faker
from typing import List, Dict

# Initialize Faker once at the module level for performance
_fake = Faker()

def get_random_name_by_gender(gender: str) -> str:
    """
    Returns a random name based on the specified gender key string 
    using the Faker library.
    """
    # Normalize mapping connections to match your blueprint keys
    clean_gender = gender.lower().strip()
    
    if clean_gender in ["female", "woman"]:
        return _fake.first_name_female()
    elif clean_gender in ["male", "man"]:
        return _fake.first_name_male()
    elif clean_gender == "non-binary":
        # Faker doesn't have a specific non-binary method, 
        # so we use the standard first_name() which is gender-neutral/mixed.
        return _fake.first_name()
    else:
        # Fallback for safety if an unexpected string is passed
        return _fake.first_name()

def get_all_names() -> Dict[str, List[str]]:
    """
    Note: Since Faker generates names dynamically, this function 
    is now deprecated as there is no longer a static list.
    """
    return {"info": "Faker generates names dynamically; no static list available."}
