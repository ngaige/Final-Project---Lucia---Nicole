# story_inputs.py
"""
Helper functions to create stories from user inputs.
This version does NOT use OpenAI – everything is done with plain Python.
"""

from typing import Dict


def create_story_for_user(user_inputs: Dict[str, str]) -> str:
    """
    Base story using the user's inputs.
    Expects keys: name, noun, place, adjective, animal, verb.
    """
    name = user_inputs.get("name", "Someone")
    noun = user_inputs.get("noun", "object")
    place = user_inputs.get("place", "somewhere")
    adjective = user_inputs.get("adjective", "mysterious")
    animal = user_inputs.get("animal", "animal")
    verb = user_inputs.get("verb", "walked")

    story = (
        f"One {adjective} afternoon, {name} was in {place} carrying a {noun}. "
        f"Out of nowhere, a {adjective} {animal} appeared and {verb} right past them. "
        f"{name} wasn’t sure if it was real or just their imagination, "
        f"but from that day on, every time they saw a {animal}, "
        f"they remembered that strange moment in {place}."
    )

    return story


def winner_story(user_inputs: Dict[str, str]) -> bool:
    """
    Simple 'winner' condition.
    For now: if the golden_word is provided and has at least 5 characters,
    we treat it as a 'winner' and unlock the special golden story.
    """
    golden_word = user_inputs.get("golden_word", "").strip()
    return len(golden_word) >= 5


def story_with_golden_word(user_inputs: Dict[str, str]) -> str:
    """
    Story that highlights the user's golden word if they 'win'.
    Reuses the base story and adds a special sentence.
    """
    base_story = create_story_for_user(user_inputs)
    golden_word = user_inputs.get("golden_word", "").strip()
    place = user_inputs.get("place", "that place")

    if golden_word:
        extra_line = (
            f"\n\nEveryone in {place} soon started calling that day "
            f'the "{golden_word}" day, because nothing felt normal after it.'
        )
    else:
        extra_line = (
            "\n\nPeople in town later said that day changed something, "
            "even if nobody could explain exactly what."
        )

    return base_story + extra_line
