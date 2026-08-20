from faker import Faker
import logging

# Initialize Faker instance globally for better performance
# This creates a singleton-like behavior for the generator
_fake = Faker()

def get_random_surname() -> str:
    """
    Returns a randomized, realistic surname using the Faker library.
    
    Returns:
        str: A randomly generated last name.
    """
    try:
        return _fake.last_name()
    except Exception as e:
        # Fallback or error logging in case of unexpected issues
        logging.error(f"Error generating surname: {e}")
        return "Unknown"

# Example usage for testing purposes
#if __name__ == "__main__":
#    print(f"Generated Surname: {get_random_surname()}")
