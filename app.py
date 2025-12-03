from flask import Flask, render_template, request
from story_inputs import create_story_for_user, winner_story, story_with_golden_word


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    final_story = None 
    error_message = None

    if request.method == "POST":

        name = request.form.get("name").strip()
        noun = request.form.get("noun").strip()
        place = request.form.get("place").strip()
        adjective = request.form.get("adjective").strip()
        animal = request.form.get("animal").strip()
        verb = request.form.get("verb").strip()
        style = request.form.get("style","funny").strip()

        user_inputs = {
            "name": name, 
            "noun": noun,
            "place": place,
            "adjective": adjective,
            "animal": animal,
            "verb": verb,
            "style": style
        }

        if not all(user_inputs.values()):
            error_message = "Please fill in all fields."
            return render_template("index.html", error=error_message)

        golden_winner = winner_story(user_inputs)

        if golden_winner:
            final_story = story_with_golden_word(user_inputs)
        else:
            final_story = create_story_for_user(user_inputs)
        print(final_story)

        return render_template("story.html", final_story=final_story)
    else:
        return render_template("index.html", error = None)

if __name__ == "__main__":
    app.run(debug=True)
