# health_profiles.py
import random
from typing import Dict, Any

# Structural pool of physical/somatic markers influenced by behavioral traits
SOMATIC_CONDITIONS = [
    "Suffer from stress-induced tension headaches and lower-back stiffness.",
    "Excellent metabolic health, with high physical stamina and clean sleep cycles.",
    "Prone to mild chronic fatigue, often ignoring dehydration and physical fatigue markers.",
    "Maintains standard physical fitness, but carries high muscle tension across shoulders.",
    "Prone to nervous stomach conditions and acid reflux during periods of professional pressure."
]

# Structural pool of psychological markers influenced by personality archetypes
MENTAL_CONDITIONS = {
    "high_stress": "High psychological burnout risk; constantly over-analyzing responsibilities and struggling to mentally disconnect.",
    "melancholic": "Prone to introspective emotional dips; highly sensitive to perceived rejection or isolation.",
    "anxious": "Undercurrent of low-grade anxiety; constantly managing hyper-vigilance about physical security or control.",
    "resilient": "Remarkably stable mental resilience; naturally possesses adaptive coping mechanisms for high-stress events.",
    "suppressed": "Suppresses personal frustrations or needs to keep peace, leading to sudden bursts of emotional fatigue."
}

def get_contextual_health_profile(age: int, career: str, personality: Dict[str, Any], social_life: Dict[str, str], physical_traits: Dict[str, str]) -> Dict[str, str]:
    """
    Dynamically generates a deeply descriptive health and wellness blueprint 
    by analyzing age, occupational pressure, and psychological traits.
    """
    enneagram = personality.get("enneagram_type", "")
    temperament = personality.get("temperament", "")
    contentment = social_life.get("Contentment Level", "").lower()
    career_lower = career.lower()

    # 1. Evaluate Contextual Mental Health Archetypes
    if "3 - The Achiever" in enneagram or "8 - The Challenger" in enneagram or "manager" in career_lower:
        mental = MENTAL_CONDITIONS["high_stress"]
    elif "4 - The Individualist" in enneagram or "Neurotic" in temperament:
        mental = MENTAL_CONDITIONS["melancholic"]
    elif "6 - The Loyalist" in enneagram or "Anxious" in personality.get("emotional_traits", ""):
        mental = MENTAL_CONDITIONS["anxious"]
    elif "9 - The Peacemaker" in enneagram or "Agreeable" in temperament:
        mental = MENTAL_CONDITIONS["suppressed"]
    else:
        mental = MENTAL_CONDITIONS["resilient"]

    # 2. Evaluate Physical/Somatic Adaptations
    if age > 50 and "dissatisfied" in contentment:
        physical = "Carries persistent joint stiffness and sluggish recovery times, exacerbated by ongoing lifestyle stress."
    elif "Conscientious" in temperament and "high_stress" in mental:
        physical = "Suffer from stress-induced tension headaches and tight jaw alignment; rarely stretches or takes breaks."
    elif "7 - The Enthusiast" in enneagram or "Athletic" in physical_traits.get("body_shape_and_build", ""):
        physical = "Excellent metabolic health, with high physical stamina and clean sleep cycles."
    else:
        physical = random.choice(SOMATIC_CONDITIONS)

    # 3. Add a realistic lifestyle or coping vice element
    if "8 - The Challenger" in enneagram or "chef" in career_lower:
        vice = "Relies on high caffeine intake and irregular eating schedules to push through late shifts."
    elif "7 - The Enthusiast" in enneagram or "Complicated" in social_life.get("Relationship Status", ""):
        vice = "Prone to social drinking and erratic sleep patterns when distracting themselves from stress."
    elif "5 - The Investigator" in enneagram:
        vice = "Sedentary lifestyle habits; tends to hyper-focus on intellectual work and completely skip meals."
    else:
        vice = "Maintains a balanced routine, though prone to minor screen-time addiction before sleeping."

    return {
        "Physical Health Status": physical,
        "Mental & Emotional Baseline": mental,
        "Somatic Coping Mechanisms": vice
    }
