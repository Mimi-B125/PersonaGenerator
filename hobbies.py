import random
from typing import List

HOBBIES_LIST = [
    "Reading books", "Gardening", "Cooking", "Hiking", "Backpacking",
    "Cycling", "Photography", "Knitting", "Writing", "Fishing", "Rock Climbing",
    "Bird Watching", "Pottery", "Dancing", "Yoga", "Meditation", 
    "Playing musical instruments (e.g., guitar, piano)", 
    "Collecting (e.g., stamps, coins, vintage items)",
    "Gaming (video games or board games)", "Sewing or Quilting", 
    "Calligraphy or Typography", "Traveling and exploring new cultures",
    "Camping", "Surfing or Kayaking", "Martial Arts", 
    "Volunteering for community service", "Learning new languages",
    "DIY Projects or Woodworking", "Baking and experimenting with recipes",
    "Stargazing or Astronomy", "Scrapbooking or Collage Making",
    "Fitness training or Bodybuilding", "Watching movies and reviewing them",
    "Blogging or Vlogging", "LARPing (Live Action Roleplaying)",
    "Aquascaping (underwater gardening)", "Rock Tumbling or Lapidary",
    "Flower Arranging or Floral Design"
]

def get_random_hobbies(count: int = 2) -> List[str]:
    return random.sample(HOBBIES_LIST, k=min(count, len(HOBBIES_LIST)))
