"""
sexual_preferences.py

Generates weighted sexual preferences, kink profiles, intensity scales, and 
dynamic orientations tailored for uncensored local LLM character grounding.
Calculates weights using upstream anchors: Enneagram, Temperament, Age, Sex, and Orientation.

===============================================================================
DEVELOPER GUIDE: EXTENDING KINKS & SUBTYPES
===============================================================================

1. ADDING SUBTYPES TO AN EXISTING CATEGORY:
   - Locate the target category key in `KINK_DICT`.
   - Append your new subtype string directly to the category's list.
   Example:
       "BDSM": [
           "Bondage", "Discipline", ..., "Your New Subtype Here"
       ]

2. ADDING A BRAND NEW KINK CATEGORY:
   - Add a new key-value pair to `KINK_DICT` with a descriptive category title 
     and a list of string subtypes.
   Example:
       "Wax Play": [
           "Low-Temperature Soy Wax",
           "Dripping Sensation Play",
           "Temperature Contrast Scenes"
       ]

3. (OPTIONAL) TUNING ENNEAGRAM & TEMPERAMENT WEIGHTS:
   - If you added a new category and want specific personality types to favor it:
     a. Go to `ENNEAGRAM_WEIGHTS` and add the category key under the desired 
        type string ("1" through "9") with a float multiplier (e.g., 1.4).
     b. Go to `TEMPERAMENT_WEIGHTS` and add the category key under the desired 
        temperament string ("neurotic", "extroverted", etc.) with a multiplier.
   - NOTE: If you skip step 3, the engine automatically assigns a baseline 
     multiplier of 1.0 to your new category and applies organic random variance, 
     so it will still be selected seamlessly without throwing errors.

4. RETURN SCHEMA CONTRACT:
   - Function MUST return `Dict[str, str]`.
   - Keys act as Markdown headers/labels; values act as prompt grounding tokens.
===============================================================================
"""

import random
from typing import Dict, List, Any

