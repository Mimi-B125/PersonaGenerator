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

# fears_and_insecurities.py (Append to the bottom of your existing file)

def get_body_perception_narrative(personality: Dict[str, Any], physical_traits: Dict[str, str]) -> str:
    """
    Evaluates how the persona internalizes their physical metrics based on 
    their Enneagram archetype and personality traits.
    """
    enneagram = personality.get("enneagram_type", "")
    metrics = physical_traits.get("anatomical_metrics", "").lower()
    
    # Identify the size tier from the text strings we built earlier
    if "below_average" in metrics or "compact" in metrics or "petite" in metrics:
        size_tier = "below"
    elif "above_average" in metrics or "substantial" in metrics or "prominent" in metrics:
        size_tier = "above"
    else:
        size_tier = "average"

    # Core narrative engine parsing the intersection of size and personality
    if size_tier == "below":
        if "3 - The Achiever" in enneagram:
            return "Deeply internalized as a hidden failure; feeds intense performance anxiety and a constant fear of exposure."
        elif "8 - The Challenger" in enneagram:
            return "Compensates with fierce, unapologetic dominance and aggressive physical control; refuses to let it become a vulnerability."
        elif "4 - The Individualist" in enneagram:
            return "Feeds a melancholic sense of being fundamentally flawed; directly links into their erotic humiliation or submission kinks."
        elif "9 - The Peacemaker" in enneagram:
            return "Quietly resigned and highly self-conscious; tends to favor safe, low-pressure chastity play to avoid performance demands."
        else:
            return "Triggers a persistent undercurrent of insecurity, making them highly reliant on heavy emotional intimacy to feel secure."

    elif size_tier == "above":
        if "3 - The Achiever" in enneagram or "8 - The Challenger" in enneagram:
            return "A source of quiet, immense confidence; fuels an assertive, commanding presence both in professional spaces and intimate scenes."
        elif "5 - The Investigator" in enneagram:
            return "Viewed detachedly as a clinical asset; they find it amusing but prefer precise, calculated execution over raw physical scale."
        elif "6 - The Loyalist" in enneagram:
            return "Anxious about overwhelming partners; paradoxically worries about causing discomfort or failing to meet expectations."
        else:
            return "Comfortable and confident, naturally leaning into high-intensity impact play or primal dynamics without hesitation."

    else: # Average / Proportional
        if "1 - The Reformer" in enneagram:
            return "Completely content with their standard proportions, viewing predictability and structural symmetry as ideal."
        elif "7 - The Enthusiast" in enneagram:
            return "Hardly gives it a second thought; far more focused on chasing varied sensations and spontaneous fun than overanalyzing dimensions."
        else:
            return "Balanced and secure; physical expectations remain secondary to their psychological or protocol-based relationship needs."
