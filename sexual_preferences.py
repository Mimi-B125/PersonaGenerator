import random
from typing import List, Dict, Any

# 1. Merge your original KINK_DICT with the weighting logic
# We keep your exact lists but add metadata for the generator to use.
KINK_DATA = {
    "BDSM": {
        "subtypes": ["Bondage", "Discipline", "Dominance", "Submission", "Sadism", "Masochism", "Power Dynamics"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 0.8, "bisexual": 1.0},
        "enneagram_modifiers": {"8 - The Challenger": 1.5, "3 - The Achiever": 1.2}
    },
    "Chastity Play": {
        "subtypes": ["Chastity Cages", "'Keyholder' Dynamics", "Orgasm Denial", "Long-Term Lock-Up", "Tease and Denial", "Remote-Controlled Devices", "Cuckolding with Chastity"],
        "base_weights": {"heterosexual": 0.9, "lesbian": 0.7, "bisexual": 0.9},
        "enneagram_modifiers": {"2 - The Helper": 1.4, "9 - The Peacemaker": 1.3}
    },
    "Power Exchange": {
        "subtypes": ["Master/Slave Dynamics", "24/7 D/s Relationships", "Service Submission", "Protocol-Based Relationships", "Collaring Ceremonies", "Financial Domination (Findom)", "Obedience Training"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 0.8, "bisexual": 1.0},
        "enneagram_modifiers": {"8 - The Challenger": 1.5, "6 - The Loyalist": 1.3}
    },
    "Erotic Humiliation": {
        "subtypes": ["Verbal Degradation", "Public Embarrassment", "Cuckolding", "SPH (Small Penis Humiliation)", "Forced Feminization", "'Slut'-Shaming Roleplay", "Writing Lines as Punishment"],
        "base_weights": {"heterosexual": 0.8, "lesbian": 0.6, "bisexual": 0.8},
        "enneagram_modifiers": {"4 - The Individualist": 1.5, "7 - The Enthusiast": 1.2}
    },
    "Corner Time": {
        "subtypes": ["Disciplinary Punishment", "'Time-Out' Scenarios", "Psychological Control", "Standing in Silence", "Facing a Wall or Corner Naked", "'Thinking Time' Roleplay Punishment", "Physical Restrictions (e.g., Holding Something)"],
        "base_weights": {"heterosexual": 0.9, "lesbian": 0.7, "bisexual": 0.9},
        "enneagram_modifiers": {"8 - The Challenger": 1.4, "6 - The Loyalist": 1.3}
    },
    "Impact Play": {
        "subtypes": ["Spanking", "Whipping", "Flogging", "Caning", "Paddling", "Riding Crops", "Switching (Roles)"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 0.9, "bisexual": 1.0},
        "enneagram_modifiers": {"8 - The Challenger": 1.6, "3 - The Achiever": 1.2}
    },
    "Electrostimulation": {
        "subtypes": ["Violet Wand", "E-Stim Pads", "TENS Unit", "Erotic Shocks on Genitals", "Sensation Play with Electricity", "Remote-Controlled Shocks", "Edge Play with Safety Precautions"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 1.0, "bisexual": 1.0},
        "enneagram_modifiers": {"5 - The Investigator": 1.5, "7 - The Enthusiast": 1.3}
    },
    "Sensory Deprivation": {
        "subtypes": ["Blindfolds", "Earplugs/Headphones", "Hood Play", "Mummification", "Deprivation Tanks", "Gags (e.g., Ball Gags)", "Temperature Play (e.g., Ice or Heat)"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 1.0, "bisexual": 1.0},
        "enneagram_modifiers": {"4 - The Individualist": 1.5, "9 - The Peacemaker": 1.3}
    },
    "Rope Bondage": {
        "subtypes": ["Shibari", "Kinbaku", "Full Body Harnesses", "Suspension Bondage Techniques", "Decorative Rope Patterns on the Skin", "Partial Restraint Scenes (e.g., Hands Only)", "Rope Burn as a Sensation Play Element"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 1.0, "bisexual": 1.0},
        "enneagram_modifiers": {"4 - The Individualist": 1.6, "5 - The Investigator": 1.3}
    },
    "Corsetry/Tight-Lacing": {
        "subtypes": ["Waist Training", "Breath-Restricting Corsets", "Victorian Aesthetic Roleplay", "'Dollification' Through Corset Use", "'Tight-Lace Punishment' Dynamics in D/s Play", "Corset Fetishism for Aesthetic Appeal", "'Training' to Endure Tight Lacing Over Time"],
        "base_weights": {"heterosexual": 0.9, "lesbian": 0.8, "bisexual": 0.9},
        "enneagram_modifiers": {"4 - The Individualist": 1.5, "3 - The Achiever": 1.2}
    },
    "Fisting": {
        "subtypes": ["Anal Fisting", "Vaginal Fisting with Proper Technique", "Stretching Toys for Preparation", "'Slow and Gentle' Fisting Dynamics for Safety", "'Punch Fisting' for Advanced Players (Risk-Aware)", "'Double Fisting' Scenarios (Advanced)", "'Aftercare Focus' Due to Intensity of Play"],
        "base_weights": {"heterosexual": 0.8, "lesbian": 0.7, "bisexual": 0.8},
        "enneagram_modifiers": {"8 - The Challenger": 1.4, "5 - The Investigator": 1.3}
    },
    "Objectification": {
        "subtypes": ["Sex Doll Roleplay", "'Furniture Objectification' (e.g., Human Chair/Table)", "'Pet Objectification' (e.g., Being Treated Like an Animal)", "'Dehumanization' Scenarios in D/s Play", "'Mannequin Roleplay'", "'Human Ashtray' Scenarios", "'Being Used as a Tool or Prop in Scenes"],
        "base_weights": {"heterosexual": 0.9, "lesbian": 0.8, "bisexual": 0.9},
        "enneagram_modifiers": {"4 - The Individualist": 1.6, "7 - The Enthusiast": 1.4}
    },
    "Primal Fear Play": {
        "subtypes": ["Chase-and-Capture Dynamics", "'Hunted Prey' Scenarios", "Growling/Snarling with Intent to Intimidate", "Use of Natural Settings for Scenes (e.g., Forests)", "Non-Verbal Communication During Fear Play", "Scratching/Biting to Simulate Predatory Behavior", "'Fear-Induced Adrenaline Rush as a Turn-On'"],
        "base_weights": {"heterosexual": 1.0, "lesbian": 1.0, "bisexual": 1.0},
        "enneagram_modifiers": {"8 - The Challenger": 1.5, "7 - The Enthusiast": 1.4}
    }
}

