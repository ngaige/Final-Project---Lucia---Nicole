# story_inputs.py

import os 
from dotenv import load_dotenv
from openai import OpenAI

#Load environment variables from .env file
load_dotenv()

#Retrieve OpenAI API key from the environment variables
API_KEY = os.getenv("OPENAI_API_KEY")

#Create the OpenAI client if the API key is available

client = None 
if API_KEY:
    client = OpenAI(api_key=API_KEY)

def create_story_for_user(user_input):
    """Use OpenAI to create a mad libs style story, funny and simple, based on user input."""
    #Safety check to ensure the client is initialized
    if client is None:
        raise ValueError(
            "OpenAI key is not found! Story cannot be created until key is provided."
        )
    #format the user inputs into a string list
    
    word_list = "\n".join([f"{key}: {value}" for key, value in user_input.items()])
    style = user_input.get("style", "funny")
    
    #Prompt sent to the model
    prompt = f"""Create a {style} and simple mad libs style story for children using the following words provided by the user:
        {word_list}
        Rules for the story to follow the Mads Libs style:
        - Needs to be between 5-10 sentences long.
        - Keep it funny, entretaining, simple and appropiate.
        - Use all the words provided by the user in the story.
        - Have no follow up questions or instructions in the story.

        Write the story below:
        """
    #Call the OpenAI API to generate the story
    response = client.responses.create(model="gpt-4o-mini", input=prompt)
    return response.output[0].content[0].text.strip()

def winner_story(name):
   """Generate a special winner story, where if the user gives specific inputs they win the game, unlocking a new golden story."""
   #Extract the generated story
   return (
       f"Congratulations! Golden story unlocked \n\n"
       f"As {name} mentioned the secret winner word 'banana', "
       f"They have proven to be the ultimate story adventurer! "
       f"With the magical word a new portal opened. "
       f"You now have access to multiple funny hilarious stories, unlimited jokes and a guaranteed great time! "
       f"It was a great adventure, {name}! Thank you for playing with us!"
   )

def story_with_golden_word(user_input):
   """Check if the user input contains the golden word to unlock a special story."""
   golden_word = "banana"

#Look through what the user submitted to see if the golden word is present
   for value in user_input.values():
       if value and golden_word in value.lower():
           name = user_input.get("name", "Adventurer")
           return winner_story(name)

#Default story generation if the golden word is not found
   return create_story_for_user(user_input)


#Simpel test to verify the story generation function
if __name__ == "__main__":
   sample_input = {
       "name": "Alice",
       "noun": "cat",
       "place": "park",
       "adjective": "happy",
       "animal": "dog",
       "verb": "run",
   }
   print(create_story_for_user(sample_input))


