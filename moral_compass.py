# moral_compass.py
import random
from typing import Dict, List, Any

# Structural pool linking moral outlooks to Enneagram and Temperament anchors
MORAL_POOL = [
    {
        "framework": "Utilitarian",
        "description": "Calculates morality based on maximizing overall well-being and outcome efficiency. Strongly focused on results over rigid rules.",
        "triggers": {"enneagrams": ["3 - The Achiever", "8 - The Challenger"], "temperaments": ["Conscientious"]}
    },
    {
        "framework": "Deontological",
        "description": "Bound strictly by duty, absolute principles, and universal rules. Right actions are defined by an unwavering moral code, regardless of consequences.",
        "triggers": {"enneagrams": ["1 - The Reformer", "6 - The Loyalist"], "temperaments": ["Conscientious"]}
    },
    {
        "framework": "Virtue Ethics",
        "description": "Centers on internal character, integrity, and personal excellence. Asks 'who should I be' rather than 'what rule should I follow' in a situation.",
        "triggers": {"enneagrams": ["1 - The Reformer", "2 - The Helper", "4 - The Individualist"], "temperaments": ["Agreeable"]}
    },
    {
        "framework": "Pragmatic",
        "description": "Views morality as an evolving toolkit that adapts to real-world experience. Principles are tested by practical application, emphasizing what works.",
        "triggers": {"enneagrams": ["7 - The Enthusiast", "5 - The Investigator", "9 - The Peacemaker"], "temperaments": ["Extroverted"]}
    }
]

def get_contextual_moral_compass(personality: Dict[str, Any]) -> str:
    """
    Scores and returns an ethical framework and description 
    aligned with the persona's internal psychological makeup.
    """
    enneagram = personality.get("enneagram_type", "")
    temperament = personality.get("temperament", "")
    
    scored_frameworks = []
    for item in MORAL_POOL:
        score = 0.5  # Neutral baseline
        
        if enneagram in item["triggers"].get("enneagrams", []):
            score += 2.0
        if temperament in item["triggers"].get("temperaments", []):
            score += 1.0
            
        full_text = f"{item['framework']} — {item['description']}"
        scored_frameworks.append((score, full_text))
        
    # Sort descending by compatibility score
    scored_frameworks.sort(key=lambda x: x[0], reverse=True)
    
    # Extract top matching tier, shuffle for variety, and return the winner
    top_tier = [text for score, text in scored_frameworks[:2]]
    return random.choice(top_tier)
