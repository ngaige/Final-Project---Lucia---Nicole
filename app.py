from flask import Flask, render_template, request
from story_inputs import create_story_for_user, story_with_golden_word

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/start", methods=["GET"])
def start():
    return render_template("index.html")


@app.route("/story", methods=["POST"])
def story():
    # Get form data
    user_input = {
        "name": request.form.get("name"),
        "noun": request.form.get("noun"),
        "place": request.form.get("place"),
        "adjective": request.form.get("adjective"),
        "verb": request.form.get("verb"),
        "animal": request.form.get("animal"),
        "verb_past": request.form.get("verb_past"),
        "golden_word": request.form.get("golden_word", "").strip(),
        "story_option": request.form.get("story_option", "funny"),
        }

    story_text = story_with_golden_word(user_input)
    return render_template("story.html", story=story_text)

if __name__ == "__main__":
    app.run(debug=True)

