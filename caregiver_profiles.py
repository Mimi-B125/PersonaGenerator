# caregiver_profiles.py
import random
from typing import Dict, Any, List

# Core behavioral templates blending caregiving archetypes with raw prompt execution hooks
CAREGIVER_MATRIX = [
    {
        "style": "Authoritarian / Firm",
        "description": "Demands strict adherence to rules and established protocols. Uses clear boundaries, precise expectations, and immediate correction to enforce structure.",
        "triggers": {"enneagrams": ["8 - The Challenger", "1 - The Reformer"], "morals": ["Deontological", "Virtue Ethics"]}
    },
    {
        "style": "Nurturing / Empathetic",
        "description": "Prioritizes emotional warmth, deep safety, and psychological reassurance. Focuses heavily on aftercare and active listening, softening boundaries to accommodate needs.",
        "triggers": {"enneagrams": ["2 - The Helper", "9 - The Peacemaker"], "morals": ["Virtue Ethics", "Pragmatic"]}
    },
    {
        "style": "Tough Love / No-Nonsense",
        "description": "Highly results-oriented and fiercely practical. Challenges weakness directly to force self-reliance; uses calculated discomfort as a primary optimization tool.",
        "triggers": {"enneagrams": ["3 - The Achiever", "8 - The Challenger"], "morals": ["Utilitarian", "Pragmatic"]}
    },
    {
        "style": "Playful / Engaging",
        "description": "Balances control with dynamic, high-energy interactions. Uses teasing, spontaneous games, and creative framing to maintain engagement while keeping underlying authority intact.",
        "triggers": {"enneagrams": ["7 - The Enthusiast"], "morals": ["Pragmatic"]}
    },
    {
        "style": "Overprotective / Cautious",
        "description": "Hyper-focused on risk management and safety protocols. Constantly monitors boundaries and vital signs, keeping actions tightly restricted to prevent distress.",
        "triggers": {"enneagrams": ["6 - The Loyalist"], "morals": ["Deontological"]}
    },
    {
        "style": "Hands-Off / Detached",
        "description": "Maintains an analytical, highly objective distance. Operates via cold clinical logic, leaving the partner to navigate protocols independently until a safety threshold is breached.",
        "triggers": {"enneagrams": ["5 - The Investigator"], "morals": ["Utilitarian", "Pragmatic"]}
    }
]

def get_contextual_caregiver_style(personality: Dict[str, Any], moral_compass: str) -> str:
    """
    Scores and returns a psychologically consistent caregiving profile 
    and description based on the persona's Enneagram and moral compass alignment.
    """
    enneagram = personality.get("enneagram_type", "")
    
    scored_styles = []
    for item in CAREGIVER_MATRIX:
        score = 0.5  # Neutral baseline
        
        if enneagram in item["triggers"].get("enneagrams", []):
            score += 2.0
        if moral_compass in item["triggers"].get("morals", []):
            score += 1.0
            
        full_text = f"{item['style']} — {item['description']}"
        scored_styles.append((score, full_text))
        
    # Sort by calculated compatibility weight descending
    scored_styles.sort(key=lambda x: x[0], reverse=True)
    
    # Grab the best matching tiers, shuffle to preserve variety, and pick the winner
    top_tier = [text for score, text in scored_styles[:2]]
    return random.choice(top_tier)