KINK_DICT: Dict[str, List[str]] = {
    "BDSM": [
        "Bondage", "Discipline", "Dominance", "Submission", 
        "Sadism", "Masochism", "Power Dynamics"
    ],
    "Chastity Play": [
        "Chastity Cages", "'Keyholder' Dynamics", "Orgasm Denial", 
        "Long-Term Lock-Up", "Tease and Denial", "Remote-Controlled Devices", 
        "Cuckolding with Chastity"
    ],
    "Power Exchange": [
        "Master/Slave Dynamics", "24/7 D/s Relationships", "Service Submission", 
        "Protocol-Based Relationships", "Collaring Ceremonies", 
        "Financial Domination (Findom)", "Obedience Training"
    ],
    "Erotic Humiliation": [
        "Verbal Degradation", "Public Embarrassment", "Cuckolding", 
        "SPH (Small Penis Humiliation)", "Forced Feminization", 
        "'Slut'-Shaming Roleplay", "Writing Lines as Punishment"
    ],
    "Corner Time": [
        "Disciplinary Punishment", "'Time-Out' Scenarios", "Psychological Control", 
        "Standing in Silence", "Facing a Wall or Corner Naked", 
        "'Thinking Time' Roleplay Punishment", "Physical Restrictions"
    ],
    "Impact Play": [
        "Spanking", "Whipping", "Flogging", "Caning", 
        "Paddling", "Riding Crops", "Switching (Roles)"
    ],
    "Electrostimulation": [
        "Violet Wand", "E-Stim Pads", "TENS Unit", "Erotic Shocks on Genitals", 
        "Sensation Play with Electricity", "Remote-Controlled Shocks", 
        "Edge Play with Safety Precautions"
    ],
    "Sensory Deprivation": [
        "Blindfolds", "Earplugs/Headphones", "Hood Play", "Mummification", 
        "Deprivation Tanks", "Gags (e.g., Ball Gags)", 
        "Temperature Play (Ice or Heat)"
    ],
    "Breath Play": [
        "Choking", "Bag Over Head", "Hand Over Mouth", "Plastic Wrap Play", 
        "Controlled Breath Control Devices", "Gas Masks", "Exhalation Control"
    ],
    "Knife Play": [
        "Fear Play with Blades", "Controlled Skin Contact", "Scraping the Skin", 
        "Cold Metal Sensation Play", "Edge Play with Sharp Objects", 
        "Psychological Intensity with Knives", "Wax/Rope Cutting Scenes"
    ],
    "Roleplay": [
        "Doctor/Patient", "Boss/Employee", "'Captured and Interrogated' Dynamics", 
        "'Fantasy Creatures' (Vampires, Aliens)", "Authority Figures", "Taboo Scenarios"
    ],
    "Primal Play": [
        "Animal Roleplay", "Growling/Snarling", "Non-Verbal Communication", 
        "Physical Dominance Displays", "Biting/Scratching During Scenes", 
        "Predator/Prey Dynamics", "Animalistic Sounds"
    ],
    "Foot Fetish": [
        "Toe Sucking", "Foot Worship", "High Heels", "Foot Smelling/Sniffing", 
        "Trampling (Feet on Body)", "Pedicures as Rituals", "Stockings/Socks Fetish"
    ],
    "Nylon Kink": [
        "Pantyhose", "Fishnets", "Garters", "Stockings with Heels", 
        "Tearing Nylon During Scenes", "Worshipping Nylon-Clad Legs", "Encasement"
    ],
    "Cross-Dressing": [
        "Wearing Opposite Gender Clothing for Arousal", "Makeup Application Roleplay", 
        "Wig Wearing Transformation", "Feminization/Masculinization Costumes", 
        "Gender-Bending in Scenes", "Exploring Gender Identity Through Dress-Up"
    ],
    "Pregnancy Fetish": [
        "Arousal from Visible Pregnancy", "'Pregnant Lover' Scenarios", 
        "Pregnancy Worship", "Belly Touching Fetishes", 
        "Impregnation Fantasies", "Fertility Goddess Imagery"
    ],
    "Lactation Fetish": [
        "Breast Milk Consumption", "'Nursing' Roleplay", "Milk-Inducing Techniques", 
        "Milking Machines for Lactation Scenes", "Breast Worship with Lactation Play", 
        "Hucow Roleplay Integration", "Feeding a Partner"
    ],
    "Exhibitionism": [
        "Public Nudity", "Performing in Front of Others", 
        "Revealing Clothing in Public", "Flashing (Consensual)", 
        "Being Watched During Intimate Acts", "Outdoor Sex Fantasies", 
        "Webcam Performances"
    ],
    "Voyeurism": [
        "Watching Consensual Acts", "Observing at Sex Parties", 
        "Peeping Scenarios (Staged/Consensual)", "Watching Porn with Partner", 
        "Watching Through Windows/Doors", "Erotic Watching Without Participating"
    ],
    "Tickling (Knismolagnia)": [
        "Feathers", "Tied Down Tickling", "Light Fingertip Touches", 
        "Tickling With Restraints", "Electric Toothbrushes for Sensation Play", 
        "Forced Laughter in Scenes", "Tickling as Teasing/Torture"
    ],
    "Golden Showers": [
        "Peeing on Partner", "Being Peed On", "Peeing in Controlled Spaces (Shower)", 
        "Marking Partner with Urine", "Peeing as Dominance Display", 
        "Incorporating Urine into D/s Dynamics"
    ],
    "Hucow Roleplay": [
        "Milking Machines", "'Human Cow' Roleplay", "Lactation Induction", 
        "Cowbells and Collars as Props", "Feeding Partner Milk", 
        "Breast Worship in Hucow Contexts", "Crawling/Mooing Roleplay"
    ],
    "SPH (Small Penis Humiliation)": [
        "Verbal Teasing About Size", "Comparison to Larger Partners", 
        "Embarrassment in Size-Based Scenarios", "'Measuring' Roleplay", 
        "Mockery During Sexual Acts", "Public/Group Size Humiliation"
    ],
    "Breeding Kink": [
        "Impregnation Roleplay", "'Put a Baby in Me' Fantasies", 
        "Alien Egg Implantation (Ovipositors)", "Risk of Pregnancy Fantasy", 
        "Erotic Focus on Fertility", "Cum-Inflation Fantasies", "Multiple Partner Breeding"
    ],
    "Rope Bondage": [
        "Shibari", "Kinbaku", "Full Body Harnesses", "Suspension Bondage Techniques", 
        "Decorative Rope Patterns", "Partial Restraint Scenes", "Sensation of Rope Burn"
    ],
    "Corsetry/Tight-Lacing": [
        "Waist Training", "Breath-Restricting Corsets", "Victorian Aesthetic Roleplay", 
        "'Dollification' Through Corsets", "Tight-Lace Punishment Dynamics", 
        "Corset Fetishism", "Enduring Tight Lacing"
    ],
    "Fisting": [
        "Anal Fisting", "Vaginal Fisting with Proper Technique", 
        "Stretching Toys for Preparation", "Slow and Gentle Fisting Dynamics", 
        "Punch Fisting (Risk-Aware)", "Double Fisting Scenarios", "Aftercare Focus"
    ],
    "Objectification": [
        "Sex Doll Roleplay", "Furniture Objectification (Human Chair/Table)", 
        "Pet Objectification", "Dehumanization Scenarios in D/s", 
        "Mannequin Roleplay", "Human Ashtray Scenarios", "Used as a Prop/Tool"
    ],
    "Primal Fear Play": [
        "Chase-and-Capture Dynamics", "'Hunted Prey' Scenarios", 
        "Growling/Snarling with Intimidating Intent", "Natural Settings (Forests)", 
        "Non-Verbal Communication", "Scratching/Biting Predatory Behavior", 
        "Fear-Induced Adrenaline Turn-On"
    ]
}

