"""
enneagram_psychodynamics.py

Generates high-fidelity psychodynamic behavioral tokens including Instinctual Subtypes
(Self-Preservation, Social, Sexual/One-to-One), Stress Disintegration Vectors,
Integration Growth Pathways, and Somatic Armoring Mechanics.

Refined with advanced Enneagram somatic armor research and uncensored local LLM 
character grounding tokens.
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
        instinct_weights = [("sp", 3.0), ("so", 1.0), ("sx", 1.5)]
    elif temp_lower in ["extroverted", "agreeable"]:
        instinct_weights = [("sp", 1.0), ("so", 3.0), ("sx", 2.0)]

    chosen_instinct = _weighted_choice(instinct_weights)

    subtype_matrix: Dict[str, Dict[str, Tuple[str, str]]] = {
        "1": {
            "sp": ("Self-Preservation 1 (Worry)", "Compulsive obsession with physical order, safety, and double-checking practical details; covert anxiety masked as perfectionism and bodily control."),
            "so": ("Social 1 (Inadaptability)", "Rigid adherence to social protocols; acts as an unyielding beacon of moral duty, structural correctness, and behavioral expectation."),
            "sx": ("Sexual 1 (Zeal)", "Intense, righteous drive to reform specific partners; projects high demands for ideological purity, physical perfection, and strict adherence to personal standards.")
        },
        "2": {
            "sp": ("Self-Preservation 2 (Privilege)", "Adopts an endearing, childlike vulnerability to secure physical protection; expects needs to be met implicitly through charm and subtle dependency."),
            "so": ("Social 2 (Ambition)", "Strategic cultivated generosity targeting influential figures; uses extensive social and power networks to make themselves indispensable."),
            "sx": ("Sexual 2 (Seduction)", "Intensely magnetic and emotionally seductive; hyper-focused on captivating chosen targets through intense intimacy, charm, and emotional possession.")
        },
        "3": {
            "sp": ("Self-Preservation 3 (Security)", "Relentless work ethic centered on material success, physical stamina, and operational efficiency; avoids flashy vanity in favor of tangible achievement."),
            "so": ("Social 3 (Prestige)", "Hyper-attuned to status symbols and institutional recognition; curates an impeccable public persona, physical presentation, and social pedigree."),
            "sx": ("Sexual 3 (Charisma)", "Adapts physical appeal, allure, and emotional presentation to embody the absolute personal ideal of a chosen partner.")
        },
        "4": {
            "sp": ("Self-Preservation 4 (Tenacity)", "Endures deep internal suffering silently without complaining; converts melancholy into stoic stamina and tough self-reliance."),
            "so": ("Social 4 (Shame)", "Hyper-sensitive to feeling defective or outcast; openly communicates vulnerability and compares self to peers with persistent self-deprecation."),
            "sx": ("Sexual 4 (Competition)", "Expresses envy as fierce, aggressive competitiveness; demands total emotional intensity, raw expression, and compensation for slights.")
        },
        "5": {
            "sp": ("Self-Preservation 5 (Castle)", "Builds impenetrable physical and mental boundaries around personal space and energy to prevent depletion and invasion."),
            "so": ("Social 5 (Totem)", "Connects with others exclusively through specialized intellectual systems, expert circles, complex theories, and shared technical interests."),
            "sx": ("Sexual 5 (Confidence)", "Seeks intense, secret intellectual and emotional intimacy; searches for a single trusted confidant to share private inner worlds and taboo interests.")
        },
        "6": {
            "sp": ("Self-Preservation 6 (Warmth)", "Cultivates disarming alliances and warm friendships to neutralize potential threats, hostility, and emotional unpredictability."),
            "so": ("Social 6 (Duty)", "Strictly adheres to organizational rules, codes of conduct, and clear authorities to maintain systemic safety and relational clarity."),
            "sx": ("Sexual 6 (Strength/Beauty)", "Counterphobic orientation; meets fear and vulnerability with aggressive confrontation, physical readiness, striking self-assertion, or seductive power.")
        },
        "7": {
            "sp": ("Self-Preservation 7 (Keepers)", "Networks aggressively for practical advantage; surrounds self with a chosen inner circle of resource providers and hedonistic allies."),
            "so": ("Social 7 (Sacrifice)", "Suppresses immediate desires to project an altruistic, saintly image; eager to be seen serving group goals and elevating collective mood."),
            "sx": ("Sexual 7 (Fascination)", "Enthusiastically idealizes exotic ideas, novel partners, and utopian visions; easily intoxicated by new horizons, rapid stimulation, and intense chemistry.")
        },
        "8": {
            "sp": ("Self-Preservation 8 (Satisfier)", "Direct, pragmatic, and territorial focus on securing material resources, physical comfort, dominance, and immediate physical autonomy."),
            "so": ("Social 8 (Solidarity)", "Protective, fiercely loyal champion of the disenfranchised; channels power into guarding their inner circle against external threats."),
            "sx": ("Sexual 8 (Possession)", "Demands total emotional transparency, intense engagement, physical dominance, and complete raw honesty in intimate relationships.")
        },
        "9": {
            "sp": ("Self-Preservation 9 (Appetite)", "Substitutes deep emotional expression with physical comforts, structured routines, sleep, food, or repetitive soothing habits."),
            "so": ("Social 9 (Participation)", "Pours immense energy into group goals and social cohesion while completely neglecting personal priorities, desires, and identity."),
            "sx": ("Sexual 9 (Fusion)", "Merges identity, opinions, and physical energy entirely with strong partners, adopting their drives, beliefs, and behavioral habits.")
        }
    }

    type_data = subtype_matrix.get(clean_type, subtype_matrix["5"])
    sub_title, sub_desc = type_data.get(chosen_instinct, type_data["sp"])

    # -------------------------------------------------------------------------
    # 2. Stress Disintegration & Integration Dynamics
    # -------------------------------------------------------------------------
    dynamics_matrix: Dict[str, Dict[str, str]] = {
        "1": {
            "stress": "Disintegrates to 4: Under pressure, becomes bitter, moodily defensive, dramatically misunderstood, quietly self-pitying, and resentfully uninhibited.",
            "growth": "Integrates to 7: In security, releases rigid perfectionism, becoming spontaneous, joyful, emotionally adaptable, and tolerant of imperfection."
        },
        "2": {
            "stress": "Disintegrates to 8: Under pressure, turns abruptly aggressive, demanding, domineering, vengeful, and resentfully controlling.",
            "growth": "Integrates to 4: In security, develops authentic self-awareness, acknowledging personal desires and boundaries without manipulation."
        },
        "3": {
            "stress": "Disintegrates to 9: Under pressure, shifts into burn-out numb apathy, passive avoidance, deceptive stonewalling, and paralyzed procrastination.",
            "growth": "Integrates to 6: In security, drops calculated performance, becoming fiercely loyal, grounded, cooperative, and vulnerability-tolerant."
        },
        "4": {
            "stress": "Disintegrates to 2: Under pressure, becomes possessive, overly dependent, emotional manipulates others for reassurance, and smothers partners.",
            "growth": "Integrates to 1: In security, channels chaotic emotional energy into disciplined action, objective focus, and grounded practical creation."
        },
        "5": {
            "stress": "Disintegrates to 7: Under pressure, becomes scattered, hyper-active, intellectually erratic, compulsively distracted, and impulse-driven.",
            "growth": "Integrates to 8: In security, steps out of mental isolation into bold physical action, authoritative presence, and decisive real-world engagement."
        },
        "6": {
            "stress": "Disintegrates to 3: Under pressure, puts on an arrogant performance of hyper-competence, obsessing over image, status, and defensive posture.",
            "growth": "Integrates to 9: In security, drops chronic hyper-vigilance, developing deep calm, emotional trust, and unshakeable inner peace."
        },
        "7": {
            "stress": "Disintegrates to 1: Under pressure, turns critical, dogmatically rigid, easily irritated, punitive, and sternly perfectionistic.",
            "growth": "Integrates to 5: In security, grounds scattered energy into deep focus, intellectual rigor, quiet emotional presence, and deliberate pacing."
        },
        "8": {
            "stress": "Disintegrates to 5: Under pressure, withdraws into icy isolation, secretive paranoia, cold calculation, and hyper-vigilant emotional silence.",
            "growth": "Integrates to 2: In security, softens armor to show tender vulnerability, open-hearted protection, physical gentleness, and genuine warmth."
        },
        "9": {
            "stress": "Disintegrates to 6: Under pressure, turns anxious, hyper-vigilant, defensive, passive-aggressive, and burdened by sudden catastrophic worry.",
            "growth": "Integrates to 3: In security, wakes up to personal worth, pursuing ambitious personal goals with vibrant self-assertion and physical vitality."
        }
    }

    dyn = dynamics_matrix.get(clean_type, dynamics_matrix["5"])

    # -------------------------------------------------------------------------
    # 3. Somatic Armoring & Physical Tension Patterns
    # -------------------------------------------------------------------------
    somatic_matrix: Dict[str, List[str]] = {
        "1": [
            "Chronic tension across jawline and masseter muscles, strict erect spinal posture, locked shoulders; shallow abdominal respiration when challenged.",
            "Clenched teeth, tight core bracing, restricted diaphragmatic breathing; involuntary micro-flinches when protocols or order are breached."
        ],
        "2": [
            "Tension held in upper chest, throat, and arms; elevated heart rate during emotional appeals; expressive, reaching arm movements and open body tilts.",
            "Tightness in neck and traps from carrying emotional support burdens; rapid eye-contact seeking and forward posture during intimacy."
        ],
        "3": [
            "Micro-tension in facial muscles to maintain ideal composure; high shoulder line, rigid core engagement ready for immediate physical performance.",
            "Restless lower limbs, rapid eye movement under evaluation, locked abdominal wall masking internal nervous exhaustion."
        ],
        "4": [
            "Sunken chest posture, tension centered around diaphragm and solar plexus, heavy expressive sighing; dramatic fluid gestures masking postural slumps.",
            "Tightness behind the eyes and cervical spine; holds breath when feeling vulnerable, accompanied by sudden intense eye contact or dramatic withdrawal."
        ],
        "5": [
            "Frozen facial expressions, cold extremities, rigid unmoving torso; shallow upper-chest respiration with minimal blink rate during stress.",
            "Hollowed shoulder alignment, physical withdrawal of neck into collarline; minimal physical movement during high-stimulus or intimate settings."
        ],
        "6": [
            "Hyper-vigilant darting eyes, tight neck tendons, micro-clenched fists; constant posture shifting and micro-flinches to unexpected sounds or touch.",
            "Tense lower back and lumbar curve, elevated muscle tone in legs ready for flight/confrontation; rigid neck bracing during questioning."
        ],
        "7": [
            "Rapid shallow breath, restless leg bouncing, flighty upper-body movement; jaw tension from rapid speech and constant sensory scanning.",
            "High overall muscular tone, quick volatile facial transitions; physical fidgeting when constrained or forced into slow emotional pacing."
        ],
        "8": [
            "Heavy grounded stance, broad chest expansion, locked unblinking gaze; dense neck massing, clenched fists in resting posture, assertive forward lean.",
            "Locked jawline, thick abdominal bracing, intense physical proximity; visceral thoracic expansion when exerting dominance or resisting control."
        ],
        "9": [
            "Heavy, relaxed muscle tone bordering on lethargy, shallow steady breath; slumped shoulder line, slow deliberate motor responses.",
            "Soft untensed facial muscles, heavy eyelids, physical grounding through leaning on furniture or partners; delayed motor startle response."
        ]
    }

    somatic_options = somatic_matrix.get(clean_type, somatic_matrix["5"])
    somatic_choice = random.choice(somatic_options)

    if age > 50:
        somatic_choice += " Amplified by chronic joint stiffness, decreased tissue elasticity, and deep-seated physical habituation."

    return {
        "Instinctual Subtype": f"{sub_title} - {sub_desc}",
        "Stress Disintegration": dyn["stress"],
        "Integration Pathway": dyn["growth"],
        "Somatic Armoring": somatic_choice
    }