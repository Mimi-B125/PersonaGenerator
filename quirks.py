"""
quirks.py

Generates deeply grounded, visceral character quirks, behavioral regressions, 
and private compulsions. Scores candidate traits using upstream foundational anchors 
(Enneagram, Temperament, Age, Sex, Health, and Lifestyle).
"""

import random
from typing import Dict, List, Any


# -----------------------------------------------------------------------------
# QUIRKS & COMPULSIONS DATA POOL
# -----------------------------------------------------------------------------
QUIRKS_POOL: List[Dict[str, Any]] = [
    {
        "text": "Tends to wet the bed during periods of severe exhaustion or heavy drinking; keeps a discreet waterproof protector tucked under their bottom sheet.",
        "triggers": {
            "enneagrams": ["9", "7"],
            "temperaments": ["Neurotic", "Introverted"],
            "emotional_traits": ["Anxious", "Irritable"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Quietly reverts to sucking their thumb or rubbing a specific soft textile sample when entirely alone and spiraling into acute anxiety.",
        "triggers": {
            "enneagrams": ["6", "2", "9"],
            "temperaments": ["Introverted", "Agreeable"],
            "emotional_traits": ["Anxious", "Empathetic"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Deals with a severe shy bladder (paruresis) and usually has to wait until a public restroom is completely empty before they can void.",
        "triggers": {
            "enneagrams": ["1", "5", "6"],
            "temperaments": ["Introverted", "Conscientious"],
            "emotional_traits": ["Anxious", "Reserved"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Saves their trimmed fingernails in a small glass jar hidden away behind medicine bottles in their bathroom cabinet.",
        "triggers": {
            "enneagrams": ["5", "1"],
            "temperaments": ["Introverted", "Conscientious"],
            "emotional_traits": ["Calm", "Reserved"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Compulsively checks that every exterior door lock and stove dial is secured exactly four times before going to sleep.",
        "triggers": {
            "enneagrams": ["1", "6"],
            "temperaments": ["Conscientious", "Neurotic"],
            "emotional_traits": ["Anxious", "Irritable"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Cannot fall asleep unless wearing tight, restrictive sleepwear or wrapped in a dense compression body harness.",
        "triggers": {
            "enneagrams": ["4", "8"],
            "temperaments": ["Neurotic", "Introverted"],
            "emotional_traits": ["Anxious", "Neurotic"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Absentmindedly plucks out individual strands of hair (trichotillomania) when working under intense pressure or social evaluation.",
        "triggers": {
            "enneagrams": ["3", "1", "6"],
            "temperaments": ["Conscientious", "Neurotic"],
            "emotional_traits": ["Anxious", "Irritable"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Pathologically hoards expired over-the-counter medications and bandages out of an irrational dread of sudden resource scarcity.",
        "triggers": {
            "enneagrams": ["6", "5"],
            "temperaments": ["Introverted", "Conscientious"],
            "emotional_traits": ["Anxious", "Reserved"],
            "min_age": 30,
            "max_age": 68
        }
    },
    {
        "text": "Flinches violently or pulls away if anyone moves toward their neck or collarbone area without explicit warning.",
        "triggers": {
            "enneagrams": ["8", "4"],
            "temperaments": ["Neurotic", "Extroverted"],
            "emotional_traits": ["Irritable", "Anxious"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Counts every stair step out loud in a low whisper whenever ascending or descending a staircase alone.",
        "triggers": {
            "enneagrams": ["1", "5", "6"],
            "temperaments": ["Conscientious", "Introverted"],
            "emotional_traits": ["Calm", "Anxious"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Bites the skin around their cuticles until they bleed whenever trapped in prolonged, idle social conversation.",
        "triggers": {
            "enneagrams": ["3", "7", "9"],
            "temperaments": ["Neurotic", "Introverted"],
            "emotional_traits": ["Anxious", "Irritable"],
            "min_age": 22,
            "max_age": 68
        }
    },
    {
        "text": "Refuses to eat food if different items on the plate touch each other; will use a separate side plate if forced.",
        "triggers": {
            "enneagrams": ["1", "5"],
            "temperaments": ["Conscientious"],
            "emotional_traits": ["Reserved", "Irritable"],
            "min_age": 22,
            "max_age": 68
        }
    }
]


# -----------------------------------------------------------------------------
# CASCADING WEIGHTED SELECTION ENGINE
# -----------------------------------------------------------------------------
def get_contextual_quirk(
    personality: Dict[str, Any],
    health_data: Dict[str, str],
    age: int,
    biological_sex: str
) -> Dict[str, str]:
    """
    Evaluates upstream foundational anchors to calculate dynamic scores for
    behavioral quirks, returning a formatted key-value pair dictionary.

    Args:
        personality: Dict containing enneagram_type, temperament, emotional_traits, social_behavior.
        health_data: Dict generated by health_profiles.py.
        age: Biological age integer.
        biological_sex: Biological sex string ("male" or "female").

    Returns:
        Dict[str, str]: Single-entry key-value string dictionary.
    """
    enneagram = str(personality.get("enneagram_type", "5")).strip().split(" ")[0]
    temperament = str(personality.get("temperament", "Introverted")).strip()
    emotional_trait = str(personality.get("emotional_traits", "")).strip()
    social_behavior = str(personality.get("social_behavior", "")).strip()
    mental_baseline = health_data.get("Mental & Emotional Baseline", "")

    scored_quirks: List[tuple] = []

    for item in QUIRKS_POOL:
        triggers = item["triggers"]
        score = 1.0

        # Age boundaries check
        if not (triggers["min_age"] <= age <= triggers["max_age"]):
            continue

        # Enneagram Match
        if enneagram in triggers["enneagrams"]:
            score += 2.5

        # Temperament Match
        if temperament in triggers["temperaments"]:
            score += 1.5

        # Emotional Traits Match
        if emotional_trait in triggers["emotional_traits"]:
            score += 1.25

        # Social Behavior Match
        if social_behavior in triggers["emotional_traits"]:
            score += 1.0

        # Cross-reference with Health Profile Mental Baseline
        if "burnout" in mental_baseline.lower() or "anxiety" in mental_baseline.lower():
            if "Anxious" in triggers["emotional_traits"] or "Neurotic" in triggers["temperaments"]:
                score += 1.5

        # Random variance factor (0.8 - 1.2) to ensure variety across generations
        score *= random.uniform(0.8, 1.2)

        scored_quirks.append((score, item["text"]))

    # Sort descending by calculated compatibility
    scored_quirks.sort(key=lambda x: x[0], reverse=True)

    # Select top 3 candidates and pull a winner
    top_candidates = [text for score, text in scored_quirks[:3]]
    selected_quirk = random.choice(top_candidates) if top_candidates else QUIRKS_POOL[0]["text"]

    return {
        "Private Quirks & Compulsions": selected_quirk
    }