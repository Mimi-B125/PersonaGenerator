# coachable_topics.py
import random
from typing import List, Dict, Any

# TOPIC_POOL refactored to align with ICF Competencies:
# - Shifts from "Are you struggling with X?" to "What would open up if you did X?"
# - Focuses on agency, somatic/emotional awareness, and forward momentum.
TOPIC_POOL = [
    {
        "icf_focus": "Competency 7: Evoking Awareness (Shifting Perspective)",
        "question": "What becomes possible for your long-held dreams if you redefine failure as a source of clean feedback?",
        "triggers": {"enneagrams": ["3 - The Achiever", "5 - The Investigator"], "temperaments": ["Conscientious", "Neurotic"]}
    },
    {
        "icf_focus": "Competency 7: Exploring Beyond Current Thinking",
        "question": "What is the unexpressed boundary you are holding right now, and what do you need to honor it?",
        "triggers": {"enneagrams": ["9 - The Peacemaker", "2 - The Helper"], "temperaments": ["Introverted", "Agreeable"]}
    },
    {
        "icf_focus": "Competency 7: Somatic & Emotional Integration",
        "question": "When you think about setting a firm boundary, where do you feel that tension in your body, and what is it telling you?",
        "triggers": {"enneagrams": ["2 - The Helper", "6 - The Loyalist"], "temperaments": ["Agreeable", "Neurotic"]}
    },
    {
        "icf_focus": "Competency 8: Facilitating Client Growth (Sustainability)",
        "question": "How can you design your current role so that your impact expands while your baseline energy is actively restored?",
        "triggers": {"enneagrams": ["3 - The Achiever", "8 - The Challenger", "1 - The Reformer"], "temperaments": ["Conscientious", "Extroverted"]}
    },
    {
        "icf_focus": "Competency 7: Breaking Decision Paralysis",
        "question": "If structural perfection weren't a requirement for your next step, what micro-action would you take right now?",
        "triggers": {"enneagrams": ["1 - The Reformer", "5 - The Investigator"], "temperaments": ["Conscientious", "Neurotic"]}
    },
    {
        "icf_focus": "Competency 7: Evoking Core Values",
        "question": "When you pause the sprint for new experiences, what core value or internal truth is waiting to be acknowledged?",
        "triggers": {"enneagrams": ["7 - The Enthusiast"], "temperaments": ["Extroverted"]}
    },
    {
        "icf_focus": "Competency 6: Listening Actively to the Who",
        "question": "Who do you choose to be in moments when your unique perspective runs the risk of being misunderstood?",
        "triggers": {"enneagrams": ["4 - The Individualist", "6 - The Loyalist"], "temperaments": ["Introverted", "Neurotic"]}
    },
    {
        "icf_focus": "Competency 4: Cultivating Trust and Safety (Vulnerability)",
        "question": "What would it look like to lean on the strengths of your team, allowing collaboration to replace your protective armor?",
        "triggers": {"enneagrams": ["8 - The Challenger"], "temperaments": ["Neurotic", "Introverted"]}
    }
]

def get_tailored_coachable_topics(personality: Dict[str, Any], count: int = 2) -> List[str]:
    """
    Scores and extracts the most relevant ICF-compliant coaching questions 
    based on the persona's Enneagram type and Temperament.
    """
    enneagram = personality.get("enneagram_type", "")
    temperament = personality.get("temperament", "")
    
    scored_topics = []
    
    for item in TOPIC_POOL:
        score = 0.5  # Baseline weight
        
        if enneagram in item["triggers"].get("enneagrams", []):
            score += 1.5
            
        if temperament in item["triggers"].get("temperaments", []):
            score += 1.0
            
        scored_topics.append((score, item["question"]))
        
    scored_topics.sort(key=lambda x: x[0], reverse=True)
    
    # Extract strings from the top tier, shuffle, and return the clean slice
    top_tier = [text for score, text in scored_topics[:count + 2]]
    random.shuffle(top_tier)
    
    return top_tier[:count]
