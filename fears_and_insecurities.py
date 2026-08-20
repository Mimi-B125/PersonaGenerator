# fears_and_insecurities.py
import random
from typing import List, Dict, Any

# Structural pool mapping specific fears to their root Enneagram and Temperament triggers
FEARS_POOL = [
    {
        "text": "Impending sense of professional failure or being exposed as a fraud (Imposter Syndrome).",
        "triggers": {"enneagrams": ["3 - The Achiever", "1 - The Reformer"], "temperaments": ["Conscientious", "Neurotic"]}
    },
    {
        "text": "Intense social anxiety; terrified of being fundamentally judged or rejected in intimate settings.",
        "triggers": {"enneagrams": ["4 - The Individualist", "6 - The Loyalist"], "temperaments": ["Neurotic", "Introverted"]}
    },
    {
        "text": "Fear of losing control over their emotions or breaking down completely in a public space.",
        "triggers": {"enneagrams": ["8 - The Challenger", "1 - The Reformer"], "temperaments": ["Conscientious"]}
    },
    {
        "text": "Severe abandonment issues; aggressively pushing others away before they have the chance to leave.",
        "triggers": {"enneagrams": ["6 - The Loyalist", "2 - The Helper"], "temperaments": ["Neurotic"]}
    },
    {
        "text": "Fear of stagnation; terrified of wasting their creative potential or getting stuck in a routine.",
        "triggers": {"enneagrams": ["7 - The Enthusiast", "4 - The Individualist"], "temperaments": ["Extroverted"]}
    },
    {
        "text": "Anxiety about physical or mental vulnerability; deeply loathes having to rely on others for support.",
        "triggers": {"enneagrams": ["8 - The Challenger", "5 - The Investigator"], "temperaments": ["Introverted"]}
    },
    {
        "text": "Fear of conflict; will completely suppress their own boundaries to maintain external peace.",
        "triggers": {"enneagrams": ["9 - The Peacemaker"], "temperaments": ["Agreeable"]}
    },
    {
        "text": "Deep insecurity about their aesthetic appearance or how their body is perceived by others.",
        "triggers": {"enneagrams": ["4 - The Individualist", "3 - The Achiever"], "temperaments": ["Neurotic"]}
    },
    {
        "text": "Fear of true emotional intimacy; uses sarcasm as a defense mechanism to keep people at a distance.",
        "triggers": {"enneagrams": ["5 - The Investigator", "7 - The Enthusiast"], "temperaments": ["Introverted", "Neurotic"]}
    },
    {
        "text": "Anxiety about sudden financial instability or losing their baseline personal independence.",
        "triggers": {"enneagrams": ["6 - The Loyalist", "8 - The Challenger"], "temperaments": ["Conscientious"]}
    }
]

def get_random_fears(count: int = 2, personality: Dict[str, Any] = None) -> List[str]:
    """
    Extracts relevant psychological fears or insecurities.
    If personality context is provided, scores and selects matching fears dynamically.
    Otherwise, falls back to a weighted baseline random sample to protect compatibility.
    """
    if not personality:
        # Fallback tracking for total backward compatibility
        raw_list = [item["text"] for item in FEARS_POOL]
        return random.sample(raw_list, k=min(count, len(raw_list)))

    enneagram = personality.get("enneagram_type", "")
    temperament = personality.get("temperament", "")
    
    scored_fears = []
    for item in FEARS_POOL:
        score = 0.5  # Neutral baseline
        
        # Match against structural personality parameters
        if enneagram in item["triggers"].get("enneagrams", []):
            score += 2.0
        if temperament in item["triggers"].get("temperaments", []):
            score += 1.0
            
        scored_fears.append((score, item["text"]))
        
    # Sort descending by calculated structural score
    scored_fears.sort(key=lambda x: x[0], reverse=True)
    
    # Grab the top-scoring slice, shuffle to avoid exact duplicates across runs, and sample
    top_tier = [text for score, text in scored_fears[:count + 2]]
    random.shuffle(top_tier)
    
    return top_tier[:count]
