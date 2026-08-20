"""
enneagram_psychodynamics.py

Generates high-fidelity psychodynamic behavioral tokens including Instinctual Subtypes
(Self-Preservation, Social, Sexual/One-to-One), Stress Disintegration Vectors,
Integration Growth Pathways, and Somatic Armoring Mechanics.
"""

import random
from typing import Dict, List, Tuple


def _weighted_choice(options: List[Tuple[str, float]]) -> str:
    """Selects an option based on numeric weights."""
    total = sum(weight for _, weight in options)
    r = random.uniform(0, total)
    upto = 0.0
    for item, weight in options:
        if upto + weight >= r:
            return item
        upto += weight
    return options[-1][0]


def generate_enneagram_psychodynamics(
    enneagram_type: str,
    temperament: str,
    age: int,
    biological_sex: str
) -> Dict[str, str]:
    """
    Generates advanced Enneagram psychodynamics including instinctual subtypes,
    stress disintegration patterns, integration growth paths, and somatic tension points.

    Args:
        enneagram_type: Enneagram type string ("1" through "9")
        temperament: Primary temperament string
        age: Numeric age of the persona
        biological_sex: Biological sex ("male" or "female")

    Returns:
        Dict[str, str]: Key-value pairs of dynamic psychological behavioral drivers.
    """
    clean_type = enneagram_type.strip()

    # -------------------------------------------------------------------------
    # 1. Instinctual Variant & Subtype Allocation
    # -------------------------------------------------------------------------
    instinct_weights: List[Tuple[str, float]] = [
        ("sp", 1.0),  # Self-Preservation
        ("so", 1.0),  # Social
        ("sx", 1.0)   # Sexual / One-to-One
    ]

    temp_lower = temperament.lower()
    if temp_lower in ["introverted", "neurotic"]:
        instinct_weights = [("sp", 3.0), ("so", 1.0), ("sx", 1.0)]
    elif temp_lower in ["extroverted", "agreeable"]:
        instinct_weights = [("sp", 1.0), ("so", 3.0), ("sx", 2.0)]

    chosen_instinct = _weighted_choice(instinct_weights)

    subtype_matrix: Dict[str, Dict[str, Tuple[str, str]]] = {
        "1": {
            "sp": ("Self-Preservation 1 (Worry)", "Compulsive obsession with physical order, double-checking practical details, covert anxiety masked as perfectionism."),
            "so": ("Social 1 (Inadaptability)", "Rigid adherence to social protocols; acts as an unyielding beacon of moral duty and structural correctness."),
            "sx": ("Sexual 1 (Zeal)", "Intense, righteous drive to reform specific individuals; projects high expectations and demands ideological purity.")
        },
        "2": {
            "sp": ("Self-Preservation 2 (Privilege)", "Adopts an endearing, childlike vulnerability to secure protection; expects needs to be met implicitly."),
            "so": ("Social 2 (Ambition)", "Strategic cultivated generosity targeting influential figures; uses power networks to make themselves irreplaceable."),
            "sx": ("Sexual 2 (Seduction)", "Intensely magnetic and emotionally seductive; hyper-focused on captivating individual targets through intimacy.")
        },
        "3": {
            "sp": ("Self-Preservation 3 (Security)", "Relentless work ethic centered on material success and operational efficiency; avoids flashy vanity."),
            "so": ("Social 3 (Prestige)", "Hyper-attuned to elite status symbols and institutional recognition; curates an impeccable public persona."),
            "sx": ("Sexual 3 (Charisma)", "Adapts physical appeal, charm, and emotional presentation to embody the personal ideal of a chosen partner.")
        },
        "4": {
            "sp": ("Self-Preservation 4 (Tenacity)", "Endures deep internal suffering silently without complaining; converts melancholy into stoic stamina."),
            "so": ("Social 4 (Shame)", "Hyper-sensitive to feeling defective or outcast; openly communicates defectiveness and compares self to peers."),
            "sx": ("Sexual 4 (Competition)", "Expresses envy as fierce, aggressive competitiveness; demands compensation for perceived slights and inadequacy.")
        },
        "5": {
            "sp": ("Self-Preservation 5 (Castle)", "Builds impenetrable boundaries around time, personal space, and physical energy to prevent depletion."),
            "so": ("Social 5 (Totem)", "Connects with others exclusively through specialized intellectual systems, expert circles, and complex theories."),
            "sx": ("Sexual 5 (Confidence)", "Seeks intense, secret intellectual intimacy; searches for a single trusted confidant to share private inner worlds.")
        },
        "6": {
            "sp": ("Self-Preservation 6 (Warmth)", "Cultivates gentle, disarming alliances and warm friendships to neutralize potential threats and hostility."),
            "so": ("Social 6 (Duty)", "Strictly adheres to organizational rules, codes of conduct, and clear authorities to maintain systemic safety."),
            "sx": ("Sexual 6 (Strength/Beauty)", "Counterphobic orientation; meets fear with aggressive confrontation, physical readiness, or striking self-assertion.")
        },
        "7": {
            "sp": ("Self-Preservation 7 (Keepers)", "Networks aggressively for practical advantage; surrounds self with a chosen 'family' of resource providers."),
            "so": ("Social 7 (Sacrifice)", "Suppresses immediate desires to project a saintly, altruistic image; eager to be seen serving the group's good."),
            "sx": ("Sexual 7 (Fascination)", "Enthusiastically idealizes exotic ideas, novel people, and utopian visions; easily intoxicated by new horizons.")
        },
        "8": {
            "sp": ("Self-Preservation 8 (Satisfier)", "Direct, pragmatic, and territorial focus on securing material resources, physical comfort, and immediate autonomy."),
            "so": ("Social 8 (Solidarity)", "Protective, fiercely loyal champion of the disenfranchised; channels power into guarding their inner circle."),
            "sx": ("Sexual 8 (Possession)", "Demands total emotional transparency, intense engagement, and complete control over intimate relationships.")
        },
        "9": {
            "sp": ("Self-Preservation 9 (Appetite)", "Substitutes deep emotional needs with physical comforts, structured routines, sleep, food, or soothing habits."),
            "so": ("Social 9 (Participation)", "Pours immense energy into group goals and team cohesion while completely neglecting personal priorities."),
            "sx": ("Sexual 9 (Fusion)", "Merges identity and opinions entirely with strong partners, adopting their drives, beliefs, and habits.")
        }
    }

    type_data = subtype_matrix.get(clean_type, subtype_matrix["5"])
    sub_title, sub_desc = type_data.get(chosen_instinct, type_data["sp"])

    # -------------------------------------------------------------------------
    # 2. Stress Disintegration & Integration Dynamics
    # -------------------------------------------------------------------------
    dynamics_matrix: Dict[str, Dict[str, str]] = {
        "1": {
            "stress": "Disintegrates to 4: Under pressure, becomes bitter, moodily defensive, dramatically misunderstood, and quietly self-pitying.",
            "growth": "Integrates to 7: In security, releases rigid perfectionism, becoming spontaneous, joyful, and tolerant of imperfection."
        },
        "2": {
            "stress": "Disintegrates to 8: Under pressure, turns abruptly aggressive, demanding, domineering, and resentfully controlling.",
            "growth": "Integrates to 4: In security, develops authentic self-awareness, acknowledging personal needs without manipulation."
        },
        "3": {
            "stress": "Disintegrates to 9: Under pressure, shifts into burn-out numb apathy, passive avoidance, and paralyzed procrastination.",
            "growth": "Integrates to 6: In security, drops calculated performance, becoming fiercely loyal, grounded, and team-dedicated."
        },
        "4": {
            "stress": "Disintegrates to 2: Under pressure, becomes clingy, overly dependent, and manipulates others for reassurance.",
            "growth": "Integrates to 1: In security, channels chaotic emotions into disciplined action, objective focus, and practical creation."
        },
        "5": {
            "stress": "Disintegrates to 7: Under pressure, becomes scattered, hyper-active, intellectually erratic, and compulsively distracted.",
            "growth": "Integrates to 8: In security, steps out of mental isolation into bold physical action, authority, and decisive engagement."
        },
        "6": {
            "stress": "Disintegrates to 3: Under pressure, puts on an arrogant performance of hyper-competence, obsessing over image and defense.",
            "growth": "Integrates to 9: In security, drops chronic hyper-vigilance, developing deep calm, trust, and unshakeable inner peace."
        },
        "7": {
            "stress": "Disintegrates to 1: Under pressure, turns critical, dogmatically rigid, easily irritated, and sternly perfectionistic.",
            "growth": "Integrates to 5: In security, grounds scattered energy into deep focus, intellectual rigor, and quiet emotional presence."
        },
        "8": {
            "stress": "Disintegrates to 5: Under pressure, withdraws into icy isolation, secretive paranoia, and hyper-calculating silence.",
            "growth": "Integrates to 2: In security, softens armor to show tender vulnerability, open-hearted protection, and genuine warmth."
        },
        "9": {
            "stress": "Disintegrates to 6: Under pressure, turns anxious, hyper-vigilant, defensive, and burdened by sudden catastrophic worry.",
            "growth": "Integrates to 3: In security, wakes up to personal worth, pursuing ambitious personal goals with vibrant self-assertion."
        }
    }

    dyn = dynamics_matrix.get(clean_type, dynamics_matrix["5"])

    # -------------------------------------------------------------------------
    # 3. Somatic Armoring & Physical Tension Patterns
    # -------------------------------------------------------------------------
    somatic_matrix: Dict[str, List[str]] = {
        "1": [
            "Chronic tension across jawline, strict erect spinal posture, locked shoulders.",
            "Clenched teeth, tight abdominal bracing, shallow diaphragmatic breath."
        ],
        "2": [
            "Tension held in upper chest and throat, quick heart rate, expressive hands.",
            "Tightness in neck and traps from carrying physical helpfulness, open body tilt."
        ],
        "3": [
            "Micro-tension in facial muscles to maintain composure, high shoulder line.",
            "Restless lower limbs, rapid eye movement, locked core ready for fast action."
        ],
        "4": [
            "Sunken chest posture, tension in diaphragm, heavy expressive sighing.",
            "Tightness behind the eyes and neck, dramatic fluid gestures hiding postural slump."
        ],
        "5": [
            "Frozen facial expressions, cold extremities, rigid unmoving torso.",
            "Shallow upper-chest respiration, hollowed shoulder position, minimal eye blinks."
        ],
        "6": [
            "Hyper-vigilant darting eyes, tight neck tendons, micro-clenched fists.",
            "Constant weight-shifting, micro-flinching to sudden movements, tense lower back."
        ],
        "7": [
            "Rapid breath, restless leg bouncing, flighty upper-body movement.",
            "High muscular tone, quick facial transitions, jaw tension from rapid speech."
        ],
        "8": [
            "Heavy grounded posture, broad chest expansion, locked unblinking gaze.",
            "Dense neck and shoulder massing, clenched fists in resting stance, forward lean."
        ],
        "9": [
            "Heavy, relaxed muscle tone bordering on lethargy, shallow steady breath.",
            "Slumped shoulder line, slow deliberate motor speed, soft untensed facial tone."
        ]
    }

    somatic_options = somatic_matrix.get(clean_type, somatic_matrix["5"])
    somatic_choice = random.choice(somatic_options)

    if age > 50:
        somatic_choice += " Amplified by chronic joint stiffness and deep-seated muscle memory."

    return {
        "Instinctual Subtype": f"{sub_title} - {sub_desc}",
        "Stress Disintegration": dyn["stress"],
        "Integration Pathway": dyn["growth"],
        "Somatic Armoring": somatic_choice
    }