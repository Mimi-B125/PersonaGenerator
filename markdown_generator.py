def generate_persona_markdown(persona) -> str:
    markdown = f"# Persona: {persona.name}\n\n"
    
    markdown += "## Physical Traits\n"
    for trait, value in persona.physical_traits.items():
        markdown += f"- **{trait.capitalize()}:** {value}\n"
    
    markdown += "\n## Personality Traits\n"
    for trait, value in persona.personality.items():
        markdown += f"- **{trait.capitalize()}:** {value}\n"
    
    markdown += f"\n- **Caregiver Style:** {persona.caregiver_style}\n"
    
    markdown += "\n## Gender and Biological Sex\n"
    markdown += f"- **Gender Identity:** {persona.gender}\n"
    markdown += f"- **Sex:** {persona.sex}\n"
    markdown += f"- **Sexual Orientation:** {persona.orientation}\n"
    
    markdown += f"\n## Region of Origin\n- **Region:** {persona.region}\n"
    
    markdown += "\n## Kink Preferences\n"
    for kink, description in persona.kink_preferences.items():
        markdown += f"- **{kink.capitalize()}:** {description}\n"
    
    markdown += "\n## Hobbies\n"
    for hobby in persona.hobbies:
        markdown += f"- {hobby}\n"

    markdown += "\n## Cultural Background\n"
    for key, value in persona.cultural_background.items():
        markdown += f"- **{key.capitalize()}:** {value}\n"

    markdown += f"\n## Education and Career\n- **Education:** {persona.education}\n- **Career:** {persona.career}\n"

    markdown += "\n## Social Life\n"
    for key, value in persona.social_life.items():
        markdown += f"- **{key.capitalize()}:** {value}\n"

    markdown += f"\n## Financial Situation\n- **Income Level:** {persona.financial_situation}\n"

    markdown += "\n## Health\n"
    for key, value in persona.health.items():
        markdown += f"- **{key.capitalize()}:** {value}\n"

    markdown += f"\n## Political Views and Life Goals\n- **Political Views:** {persona.political_views}\n- **Life Goals:** {persona.life_goals}\n"

    markdown += "\n## Skills and Talents\n"
    for skill in persona.skills_and_talents:
        markdown += f"- {skill}\n"

    markdown += "\n## Fears and Insecurities\n"
    for fear in persona.fears_and_insecurities:
        markdown += f"- {fear}\n"

    markdown += f"\n## Moral Compass\n- **Moral Compass:** {persona.moral_compass}\n"

    markdown += "\n## Leisure Activities\n"
    for activity in persona.leisure_activities:
        markdown += f"- {activity}\n"

    markdown += "\n## Coachable Topics\n"
    for topic in persona.coachable_topics:
        markdown += f"- {topic}\n"

    markdown += f"\n## Fashion Sense & Tech Use\n- **Fashion:** {persona.fashion_sense}\n- **Tech Use:** {persona.technology_use}\n"
    return markdown
