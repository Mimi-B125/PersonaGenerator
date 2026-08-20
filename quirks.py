# quirks.py
import random
from typing import List, Dict, Any

# Visceral behavioral regressions, social neuroses, and private compulsions
QUIRKS_POOL = [
    {
        "text": "Prone to wetting the bed if they drink heavily or slip into deep exhaustion; keeps a discrete waterproof protector on their mattress.",
        "triggers": {"enneagrams": ["9 - The Peacemaker", "7 - The Enthusiast"], "emotions": ["Anxious", "Irritable"]}
    },
    {
        "text": "Secretly reverts to sucking their thumb or holding a specific textile sample when completely alone and spiraling into high anxiety.",
        "triggers": {"enneagrams": ["6 - The Loyalist", "2 - The Helper"], "emotions": ["Anxious", "Empathetic"]}
    },
    {
        "text": "Suffers from severe paruresis (shy bladder); completely unable to use public restrooms unless the space is entirely empty.",
        "triggers": {"enneagrams": ["1 - The Reformer", "5 - The Investigator"], "emotions": ["Anxious", "Reserved"]}
    },
    {
        "text": "Collects their trimmed fingernails in a small glass jar hidden at the back of their vanity cabinet.",
        "triggers": {"enneagrams": ["5 - The Investigator"], "emotions": ["Calm", "Reserved"]}
    },
    {
        "text": "Compulsively checks that door locks are secure and appliance dials are turned off exactly four times before they can sleep.",
        "triggers": {"enneagrams": ["1 - The Reformer", "6 - The Loyalist"], "emotions": ["Anxious"]}
    },
    {
        "text": "Cannot fall asleep unless they are wearing tight, restrictive clothing or a heavy, constricting body harness.",
        "triggers": {"enneagrams": ["4 - The Individualist", "8 - The Challenger"], "emotions": ["Neurotic", "Anxious"]}
    },
    {
        "text": "Involuntarily pulls out strands of their own hair (trichotillomania) when processing severe professional or emotional pressure.",
        "triggers": {"enneagrams": ["3 - The Achiever", "1 - The Reformer"], "emotions": ["Irritable", "Anxious"]}
    },
    {
        "text": "Pathologically hoards expired over-the-counter medications and visual medical supplies out of an irrational fear of scarcity.",
        "triggers": {"enneagrams": ["6 - The Loyalist", "5 - The Investigator"], "emotions": ["Anxious"]}
    },
    {
        "text": "Refuses to let anyone touch their neck or collarbones; will instantly freeze or aggressively snap if their perimeter is breached.",
        "triggers": {"enneagrams": ["8 - The Challenger", "4 - The Individualist"], "emotions": ["Irritable", "Neurotic"]}
    }
]

def get_contextual_quirk(personality: Dict[str, Any], fashion_sense: str) -> str:
    """
    Scores and returns a distinct, high-fidelity psychological quirk or neurosis 
    by evaluating Enneagram types and underlying emotional traits.
    """
    enneagram = personality.get("enneagram_type", "")
    emotional_trait = personality.get("emotional_traits", "")
    social_behavior = personality.get("social_behavior", "")
    
    scored_quirks = []
    for item in QUIRKS_POOL:
        score = 0.5  # Base line weight
        
        # Match primary Enneagram hooks
        if enneagram in item["triggers"].get("enneagrams", []):
            score += 2.0
            
        # Match emotional background parameters
        if emotional_trait in item["triggers"].get("emotions", []):
            score += 1.0
        if social_behavior in item["triggers"].get("emotions", []):
            score += 1.0
            
        scored_quirks.append((score, item["text"]))
        
    # Sort descending by calculated compatibility
    scored_quirks.sort(key=lambda x: x[0], reverse=True)
    
    # Extract top 3 scoring variants, shuffle for volatility, and pull the winner
    top_tier = [text for score, text in scored_quirks[:3]]
    random.shuffle(top_tier)
    
    return top_tier[0]
