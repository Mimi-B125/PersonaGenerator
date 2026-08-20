# skills_and_talents.py
import random
from typing import List, Dict, Any

# A multi-tiered pool structured around specific career domains, hobbies, and personal attributes
SKILLS_MATRIX: Dict[str, List[str]] = {
    "Technical & Engineering": [
        "Python Programming & Scripting", "Data Analysis & Visualization",
        "Network Infrastructure Configuration", "DC Power Systems Wiring",
        "PLC Automation Logic", "RF Equipment Calibration",
        "Linux Server Administration", "Database Design & SQL"
    ],
    "Creative & Literary": [
        "Creative Fiction Writing", "Narrative Architecture",
        "Psychological Character Building", "Oil Portrait Painting",
        "Graphic Design & Typography", "Woodworking & Joinery",
        "Textile Arts & Embroidery", "Acoustic Ukulele Performance"
    ],
    "Humanitarian & Interpersonal": [
        "Active Listening & Empathy", "Co-Active Leadership Coaching",
        "Group Facilitation & Mediation", "Somatic Conflict Resolution",
        "Public Speaking & Presentation", "Community Program Advocacy",
        "Strategic Boundary Setting", "Cross-Cultural Communication"
    ],
    "Practical & Applied": [
        "Artisanal Bread Baking", "Outdoor Campfire Gastronomy",
        "High-Intensity Aerobic Fitness", "Strategic Board Game Theory",
        "Micro-Atmospheric Climate Control", "Precision Tool Operation",
        "Horticultural Management", "Budgetary Operations Logistics"
    ]
}

def get_weighted_skills(count: int = 2, career: str = None, personality: Dict[str, Any] = None) -> List[str]:
    """
    Dynamically extracts a balanced, logically contextualized pool of skills and talents.
    
    Ensures that a persona receives an intuitive spread combining technical proficiencies 
    aligned with their professional identity alongside distinct creative or interpersonal talents.
    """
    selected_skills: List[str] = []
    available_pools = {domain: list(items) for domain, items in SKILLS_MATRIX.items()}
    
    # 1. Inject Context-Driven Professional Anchors
    if career:
        career_lower = career.lower()
        if any(tech_keyword in career_lower for tech_keyword in ["developer", "engineer", "accountant", "project manager"]):
            tech_skill = random.choice(available_pools["Technical & Engineering"])
            selected_skills.append(tech_skill)
            available_pools["Technical & Engineering"].remove(tech_skill)
        elif any(creative_keyword in career_lower for creative_keyword in ["writer", "artist", "chef", "designer"]):
            creative_skill = random.choice(available_pools["Creative & Literary"])
            selected_skills.append(creative_skill)
            available_pools["Creative & Literary"].remove(creative_skill)
        elif any(human_keyword in career_lower for human_keyword in ["teacher", "nurse", "paralegal", "librarian", "parent"]):
            human_skill = random.choice(available_pools["Humanitarian & Interpersonal"])
            selected_skills.append(human_skill)
            available_pools["Humanitarian & Interpersonal"].remove(human_skill)

    # 2. Inject Personality-Driven Interpersonal/Behavioral Anchors
    if personality:
        enneagram = personality.get("enneagram_type", "")
        # Nurturing types lean toward human-centered skills, thinkers lean toward analytics
        if any(type_id in enneagram for type_id in ["1", "2", "6", "9"]):
            pool_key = "Humanitarian & Interpersonal"
        elif any(type_id in enneagram for type_id in ["3", "5", "8"]):
            pool_key = "Technical & Engineering"
        else:
            pool_key = "Creative & Literary"
            
        if available_pools[pool_key]:
            trait_skill = random.choice(available_pools[pool_key])
            selected_skills.append(trait_skill)
            available_pools[pool_key].remove(trait_skill)

    # 3. Dynamic Fallback / Enrichment Phase
    # Combines all remaining unpicked entries to satisfy the final requested element count
    fallback_pool = []
    for domain_items in available_pools.values():
        fallback_pool.extend(domain_items)
        
    needed = count - len(selected_skills)
    if needed > 0 and fallback_pool:
        sampled_fallbacks = random.sample(fallback_pool, k=min(needed, len(fallback_pool)))
        selected_skills.extend(sampled_fallbacks)
        
    return selected_skills[:count]
