from flask import Flask, render_template, request
from story_inputs import create_story_for_user, winner_story, story_with_golden_word


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    final_story = None 
    if request.method == "POST":

        "name": request.form.get("name")
        "noun": request.form.get("noun")
        "place": request.form.get("place")
        "adjective": request.form.get("adjective")
        "animal": request.form.get("animal")
        "verb": request.form.get("verb")
        
        final_story = story_with_golden_word(user_inputs)