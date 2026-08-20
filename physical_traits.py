# physical_traits.py
import random
from typing import Dict, Any

# 1. Distinct aesthetic definitions linked directly to lifestyle tracking
STYLE_AESTHETICS = {
    "Minimalist": "clean lines, monochromatic tones, structural tailoring, understated elegance",
    "Edgy": "distressed textures, leather accents, raw dark denim, sharp asymmetric cuts, industrial hardware",
    "Vintage": "classic retro tailoring, silk textures, structured lace, nostalgic silhouettes, timeless glamour",
    "Trendy": "bold contemporary silhouettes, high-contrast streetwear, form-fitting statement pieces",
    "Bohemian": "flowing fabrics, earthy organic textures, layered jewelry, relaxed soft drapes",
    "Glamorous": "luxurious form-enhancing fabrics, striking high-end silhouettes, dramatic clean cuts, polished presentation",
    "Casual": "effortless relaxed basics, soft unstructured fabrics, clean athletic accents",
    "Preppy": "sharp clean-cut tailoring, classic premium knits, structured collegiate lines"
}

COMPLEXION_POOL = [
    "porcelain smooth with a cool undertone", "sun-kissed olive with a warm radiance",
    "rich deep obsidian with a flawless satin sheen", "creamy alabaster, sensitive and clear",
    "warm golden bronze with subtle luminous highlights"
]

SENSORY_DETAILS = [
    "faint scent of vanilla bourbon and rich cedar wood",
    "subtle trace of crisp sea salt and clean white musk",
    "warm aroma of crushed dark cocoa and sweet amber resin",
    "delicate notes of midnight jasmine and soft sandalwood"
]

HAIR_STYLES = {
    "female": ["cropped sharp pixie", "sleek shoulder-length bob", "cascading waves reaching the mid-back", "tightly coiled natural curls pinned up", "messy high volume top-knot"],
    "male": ["sharp textured undercut", "clean classic taper fade", "shoulder-length relaxed waves", "closely cropped buzz cut", "thick neatly groomed pompadour"]
}

def get_random_physical_traits(gender_identity: str, sex: str, age: int, fashion_sense: str) -> Dict[str, str]:
    """
    Generates cohesive, highly descriptive visual prompts for local LLMs
    by evaluating variables pulled from the core IDENTITY BLUEPRINT arrays.
    """
    # Standardize input variables
    sex_clean = sex.lower() if sex.lower() in ["female", "male"] else "female"
    identity_lower = gender_identity.lower()
    
    # 2. Extract Structural Bone / Height Layouts Based on Blueprint Input
    if sex_clean == "male":
        height_range = "tall, broad-shouldered frame with a commanding stance"
        default_hair = random.choice(HAIR_STYLES["male"])
    else:
        # Check if the identity contains "transfeminine" or "cisgender" variants dynamically
        if "transfeminine" in identity_lower:
            height_range = "statuesque, long-limbed frame with a tall and striking physical presence"
        else:
            height_range = "petite and elegantly compact frame with fine bone structure"
        default_hair = random.choice(HAIR_STYLES["female"])

    # 3. Dynamic Biological Build Matrix (Addressing specific design tastes safely)
    if sex_clean == "female":
        build_options = [
            "strikingly hourglass with a soft, full bust and narrow waist",
            "slender, long-limbed, with an athletic and highly toned core",
            "plush with full, soft curves and a classic feminine silhouette",
            "compact, muscular, with defined curves and strong posture"
        ]
    else:
        build_options = [
            "rugged V-taper build with thick shoulders and a lean waist",
            "tall, wiry, with clean definition and an athletic outline",
            "solidly built, broad, with a rugged and powerful physical frame",
            "slender and lean with an understated, elegant proportion"
        ]
    chosen_build = random.choice(build_options)

    # 4. Generate anatomical tokens based on biological sex and tier metrics
    aesthetic_tokens = STYLE_AESTHETICS.get(fashion_sense, STYLE_AESTHETICS["Casual"])
    anatomical_specs = ""
    if sex_clean == "female":
        # Categorized Bra Size Tiers
        tier = random.choices(["below_average", "average", "above_average"], weights=[0.2, 0.6, 0.2])[0]
        band = random.choice(["32", "34", "36", "38"])
        
        if tier == "below_average":
            cup = random.choice(["AA", "A"])
            desc = "modest and petite"
        elif tier == "average":
            cup = random.choice(["B", "C", "D"])
            desc = "classic and well-proportioned"
        else: # above_average
            cup = random.choice(["DD", "DDD/E", "F"])
            desc = "strikingly full and prominent"
            
        anatomical_specs = f"{band}{cup} ({desc})"
        
    else:
        # Categorized Male Dimension Tiers
        tier = random.choices(["below_average", "average", "above_average"], weights=[0.15, 0.70, 0.15])[0]
        
        if tier == "below_average":
            length = round(random.uniform(4.0, 4.9), 1)
            girth = round(random.uniform(3.8, 4.3), 1)
            desc = "discreet and compact"
        elif tier == "average":
            length = round(random.uniform(5.0, 5.9), 1)
            girth = round(random.uniform(4.4, 4.9), 1)
            desc = "perfectly standard and proportional"
        else: # above_average
            length = round(random.uniform(6.0, 7.8), 1)
            girth = round(random.uniform(5.0, 5.8), 1)
            desc = "impressively heavy and substantial"
            
        anatomical_specs = f"{length}\" length x {girth}\" girth - Erect ({desc})"

    # 5. Assemble the final payload
    return {
        "visual_presence": f"{height_range}, featuring {random.choice(COMPLEXION_POOL)}",
        "body_shape_and_build": chosen_build,
        "anatomical_metrics": anatomical_specs,
        "hair_presentation": f"{default_hair}, meticulously styled",
        "aesthetic_vibe": aesthetic_tokens,
        "sensory_signature": random.choice(SENSORY_DETAILS),
        "notable_markings": "a distinct, striking gaze that commands immediate attention"
    }
