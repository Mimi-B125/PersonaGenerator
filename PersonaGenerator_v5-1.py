import random
import os
import time
from typing import List, Dict
from dataclasses import dataclass

# Modular Imports
from physical_traits import get_random_physical_traits
from sexual_preferences import get_random_sexual_preferences
from names import get_random_name_by_gender
from hobbies import get_random_hobbies
from markdown_generator import generate_persona_markdown

@dataclass
class Trait:
    name: str
    description: str
    
@dataclass
class Persona:
    name: str
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
            'occupations': ["Teacher", "Nurse", "Engineer", "Stay-at-home parent", "Chef"],
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
        self.GENDER_AND_SEX = {
            'sex': ["female"],
            'gender_identity': ["woman", "non-binary"],
            'sexual_orientation': ["heterosexual", "lesbian", "bisexual"]
        }    
        self.REGION_OF_ORIGIN = {
            'Northeast': {'Accents': 'Northeast Accents', 'Slang': 'Bubbler, yous guys'},
            'Southeast': {'Accents': 'Southern Accent', 'Slang': 'Y’all, fixin’ to'},
            'Midwest': {'Accents': 'Midwestern English', 'Slang': 'You betcha, pop'},
            'Southwest': {'Accents': 'Southwestern English', 'Slang': 'Hella, dude'},
            'West': {'Accents': 'Western American', 'Slang': 'Gnarly, no worries'},
            'Pacific Northwest': {'Accents': 'Pacific Northwest', 'Slang': 'The 253'},
            'Upper Midwest': {'Accents': 'Upper Midwest', 'Slang': 'Uff da, Dontcha know'}
        }
        self.CARE_GIVER_STYLE = [
            'Authoritarian/Firm', 'Nurturing/Empathetic', 'Hands-Off/Detached', 
            'Playful/Engaging', 'Strict/Traditional', 'Overprotective/Cautious', 
            'Encouraging/Motivational', 'Tough Love/No-Nonsense', 'Chaotic/Unpredictable'
        ]
        self.QUIRKS = (
            Trait("Loves knitting", "Enjoys quiet time knitting blankets."),
            Trait("Afraid of heights", "Gets nervous standing on ladders."),
            Trait("Obsessed with cleanliness", "Always keeps everything spotless.")
        )
        self.SOCIAL_LIFE_AND_RELATIONSHIPS = {
           'relationship_status': [{"Single": "Not in a relationship."}, {"Complicated": "Unresolved boundaries."}],
           'relationship_contentment_level': [{"Happy": "Generally satisfied."}, {"Content": "Comfortable."}],
           'family_dynamics': [{'type': 'Close-knit Family'}, {'type': 'High-conflict Family'}, {'type': 'Absent Caregiver Dynamic'}]
        }
        self.FINANCIAL_SITUATION = {
            'Income level': ["low-income", "middle-class", "wealthy"]
        }
        self.COACHABLE_TOPICS = ["What long-held dream have you been postponing?", "Are you struggling to break through a personal limitation?"]

    def generate_persona(self) -> Persona:
        gender = random.choice(self.GENDER_AND_SEX['gender_identity'])
        enneagram = random.choice(self.PERSONALITY_TRAITS['enneagram_types'])
        region = random.choice(list(self.REGION_OF_ORIGIN.keys()))
        
        personality = {
            'siblings': random.randint(0, 4),
            'favorite_color': random.choice(self.PERSONALITY_TRAITS['favorite_colors']),
            'occupation': random.choice(self.PERSONALITY_TRAITS['occupations']),
            'enneagram_type': enneagram['type'],
            'enneagram_description': enneagram['description'],
            'temperament': random.choice(self.PERSONALITY_TRAITS['temperament']),
            'emotional_traits': random.choice(self.PERSONALITY_TRAITS['emotional_traits']),
            'social_behavior': random.choice(self.PERSONALITY_TRAITS['social_behavior']),
            'sense_of_humor': random.choice(self.PERSONALITY_TRAITS['sense_of_humor'])
        }

        # Safe extraction of dictionary structures
        chosen_status_dict = random.choice(self.SOCIAL_LIFE_AND_RELATIONSHIPS['relationship_status'])
        status_key = list(chosen_status_dict.keys())[0]
        status_desc = chosen_status_dict[status_key]

        chosen_content_dict = random.choice(self.SOCIAL_LIFE_AND_RELATIONSHIPS['relationship_contentment_level'])
        content_key = list(chosen_content_dict.keys())[0]
        content_desc = chosen_content_dict[content_key]

        return Persona(
            name=get_random_name_by_gender(gender), gender=gender, 
            sex=random.choice(self.GENDER_AND_SEX['sex']), orientation=random.choice(self.GENDER_AND_SEX['sexual_orientation']),
            caregiver_style=random.choice(self.CARE_GIVER_STYLE), physical_traits=get_random_physical_traits(),
            personality=personality, region=region, kink_preferences=get_random_sexual_preferences(),
            hobbies=get_random_hobbies(2),
            cultural_background={'ethnicity': 'Caucasian', 'religion': 'Agnostic', 'languages': ['English']},
            education='Bachelor\'s Degree', career=personality['occupation'],
            social_life={
                'Relationship Status': f"{status_key} ({status_desc})",
                'Contentment Level': f"{content_key} ({content_desc})",
                'Family Dynamics': random.choice(self.SOCIAL_LIFE_AND_RELATIONSHIPS['family_dynamics'])['type']
            },
            financial_situation=random.choice(self.FINANCIAL_SITUATION['Income level']),
            health={'Physical Health': 'Good', 'Mental Health': 'Fair'}, political_views='Independent', life_goals='Find stability',
            skills_and_talents=['Writing'], fears_and_insecurities=[random.choice(self.QUIRKS).name],
            moral_compass='Pragmatic', leisure_activities=['Reading'], fashion_sense='Casual', technology_use='Intermediate',
            coachable_topics=random.sample(self.COACHABLE_TOPICS, k=min(2, len(self.COACHABLE_TOPICS)))
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
    
    timestamp = int(time.time())
    filename = os.path.join(target_dir, f"{random_persona.name}_{timestamp}_persona.md")
    
    save_persona_to_markdown(random_persona, filename)
    print(f"\n✨ Generated Local Bio: .{os.sep}{os.path.relpath(filename, script_dir)}")
