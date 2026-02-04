from scenes import SCENES
from names import get_name

EXPOSURES = {
    "number_words": {
        "min_tier": 0,
        "max_tier": 0,
        "description": "rote number words"
    },

    "object_categories": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "animals, toys, foods"
    },

    "time_words": {
        "min_tier": 1,
        "max_tier": 2,
        "description": "yesterday, today, tomorrow"
    },

    "social_rules": {
        "min_tier": 1,
        "max_tier": 3,
        "description": "turn-taking, fairness"
    }
}


def tier_allows_content(tier_data, content_type):
    if content_type == "exposure":
        return True
    if content_type == "conditioning":
        return tier_data["capabilities"]["learning"]
    if content_type == "skill":
        return tier_data["capabilities"]["multi_step_reasoning"]
    return False


def generate_exposure_prompts(tier_data):
    prompts = []

    for scene_id, scene in SCENES.items():
        if not (scene["min_tier"] <= tier_data["id"] <= scene["max_tier"]):
            continue

        if not tier_allows_content(tier_data, scene["content_type"]):
            continue

        print("passed checks")

        for location in ["home", "playground", "school"]:
            name = get_name()
            prompt = build_exposure_prompt(
                tier_data,
                scene,
                name,
                location
            )
            print(prompt)
            prompts.append(prompt)

    return prompts


def build_exposure_prompt(tier_data, scene, name, location):
    constraints = []

    limits = tier_data["limits"]
    constraints.append(f"- Max {limits['max_sentences']} sentences")
    constraints.append(f"- Max {limits['max_sentence_length']} words per sentence")
    constraints.append("- Use present tense only")
    constraints.append("- No dialogue")
    constraints.append("- No questions")

    constraints.append(
        "- Only use these verbs: " + ", ".join(scene["allowed_verbs"])
    )
    constraints.append(
        "- Only use these nouns: " + ", ".join(scene["allowed_nouns"])
    )

    constraints.append("- Do not describe learning or change over time")
    constraints.append("- Use concrete, observable actions only")

    constraints_text = "\n".join(constraints)

    return f"""
You are generating a short scene for a machine learning dataset.

TARGET AGE:
Approximate age: {tier_data['approx_age']}

CHARACTER:
- Main character: {name}

SETTING:
- Location: {location}

SCENE:
{scene['description']}

CONSTRAINTS:
{constraints_text}

OUTPUT:
Write only the scene text.
""".strip()