# -----------------------------------------------------------------------------
# CASCADING WEIGHT MATRIX ACCORDING TO UPSTREAM ANCHORS
# -----------------------------------------------------------------------------
ENNEAGRAM_WEIGHTS: Dict[str, Dict[str, float]] = {
    "1": {
        "Corner Time": 1.7, 
        "Erotic Humiliation": 1.5, 
        "Power Exchange": 1.4, 
        "Corsetry/Tight-Lacing": 1.4, 
        "BDSM": 1.3
    },
    "2": {
        "Chastity Play": 1.6, 
        "Lactation Fetish": 1.5, 
        "Hucow Roleplay": 1.4, 
        "Roleplay": 1.3, 
        "Breeding Kink": 1.3
    },
    "3": {
        "Exhibitionism": 1.7, 
        "Corsetry/Tight-Lacing": 1.5, 
        "Foot Fetish": 1.4, 
        "Nylon Kink": 1.4, 
        "Erotic Humiliation": 1.3
    },
    "4": {
        "Rope Bondage": 1.8, 
        "Sensory Deprivation": 1.6, 
        "Objectification": 1.5, 
        "Corsetry/Tight-Lacing": 1.4, 
        "Knife Play": 1.4
    },
    "5": {
        "Electrostimulation": 1.7, 
        "Voyeurism": 1.6, 
        "Sensory Deprivation": 1.4, 
        "Rope Bondage": 1.3, 
        "Foot Fetish": 1.2
    },
    "6": {
        "Power Exchange": 1.6, 
        "Primal Fear Play": 1.5, 
        "Corner Time": 1.4, 
        "Breath Play": 1.3, 
        "BDSM": 1.3
    },
    "7": {
        "Primal Play": 1.6, 
        "Exhibitionism": 1.5, 
        "Roleplay": 1.4, 
        "Primal Fear Play": 1.4, 
        "Tickling (Knismolagnia)": 1.3
    },
    "8": {
        "Impact Play": 1.8, 
        "Primal Fear Play": 1.7, 
        "BDSM": 1.6, 
        "Power Exchange": 1.5, 
        "Fisting": 1.5, 
        "Knife Play": 1.4
    },
    "9": {
        "Sensory Deprivation": 1.6, 
        "Objectification": 1.5, 
        "Chastity Play": 1.4, 
        "Tickling (Knismolagnia)": 1.3, 
        "Golden Showers": 1.2
    }
}

TEMPERAMENT_WEIGHTS: Dict[str, Dict[str, float]] = {
    "neurotic": {
        "Corner Time": 1.4, 
        "Sensory Deprivation": 1.4, 
        "Erotic Humiliation": 1.3, 
        "Breath Play": 1.3
    },
    "extroverted": {
        "Exhibitionism": 1.7, 
        "Primal Play": 1.5, 
        "Roleplay": 1.4, 
        "Impact Play": 1.3
    },
    "introverted": {
        "Voyeurism": 1.6, 
        "Sensory Deprivation": 1.4, 
        "Rope Bondage": 1.4, 
        "Electrostimulation": 1.3
    },
    "agreeable": {
        "Roleplay": 1.3, 
        "Tickling (Knismolagnia)": 1.4, 
        "Chastity Play": 1.3, 
        "Breeding Kink": 1.2
    },
    "conscientious": {
        "Corsetry/Tight-Lacing": 1.5, 
        "Rope Bondage": 1.4, 
        "Power Exchange": 1.3, 
        "Corner Time": 1.3
    }
}


