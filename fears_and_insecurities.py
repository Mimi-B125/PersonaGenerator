import random
from typing import List

FEARS_AND_INSECURITIES_LIST = [
    "Impending sense of professional failure or being exposed as a fraud.",
    "Intense social anxiety; terrfied of being judged or rejected in intimate settings.",
    "Fear of losing control over their emotions or breaking down publicly.",
    "Severe abandonment issues; pushing others away before they can leave.",
    "Fear of stagnation; terrified of wasting their potential or getting stuck.",
    "Anxiety about physical or mental vulnerability; hates relying on others.",
    "Fear of conflict; will completely suppress their own boundaries to keep peace.",
    "Deep insecurity about their appearance or how their body is perceived.",
    "Fear of emotional intimacy; uses sarcasm as a defense mechanism to keep distance.",
    "Anxiety about financial instability or losing their independence."
]

def get_random_fears(count: int = 2) -> List[str]:
    """
    Returns a random sample of psychological fears or insecurities.
    """
    return random.sample(FEARS_AND_INSECURITIES_LIST, k=min(count, len(FEARS_AND_INSECURITIES_LIST)))