def get_weighted_sexual_preferences(
    orientation: str, 
    personality: Dict[str, Any], 
    count: int = 2
) -> List[Dict[str, Any]]:
    """
    Calculates scores for all categories in KINK_DATA based on orientation and Enneagram.
    Selects the top 'count' categories and picks a random subtype from each.
    """
    scored_categories = []

    for category_name, data in KINK_DATA.items():
        # Calculate Score
        base_weight = data["base_weights"].get(orientation.lower(), 1.0)
        enneagram_type = personality.get("enneagram_type", "")
        modifier = data["enneagram_modifiers"].get(enneagram_type, 1.0)
        
        final_score = base_weight * modifier
        
        scored_categories.append({
            "category": category_name,
            "subtypes": data["subtypes"],
            "score": final_score
        })

    # Sort by score descending and pick top results
    scored_categories.sort(key=lambda x: x["score"], reverse=True)
    top_selections = scored_categories[:count]

    results = []
    for item in top_selections:
        # Pick one random subtype from the chosen category's list
        chosen_subtype = random.choice(item["subtypes"])
        
        results.append({
            "preference": item["category"],
            "description": chosen_subtype,
            "intensity": random.randint(1, 10),
            "frequency": random.choice(["Rarely", "Occasionally", "Frequently", "Constantly"])
        })

    return results
