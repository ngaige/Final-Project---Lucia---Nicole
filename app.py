from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Just show the form
    return render_template("index.html")


@app.route("/story", methods=["POST"])
def story():
    # Get form data
    name = request.form.get("name")
    noun = request.form.get("noun")
    place = request.form.get("place")
    adjective = request.form.get("adjective")
    verb = request.form.get("verb")
    animal = request.form.get("animal")
    verb_past = request.form.get("verb_past")
    golden_word = request.form.get("golden_word", "")
    story_option = request.form.get("story_option")

    # Choose story based on dropdown
    if story_option == "adventure":
        story_text = (
            f"One {adjective} day at {place}, {name} decided to {verb} like a brave {animal}. "
            f"Everyone watched in awe as {name} {verb_past} across the scene, "
            f"proving that even an ordinary {noun} can turn into an extraordinary adventure. "
            f"{golden_word.capitalize()+'!' if golden_word else ''}"
        )

    elif story_option == "mystery":
        story_text = (
            f"Late at night at {place}, {name} noticed a mysterious {noun} glowing in the corner. "
            f"The {animal} statue seemed to move every time {name} would {verb}. "
            f"When {name} finally {verb_past}, the secret was revealed: "
            f"this mystery had been a test of courage all along. "
            f"{golden_word.capitalize()+'...' if golden_word else ''}"
        )

    elif story_option == "fairytale":
        story_text = (
            f"Once upon a time in {place}, there lived {name}, a {adjective} dreamer "
            f"who carried a tiny {noun} everywhere. With their trusty {animal} companion, "
            f"{name} would {verb} each day until one afternoon they unexpectedly {verb_past}. "
            f"The kingdom whispered forever after: {golden_word or 'magic'}."
        )

    elif story_option == "influence":
        story_text = (
            f"{name} arrived at {place} holding a {adjective} {noun} and an unshakeable presence. "
            f"While others tried to {verb}, {name} naturally stood out — "
            f"the kind of confidence even a {animal} would admire. "
            f"By the time {name} {verb_past}, the entire room felt transformed, "
            f"as if influence itself had walked in. "
            f"{golden_word.capitalize() if golden_word else 'Influence'}."
        )

    else:
        story_text = (
            f"{name} went to {place} with a {adjective} {noun}. "
            f"They decided to {verb} with a {animal}, and later they {verb_past}. "
            f"{golden_word.capitalize() if golden_word else ''}"
        )

    # Render the story on a separate page
    return render_template("story.html", story=story_text)


if __name__ == "__main__":
    app.run(debug=True)

