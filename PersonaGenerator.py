import random
import os
import time
from typing import List, Dict
from dataclasses import dataclass

# Modular Imports
from physical_traits import get_random_physical_traits
from sexual_preferences import get_weighted_sexual_preferences
from names import get_random_name_by_gender
from hobbies import get_random_hobbies
from fears_and_insecurities import get_random_fears
from markdown_generator import generate_persona_markdown
from surnames import get_random_surname

# New Attribute Modules
from careers_and_finance import get_random_career_profile
from culture_and_geography import get_random_cultural_profile
from social_and_lifestyle import get_random_lifestyle_profile
from coachable_topics import get_tailored_coachable_topics
from skills_and_talents import get_weighted_skills

@dataclass
class Persona:
    name: str
    surname: str
    generation_time: str
    age: int
    gender: str
    sex: str
    orientation: str
    caregiver_style: str
    physical_traits: Dict[str, str]
    personality: Dict[str, str]
    region: str
    kink_preferences: Dict[str, str]
    hobbies: List[str]
    cultural_background: Dict[str, str]
    education: str
    career: str
    social_life: Dict[str, str]
    financial_situation: str
    health: Dict[str, str]
    political_views: str
    life_goals: str
    skills_and_talents: List[str]
    fears_and_insecurities: List[str]
    moral_compass: str
    leisure_activities: List[str]
    fashion_sense: str
    technology_use: str
    coachable_topics: List[str]

