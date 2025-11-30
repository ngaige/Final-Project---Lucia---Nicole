#This document focuses on using AI and the users inputs to create engaging stories that follow the mad libs format.

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client= None 
if API_KEY:
    client = OpenAI(api_key=API_KEY)

def create_story_for_user(input_word):
    """Use OpenAI to create a mad libs style story, funny and simple, based on user input."""
    if client is None:
        raise ValueError("OpenAI key is not found! Story cannot be created until key is provided.")
    
    word_list= "\n".join([f"{k}: {v}- {word.strip()}" for k, v in input_word.items()])
    prompt = f"""Create a funny and simple mad libs style story for children using the following words provided by the user:

    User words provided:
    {word_list}
    Rules for the story to follow the Mads Libs style: 
    - Needs to be between 5-10 sentences long.
    - Keep it funny, entretaining, simple and appropiate. 
    - Use all the words provided by the user in the story.
    - Have no follow up questions or instructions in the story.

    write the story below:
    """

    response = client.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages=[ {"role": "user", "content": prompt}], 
        temperature=0.8, 
        max_tokens=300)
    
    return response.choices[0].message.content.strip()

def winner_story(name): 
    """Generate a special winner story, where if the user gives specific inputs they win the game, unlocking a new golden story."""
    return(
        f"Congratulations! Golden story unlocked \n\n"
        f"As {name} mentioned the secret winner word 'bannana', "
        f"they have proven to be the ultimate story adventurer! "
        f"With the magical word a new portal opened. "
        f"You now have access to multiple funny hilarious stories, unlimited jokes and a guaranteed great time! "
        f"It was a great adventure, {name}! Thank you for playing with us!"
    )

def story_with_golden_word(input_word):
    """Check if the user input contains the golden word to unlock a special story."""
    golden_word = "bannana"
    if golden_word in input_word.values():
        return winner_story(input_word.get("name", "Adventurer"))
    else:
        return create_story_for_user(input_word)