from flask import Flask, render_template, request
from story_inputs import create_story_for_user, winner_story, story_with_golden_word

import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    final_story = None
    error_message = None
    prefill = {}

    if request.method == "POST":
        # If user clicked the "Surprise me" button
        if request.form.get("random_story") == "1":
            names = ["Lucia", "Nicole", "Alex", "Sam", "Jordan"]
            nouns = ["notebook", "ring", "ticket", "camera", "coffee cup"]
            places = ["Paris", "New York", "Rome", "Tokyo", "Boston"]
            adjectives = ["mysterious", "sparkling", "chaotic", "quiet", "lucky"]
            animals = ["cat", "tiger", "owl", "dolphin", "fox"]
            verbs = ["danced", "vanished", "whispered", "appeared", "glowed"]
            golden_words = ["serendipity", "destiny", "chaos", "fortune", "magic"]

            user_inputs = {
                "name": random.choice(names),
                "noun": random.choice(nouns),
                "place": random.choice(places),
                "adjective": random.choice(adjectives),
                "animal": random.choice(animals),
                "verb": random.choice(verbs),
                "golden_word": random.choice(golden_words),
            }

            final_story = story_with_golden_word(user_inputs)
            # We don't prefill the form for surprise stories
            return render_template(
                "index.html",
                final_story=final_story,
                error_message=error_message,
                prefill={},
            )

        # Otherwise, use the values the user typed
        fields = ["name", "noun", "place", "adjective", "animal", "verb", "golden_word"]
        user_inputs = {f: request.form.get(f, "").strip() for f in fields}
        prefill = user_inputs.copy()

        required_values = [
            user_inputs["name"],
            user_inputs["noun"],
            user_inputs["place"],
            user_inputs["adjective"],
            user_inputs["animal"],
            user_inputs["verb"],
        ]

        if any(not v for v in required_values):
            error_message = "Please fill in all required fields before generating your story."
        else:
            if winner_story(user_inputs):
                final_story = story_with_golden_word(user_inputs)
            else:
                final_story = create_story_for_user(user_inputs)

    return render_template(
        "index.html",
        final_story=final_story,
        error_message=error_message,
        prefill=prefill,
    )


if __name__ == "__main__":
    app.run(debug=True)
