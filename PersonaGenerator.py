import random
import os
import time
from typing import List, Dict
from dataclasses import dataclass

# Attribute Modules
from physical_traits import get_random_physical_traits
from sexual_preferences import get_weighted_sexual_preferences
from names import get_random_name_by_gender
from hobbies import get_random_hobbies
from fears_and_insecurities import get_random_fears
from fears_and_insecurities import get_body_perception_narrative
from markdown_generator import generate_persona_markdown
from surnames import get_random_surname
from careers_and_finance import get_random_career_profile
from culture_and_geography import get_random_cultural_profile
from social_and_lifestyle import get_random_lifestyle_profile
from coachable_topics import get_tailored_coachable_topics
from skills_and_talents import get_weighted_skills
from health_profiles import get_contextual_health_profile
from caregiver_profiles import get_contextual_caregiver_style
from moral_compass import get_contextual_moral_compass
from enneagram_psychodynamics import generate_enneagram_psychodynamics
from quirks import get_contextual_quirk

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
    quirks: Dict[str, str]
    moral_compass: str
    leisure_activities: List[str]
    fashion_sense: str
    technology_use: str
    coachable_topics: List[str]
    enneagram_psychodynamics: Dict[str, str]

class PersonaGenerator:
    def __init__(self):
        random.seed(None)
        self.PERSONALITY_TRAITS = {
            'favorite_colors': ["Blue", "Green", "Red", "Purple", "Yellow", "Black", "Pink"],
            'temperament': ["Introverted", "Extroverted", "Agreeable", "Conscientious", "Neurotic"],
            'emotional_traits': ["Anxious", "Calm", "Empathetic", "Irritable", "Optimistic"],
            'social_behavior': ["Outgoing", "Reserved", "Shy", "Confident"],
            'sense_of_humor': ["Sarcastic", "Dry", "Slapstick", "Witty", "Dark"]
        }

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

        # ENVIRONMENT & LIFESTYLE GENERATION
        occupation, financial_situation, education = get_random_career_profile()
        region, region_data, cultural_bg = get_random_cultural_profile()
        social_life, fashion_sense, technology_use = get_random_lifestyle_profile()

        # PHYSICAL GENERATION
        physical = get_random_physical_traits(
            gender_identity=gender, 
            sex=sex, 
            age=assigned_age, 
            fashion_sense=fashion_sense
        )

        # PERSONALITY BASE INITIALIZATION (Sequential Upstream Anchor)
        enneagram_key = str(random.randint(1, 9))
        temperament_choice = random.choice(self.PERSONALITY_TRAITS['temperament'])     
        
        personality = {
            'enneagram_type': enneagram_key,
            'siblings': str(random.randint(0, 4)),
            'favorite_color': random.choice(self.PERSONALITY_TRAITS['favorite_colors']),
            'occupation': occupation,
            'temperament': temperament_choice,
            'emotional_traits': random.choice(self.PERSONALITY_TRAITS['emotional_traits']),
            'social_behavior': random.choice(self.PERSONALITY_TRAITS['social_behavior']),
            'sense_of_humor': random.choice(self.PERSONALITY_TRAITS['sense_of_humor']),
            'quirk': ""
        }

        # PSYCHODYNAMIC LAYER GENERATION
        psychodynamics = generate_enneagram_psychodynamics(
            enneagram_type=personality['enneagram_type'],
            temperament=personality['temperament'],
            age=assigned_age,
            biological_sex=sex
        )
        
        # CROSS-REFERENCE BODILY PERCEPTION
        personality['body_image_perception'] = get_body_perception_narrative(personality, physical)

        # SEX PREFERENCES & KINK PROFILE GENERATION
        sexual_preferences = get_weighted_sexual_preferences(
            orientation=orientation, 
            personality=personality,
            age=assigned_age,
            sex=sex
        )
        
        surname = get_random_surname()
        current_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        tailored_topics = get_tailored_coachable_topics(personality, count=2)

        # HEALTH & WELLNESS GENERATION
        health_data = get_contextual_health_profile(
            age=assigned_age,
            career=occupation,
            personality=personality,
            social_life=social_life,
            physical_traits=physical 
        )

        # QUIRKS GENERATION (Cross-referenced with Upstream Anchors)
        quirk_data = get_contextual_quirk(
            personality=personality,
            health_data=health_data,
            age=assigned_age,
            biological_sex=sex
        )
        personality['quirk'] = quirk_data.get("Private Quirks & Compulsions", "")
        
        chosen_morals = get_contextual_moral_compass(personality)
        caregiver_profile = get_contextual_caregiver_style(personality, chosen_morals)

        return Persona(
            name=get_random_name_by_gender(name_lookup_gender), 
            surname=surname,
            generation_time=current_timestamp,
            age=assigned_age,
            gender=gender, 
            sex=sex, 
            orientation=orientation,
            caregiver_style=caregiver_profile,
            physical_traits=physical, 
            personality=personality, 
            region=region, 
            kink_preferences=sexual_preferences, 
            hobbies=get_random_hobbies(2),
            cultural_background=cultural_bg,
            education=education, 
            career=occupation,
            social_life=social_life,
            financial_situation=financial_situation,
            health=health_data, 
            political_views=random.choice(['Liberal', 'Conservative', 'Moderate', 'Independent']), 
            life_goals=random.choice(['Travel the world', 'Achieve financial independence', 'Start a business', 'Find true love', 'Find stability']),
            skills_and_talents=get_weighted_skills(count=2, career=occupation, personality=personality), 
            fears_and_insecurities=get_random_fears(2, personality=personality),
            quirks=quirk_data,
            moral_compass=chosen_morals, 
            leisure_activities=random.sample(['Binge-watching TV', 'Reading', 'Gardening', 'Hiking'], k=2), 
            fashion_sense=fashion_sense, 
            technology_use=technology_use,
            coachable_topics=tailored_topics,
            enneagram_psychodynamics=psychodynamics
        )

def save_persona_to_markdown(persona, filename):
    content = generate_persona_markdown(persona)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    generator = PersonaGenerator()
    
    # Establish local filesystem directories
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_dir = os.path.join(script_dir, "md")
    os.makedirs(target_dir, exist_ok=True)
    
    # User loop parameter query
    try:
        user_input = input("Enter the number of personas to generate [Default: 1]: ").strip()
        count = int(user_input) if user_input else 1
        if count < 1:
            count = 1
    except ValueError:
        print("Invalid input detected. Defaulting to 1 persona profile.")
        count = 1

    print(f"\nInitializing bulk generation suite: Processing {count} identities...")
    
    for i in range(count):
        random_persona = generator.generate_persona()
        filename = os.path.join(target_dir, f"{random_persona.name}_{random_persona.surname}_persona.md")
        
        save_persona_to_markdown(random_persona, filename)
        
        # Display clean progress markers per creation
        print(f" [{i+1}/{count}] Generated: {random_persona.name} {random_persona.surname}")
        
    print(f"\nExecution Complete! Created markdown records inside directory: .{os.sep}md")