# prompt_builder.py
import random
from exposures import TONES

PARAGRAPH_DISTRIBUTION = [
    (4, 0.55),
    (5, 0.35),
    (6, 0.10),
]

def sample_paragraph_count():
    values, weights = zip(*PARAGRAPH_DISTRIBUTION)
    return random.choices(values, weights, k=1)[0]


def format_features(features: dict) -> str:
    items = list(features.values())
    
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    
    return ", ".join(items[:-1]) + ", and " + items[-1]


def build_prompt(
    name,
    gender,
    location,
    exposure,
    exposure_key,
    features,
    verb,
    noun,
    adjective,
    tone_key
):


    exposure_goal = exposure["exposure_goal"]

    max_paragraphs = sample_paragraph_count()

    min_paragraphs = 3
    if max_paragraphs == 6:
        min_paragraphs = 4

    if features:
        formatted_features = format_features(features)
        features_text = f"The story should {formatted_features}."
    else:
        features_text = ""

    goal_text = f"exposes {name} to {exposure_goal}."

    tone = TONES[tone_key]
    tone_label = tone["label"]
    tone_behaviors = "\n".join(f"- {b}" for b in tone["behaviors"])

    prompt = f"""
You are a children’s short story writer. Your stories are coherent and engaging while introducing new topics to 3-year-old children.

Write a short story ({min_paragraphs}-{max_paragraphs} paragraphs) about a 3-year-old {gender} named {name}.
The story is set {location} and {goal_text}

Tone: {tone_label}
Tone behaviors:
{tone_behaviors}

In the story, try to use the verb "{verb}", the noun "{noun}" and the adjective "{adjective}" at some point.
{features_text}

Only use plain text, no markdown formatting. The story should be appropriate for a 3-year-old child.
""".strip()

    return {
        "metadata": {
            "name": name,
            "gender": gender,
            "location": location,
            "exposure": exposure_key,
            "features": list(features.keys()),
            "verb": verb,
            "noun": noun,
            "adjective": adjective,
            "tone": tone_key,
        },
        "prompt": prompt
    }
