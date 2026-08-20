import random
from typing import Dict

KINK_DICT = {
    "BDSM": ["Bondage", "Discipline", "Dominance", "Submission", "Sadism", "Masochism", "Power Dynamics"],
    "Chastity Play": ["Chastity Cages", "'Keyholder' Dynamics", "Orgasm Denial", "Long-Term Lock-Up", "Tease and Denial", "Remote-Controlled Devices", "Cuckolding with Chastity"],
    "Power Exchange": ["Master/Slave Dynamics", "24/7 D/s Relationships", "Service Submission", "Protocol-Based Relationships", "Collaring Ceremonies", "Financial Domination (Findom)", "Obedience Training"],
    "Erotic Humiliation": ["Verbal Degradation", "Public Embarrassment", "Cuckolding", "SPH (Small Penis Humiliation)", "Forced Feminization", "'Slut'-Shaming Roleplay", "Writing Lines as Punishment"],
    "Corner Time": ["Disciplinary Punishment", "'Time-Out' Scenarios", "Psychological Control", "Standing in Silence", "Facing a Wall or Corner Naked", "'Thinking Time' Roleplay Punishment", "Physical Restrictions (e.g., Holding Something)"],
    "Impact Play": ["Spanking", "Whipping", "Flogging", "Caning", "Paddling", "Riding Crops", "Switching (Roles)"],
    "Electrostimulation": ["Violet Wand", "E-Stim Pads", "TENS Unit", "Erotic Shocks on Genitals", "Sensation Play with Electricity", "Remote-Controlled Shocks", "Edge Play with Safety Precautions"],
    "Sensory Deprivation": ["Blindfolds", "Earplugs/Headphones", "Hood Play", "Mummification", "Deprivation Tanks", "Gags (e.g., Ball Gags)", "Temperature Play (e.g., Ice or Heat)"],
    "Breath Play": ["Choking", "Bag Over Head", "Hand Over Mouth", "Plastic Wrap Play", "Controlled Breath Control Devices", "Gas Masks", "Exhalation Control by a Partner"],
    "Knife Play": ["Fear Play with Blades", "Controlled Skin Contact", "Scraping the Skin", "Cold Metal Sensation Play", "Edge Play with Sharp Objects", "Using Knives for Psychological Intensity", "Wax Cutting or Rope Cutting Scenes"],
    "Roleplay": ["Doctor/Patient", "Boss/Employee", "'Captured and Interrogated' Dynamics", "'Fantasy Creatures' (e.g., Vampires, Aliens)"],
    "Primal Play": ["Animal Roleplay", "Growling/Snarling", "Non-Verbal Communication", "Wrestling or Physical Dominance Displays", "Biting/Scratching During Scenes", "Predator/Prey Dynamics", "Howling or Animalistic Sounds"],
    "Foot Fetish": ["Toe Sucking", "Foot Worship", "High Heels", "Foot Smelling/Sniffing", "Trampling (Feet on Body)", "Pedicures as Rituals", "Stockings or Socks Fetish"],
    "Nylon Kink": ["Pantyhose", "Fishnets", "Garters", "Stockings with Heels", "Tearing Nylon During Scenes", "Worshipping Nylon-Clad Legs", "Encasement in Nylon"],
    "Cross-Dressing": ["Wearing Opposite Gender Clothing for Arousal", "Makeup Application as Part of Roleplay", "Wig Wearing for Transformation Fantasies", "Feminization Through Clothing Choices", "Gender-Bending Costumes in Scenes", "Public Cross-Dressing Challenges (Consensual)", "Exploring Gender Identity Through Dress-Up"],
    "Pregnancy Fetish": ["Arousal from Visible Pregnancy", "'Pregnant Lover' Scenarios", "Pregnancy Worship", "Belly Touching or Rubbing Fetishes", "Impregnation Fantasies (Real or Simulated)", "Lactation as Part of Pregnancy Fetishism", "Admiration of 'Fertility Goddess' Imagery"],
    "Lactation Fetish": ["Breast Milk Consumption", "'Nursing' Roleplay", "Milk-Inducing Toys or Techniques", "Milking Machines for Lactation Scenes", "Breast Worship with Lactation Focused Play", "Hucow Roleplay Integration in Lactation Scenes", "Feeding a Partner Breast Milk"],
    "Exhibitionism": ["Public Nudity", "Performing in Front of Others", "Wearing Revealing Clothing in Public Spaces (Consensually)", "Flashing (Consensual)", "Being Watched During Intimate Acts (Consensual)", "Outdoor Sex Fantasies (Private Locations)", "Webcam Performances for an Audience"],
    "Voyeurism": ["Watching Consensual Acts", "Attending Sex Parties as an Observer Only", "Peeping Tom Fantasies (Consensual)", "Watching Porn with a Partner as Foreplay", "Watching Through Windows/Doors (Staged Scenes)", "Observing Others Undress (Consensual)", "Erotic Watching Without Participating"],
    "Tickling (Knismolagnia)": ["Feathers", "Tied Down Tickling", "Light Fingertip Touches to Sensitive Areas", "Tickling With Restraints on Feet or Arms", "Electric Toothbrushes for Sensation Play", "Forced Laughter as Part of Scenes", "Tickling as a Form of Teasing or Torture"],
    "Golden Showers": ["Peeing on Partner", "Being Peed On", "Peeing in Controlled Spaces (e.g., Shower)", "Marking Partner with Urine", "Drinking Urine (Consensual)", "Peeing as a Dominance Display", "Incorporating Pee Play into D/s Dynamics"],
    "Hucow Roleplay": ["Milking Machines", "'Human Cow' Roleplay", "Lactation Induction", "Cowbells and Collars as Props", "Feeding Partner Milk (Real or Simulated)", "Breast Worship in Hucow Contexts", "Animalistic Behavior (e.g., Mooing, Crawling)"],
    "SPH (Small Penis Humiliation)": ["Verbal Teasing About Size", "Comparison to Larger Partners", "Embarrassment in Size-Based Scenarios", "'Measuring' Roleplay", "Mockery During Sexual Acts", "'Shrinking' Fantasies or Hypnosis Play", "Public or Group Humiliation (Consensual)"],
    "Breeding Kink": ["Impregnation Roleplay", "'Put a Baby in Me' Fantasies", "Alien Egg Implantation (Ovipositors)", "Risk of Pregnancy Scenarios (Consensual Fantasy)", "Erotic Focus on Fertility and Reproduction", "'Cum-Inflation' Fantasies (Simulated)", "'Multiple Partner Breeding Play"],
    "Rope Bondage": ["Shibari", "Kinbaku", "Full Body Harnesses", "Suspension Bondage Techniques", "Decorative Rope Patterns on the Skin", "Partial Restraint Scenes (e.g., Hands Only)", "Rope Burn as a Sensation Play Element"],
    "Corsetry/Tight-Lacing": ["Waist Training", "Breath-Restricting Corsets", "Victorian Aesthetic Roleplay", "'Dollification' Through Corset Use", "'Tight-Lace Punishment' Dynamics in D/s Play", "Corset Fetishism for Aesthetic Appeal", "'Training' to Endure Tight Lacing Over Time"],
    "Fisting": ["Anal Fisting", "Vaginal Fisting with Proper Technique", "Stretching Toys for Preparation", "'Slow and Gentle' Fisting Dynamics for Safety", "'Punch Fisting' for Advanced Players (Risk-Aware)", "'Double Fisting' Scenarios (Advanced)", "'Aftercare Focus' Due to Intensity of Play"],
    "Objectification": ["Sex Doll Roleplay", "'Furniture Objectification' (e.g., Human Chair/Table)", "'Pet Objectification' (e.g., Being Treated Like an Animal)", "'Dehumanization' Scenarios in D/s Play", "'Mannequin Roleplay'", "'Human Ashtray' Scenarios", "'Being Used as a Tool or Prop in Scenes"],
    "Primal Fear Play": ["Chase-and-Capture Dynamics", "'Hunted Prey' Scenarios", "Growling/Snarling with Intent to Intimidate", "Use of Natural Settings for Scenes (e.g., Forests)", "Non-Verbal Communication During Fear Play", "Scratching/Biting to Simulate Predatory Behavior", "'Fear-Induced Adrenaline Rush as a Turn-On'"]
}

def get_random_sexual_preferences() -> Dict[str, str]:
    selected_kinks = random.sample(list(KINK_DICT.keys()), k=min(2, len(KINK_DICT)))
    return {kink: random.choice(KINK_DICT[kink]) for kink in selected_kinks}