def get_weighted_sexual_preferences(
    orientation: str,
    personality: Dict[str, Any],
    age: int = 30,
    sex: str = "female"
) -> Dict[str, str]:
    """
    Calculates dynamic scores across all 29 categories in KINK_DICT using 
    upstream anchors (Enneagram, Temperament, Age, Sex, Orientation).
    
    Returns a unified Dict[str, str] compatible with Persona dataclass & orchestrator.
    """
    enneagram_type = str(personality.get("enneagram_type", "5")).strip()
    temperament = str(personality.get("temperament", "Introverted")).lower().strip()
    clean_orientation = orientation.lower().strip()

    scored_categories: List[Dict[str, Any]] = []

    for category, subtypes in KINK_DICT.items():
        score = 1.0

        # 1. Enneagram Matrix Multiplier
        if enneagram_type in ENNEAGRAM_WEIGHTS:
            score *= ENNEAGRAM_WEIGHTS[enneagram_type].get(category, 1.0)

        # 2. Temperament Matrix Multiplier
        if temperament in TEMPERAMENT_WEIGHTS:
            score *= TEMPERAMENT_WEIGHTS[temperament].get(category, 1.0)

        # 3. Orientation Multipliers
        if "lesbian" in clean_orientation and category in ["Nylon Kink", "Roleplay", "Sensory Deprivation", "Rope Bondage"]:
            score *= 1.25
        elif "bisexual" in clean_orientation or "pansexual" in clean_orientation:
            score *= 1.15

        # 4. Age Curves
        if age > 45:
            if category in ["Power Exchange", "Sensory Deprivation", "Voyeurism", "Corsetry/Tight-Lacing", "Chastity Play"]:
                score *= 1.35
        elif age < 28:
            if category in ["Primal Play", "Primal Fear Play", "Exhibitionism", "Erotic Humiliation", "Impact Play"]:
                score *= 1.35

        # Random variance engine (0.8 - 1.2) for organic variance
        score *= random.uniform(0.8, 1.2)

        scored_categories.append({
            "category": category,
            "subtypes": subtypes,
            "score": score
        })

    scored_categories.sort(key=lambda x: x["score"], reverse=True)

    primary_choice = scored_categories[0]
    secondary_choice = scored_categories[1]
    wildcard_choice = random.choice(scored_categories[2:8])

    sub_primary = random.choice(primary_choice["subtypes"])
    sub_secondary = random.choice(secondary_choice["subtypes"])
    sub_wildcard = random.choice(wildcard_choice["subtypes"])

    # Determine Dynamic Orientation
    if enneagram_type in ["8", "3", "1"]:
        rel_dynamic = random.choice(["Dominant (Top)", "Strict Switch (Dom-leaning)", "Master/Mistress Persona"])
    elif enneagram_type in ["2", "6", "9"]:
        rel_dynamic = random.choice(["Submissive (Bottom)", "Service Oriented Switch", "Pet/Property Persona"])
    else:
        rel_dynamic = random.choice(["Switch (Versatile)", "Sensory Explorer", "Observer/Voyeur Lean"])

    intensity_val = random.randint(7, 10) if enneagram_type in ["8", "4", "1"] else random.randint(3, 8)
    frequency_val = random.choice(["Occasional In-Bed Integration", "Frequent Scene Play", "24/7 Lifestyle Commitment", "Strictly Private Fantasy"])

    return {
        "Primary Kink Focus": f"{primary_choice['category']} ({sub_primary})",
        "Secondary Interest": f"{secondary_choice['category']} ({sub_secondary})",
        "Latent/Wildcard Interest": f"{wildcard_choice['category']} ({sub_wildcard})",
        "Dynamic Orientation": rel_dynamic,
        "Intensity Index": f"{intensity_val}/10",
        "Lifestyle Frequency": frequency_val,
        "Psychological Intimacy Driver": f"Driven by Enneagram Type {enneagram_type} core mechanisms under {personality.get('temperament', 'Neutral')} state."
    }