class PersonaGenerator:
    def __init__(self):
        random.seed(None)
        self.PERSONALITY_TRAITS = {
            'favorite_colors': ["Blue", "Green", "Red", "Purple", "Yellow", "Black", "Pink"],
            'enneagram_types': [
                {'type': '1 - The Reformer', 'description': 'Principled and perfectionistic', 'core_desire': 'To be good, ethical, and right'},
                {'type': '2 - The Helper', 'description': 'Caring and people-pleasing', 'core_desire': 'To be loved and needed'},
                {'type': '3 - The Achiever', 'description': 'Success-oriented and driven', 'core_desire': 'To be successful and admired'},
                {'type': '4 - The Individualist', 'description': 'Expressive and sensitive', 'core_desire': 'To find themselves and their unique identity'},
                {'type': '5 - The Investigator', 'description': 'Perceptive and secretive', 'core_desire': 'To be competent and knowledgeable'},
                {'type': '6 - The Loyalist', 'description': 'Security-oriented and anxious', 'core_desire': 'To feel secure and supported'},
                {'type': '7 - The Enthusiast', 'description': 'Spontaneous and versatile', 'core_desire': 'To be happy, satisfied, and content'},
                {'type': '8 - The Challenger', 'description': 'Confident and confrontational', 'core_desire': 'To protect themselves and remain in control'},
                {'type': '9 - The Peacemaker', 'description': 'Reassuring and complacent', 'core_desire': 'To have inner stability and peace'}
            ],
            'temperament': ["Introverted", "Extroverted", "Agreeable", "Conscientious", "Neurotic"],
            'emotional_traits': ["Anxious", "Calm", "Empathetic", "Irritable", "Optimistic"],
            'social_behavior': ["Outgoing", "Reserved", "Shy", "Confident"],
            'sense_of_humor': ["Sarcastic", "Dry", "Slapstick", "Witty", "Dark"]
        }
        self.CARE_GIVER_STYLE = [
            'Authoritarian/Firm', 'Nurturing/Empathetic', 'Hands-Off/Detached', 
            'Playful/Engaging', 'Strict/Traditional', 'Overprotective/Cautious', 
            'Encouraging/Motivational', 'Tough Love/No-Nonsense', 'Chaotic/Unpredictable'
        ]
        self.QUIRKS = [
            "Loves knitting", "Always wears mismatched socks", 
            "Talks to plants", "Obsessed with cleanliness"
        ]
        self.COACHABLE_TOPICS = [
            "What long-held dream have you been postponing?", 
            "Are you struggling to break through a personal limitation?",
            "Do you want to improve your ability to set boundaries or have difficult conversations?",
            "How can you create more meaningful impact in your current role?"
        ]

    def generate_persona(self) -> Persona:
        # IDENTITY BLUEPRINT CONFIGURATION
        blueprints = [
            ("cisgender woman", "female", "woman", ["heterosexual", "lesbian", "bisexual", "pansexual"]),
            ("cisgender woman", "female", "woman", ["heterosexual", "lesbian", "bisexual", "pansexual"]),
            ("cisgender woman", "female", "woman", ["heterosexual", "lesbian", "bisexual", "pansexual"]),
            ("cisgender woman", "female", "woman", ["heterosexual", "lesbian", "bisexual", "pansexual"]),
            ("cisgender man", "male", "man", ["heterosexual", "homosexual", "bisexual", "pansexual"]),
            ("transfeminine woman", "male", "woman", ["lesbian", "bisexual", "pansexual", "heterosexual"]),
        ]
        gender, sex, name_lookup_gender, orientation_pool = random.choice(blueprints)
        orientation = random.choice(orientation_pool)
        assigned_age = random.randint(22, 68)
        occupation, financial_situation, education = get_random_career_profile()
        region, region_data, cultural_bg = get_random_cultural_profile()
        social_life, fashion_sense, technology_use = get_random_lifestyle_profile()
        physical = get_random_physical_traits(sex=sex, age=assigned_age)
        enneagram = random.choice(self.PERSONALITY_TRAITS['enneagram_types'])
        sexual_preferences = get_weighted_sexual_preferences(
            orientation=orientation, 
            personality={'enneagram_type': enneagram['type']}
        )
        personality = {
            'siblings': random.randint(0, 4),
            'favorite_color': random.choice(self.PERSONALITY_TRAITS['favorite_colors']),
            'occupation': occupation,
            'enneagram_type': enneagram['type'],
            'enneagram_description': enneagram['description'],
            'temperament': random.choice(self.PERSONALITY_TRAITS['temperament']),
            'emotional_traits': random.choice(self.PERSONALITY_TRAITS['emotional_traits']),
            'social_behavior': random.choice(self.PERSONALITY_TRAITS['social_behavior']),
            'sense_of_humor': random.choice(self.PERSONALITY_TRAITS['sense_of_humor']),
            'quirk': random.choice(self.QUIRKS)
        }

        surname = get_random_surname()
        current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        tailored_topics = get_tailored_coachable_topics(personality, count=2)

        return Persona(
            name=get_random_name_by_gender(name_lookup_gender), 
            surname=surname,
            generation_time=current_timestamp,
            age=assigned_age,
            gender=gender, 
            sex=sex, 
            orientation=orientation,
            caregiver_style=random.choice(self.CARE_GIVER_STYLE), 
            physical_traits=get_random_physical_traits(), 
            personality=personality, 
            region=region, 
            kink_preferences=sexual_preferences, 
            hobbies=get_random_hobbies(2),
            cultural_background=cultural_bg,
            education=education, 
            career=occupation,
            social_life=social_life,
            financial_situation=financial_situation,
            health={
                'Physical Health': random.choice(['Good', 'Fair', 'Poor']), 
                'Mental Health': random.choice(['Good', 'Fair', 'Poor'])
            }, 
            political_views=random.choice(['Liberal', 'Conservative', 'Moderate', 'Independent']), 
            life_goals=random.choice(['Travel the world', 'Achieve financial independence', 'Start a business', 'Find true love', 'Find stability']),
            skills_and_talents=get_weighted_skills(count=2, career=occupation, personality=personality), 
            fears_and_insecurities=get_random_fears(2, personality=personality), 
            moral_compass=random.choice(['Utilitarian', 'Deontological', 'Virtue Ethics', 'Pragmatic']), 
            leisure_activities=random.sample(['Binge-watching TV', 'Reading', 'Gardening', 'Hiking'], k=2), 
            fashion_sense=fashion_sense, 
            technology_use=technology_use,
            coachable_topics=tailored_topics
        )

def save_persona_to_markdown(persona, filename):
    content = generate_persona_markdown(persona)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    generator = PersonaGenerator()
    random_persona = generator.generate_persona()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(script_dir, "md")
    os.makedirs(target_dir, exist_ok=True)
    
    filename = os.path.join(target_dir, f"{random_persona.name}_{random_persona.surname}_persona.md")
    
    save_persona_to_markdown(random_persona, filename)
    print(f"\nSuccess! Generated Local Bio: .{os.sep}{os.path.relpath(filename, script_dir)}")
