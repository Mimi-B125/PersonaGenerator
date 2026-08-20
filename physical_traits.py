# physical_traits.py
import random
from typing import Dict, Any

# 1. Distinct aesthetic styles mapped to the lifestyle fashion sense
STYLE_AESTHETICS = {
    "Minimalist": ["clean lines, monochromatic tones, structural tailoring, understated elegance"],
    "Edgy": ["distressed textures, leather accents, raw dark denim, sharp asymmetric cuts, industrial hardware"],
    "Vintage": ["classic retro tailoring, silk textures, structured lace, nostalgic silhouettes, timeless glamour"],
    "Trendy": ["bold contemporary silhouettes, high-contrast streetwear, form-fitting statement pieces"],
    "Bohemian": ["flowing fabrics, earthy organic textures, layered jewelry, relaxed soft drapes"],
    "Glamorous": ["luxurious form-enhancing fabrics, striking high-end silhouettes, dramatic clean cuts, polished presentation"],
    "Casual": ["effortless relaxed basics, soft unstructured fabrics, clean athletic accents"],
    "Preppy": ["sharp clean-cut tailoring, classic premium knits, structured collegiate lines"]
}

# 2. Somatic and visual presentation vectors driven by biological sex and fitness archetypes
COMPLEXION_AND_TEXTURE = [
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

# 3. Dynamic layout generator
def get_random_physical_traits(sex: str = "female", age: int = 35, fashion_sense: str = "Casual") -> Dict[str, str]:
    """
    Generates high-fidelity visual and physical prompt tokens optimized 
    for character persistence in local generation workflows.
    """
    sex_clean = sex.lower() if sex.lower() in ["female", "male"] else "female"
    
    # Resolve style aesthetics safely with a fallback
    aesthetic_tokens = random.choice(STYLE_AESTHETICS.get(fashion_sense, STYLE_AESTHETICS["Casual"]))
    
    # Select gender-appropriate hair styling
    hair_style_choice = random.choice(HAIR_STYLES[sex_clean])
    
    # Height parameters using absolute descriptive scales
    height_range = "petite and compact" if sex_clean == "female" else "slender and lean"
    
    return {
        "visual_presence": f"{height_range}, with {random.choice(COMPLEXION_AND_TEXTURE)}",
        "hair_presentation": f"{hair_style_choice}, shaded in a rich deep tone",
        "aesthetic_vibe": aesthetic_tokens,
        "sensory_signature": random.choice(SENSORY_DETAILS),
        "notable_markings": "a distinct, striking gaze that commands immediate attention"
    }
