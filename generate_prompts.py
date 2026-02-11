# generate_prompts.py

from prompt_builder import build_prompt
from names import get_name
from exposures import EXPOSURES, TONES
import random
import json


def load_lexicon():
    with open('D:\Tiny Models\Tiny Stories\lexicon.json') as f:
        lexicon = json.load(f)
    return lexicon

FEATURES = {
    "dialogue": "include dialogue",
    "problem_and_solution": "include a problem and solution",
    "moral_or_lesson": "include a moral or lesson",
    "clear_structure": "include a clear beginning, middle, and end",
    "repetition_for_emphasis": "include repetition for emphasis",
    "sensory_details": "include sensory details",
    "humor": "include humor",
    "twist_or_surprise": "include a twist or surprise",
    "positive_message": "include a positive message",
}
GENDERS = ['girl', 'boy']

def sample_features(features: dict) -> dict:
    k = random.randint(0, min(3, len(features)))
    selected_keys = random.sample(list(features.keys()), k)
    return {key: features[key] for key in selected_keys}

def save_prompts(prompts, output_path):
    with open(output_path, 'w') as f:
        json.dump(prompts, f, indent=2)

def generate_prompts(
        num_prompts=100
):
    prompts = []

    lexicon = load_lexicon()
    adjectives = lexicon["adjectives"]
    nouns = lexicon["nouns"]
    verbs = lexicon["verbs"]

    for _ in range(num_prompts):
        gender = random.choice(GENDERS)
        for exposure in EXPOSURES.items():
            for location in exposure[1]["locations"]:

                verb = random.choice(verbs)
                noun = random.choice(nouns)
                adjective = random.choice(adjectives)
                name = get_name(gender)
                features = sample_features(FEATURES)
                tone_key = random.choice([k for k in TONES.keys() if k not in exposure[1]["banned_tones"]])     
                result = build_prompt(name, gender, location, exposure, features, verb, noun, adjective, tone_key)
                prompts.append(result)
    return prompts


if __name__ == "__main__":
    prompts = generate_prompts()

    print(f"Generated {len(prompts)} prompts.")

    # # Print example
    # example = prompts[0]
    # # print("METADATA:", example["metadata"])
    # print("\nPROMPT:\n")
    # print(example["prompt"])

    # print 5 random prompts
    print("\nRANDOM PROMPTS:\n")
    for _ in range(5):
        random_prompt = random.choice(prompts)
        print(random_prompt["prompt"])
        print("\n---\n")

    # Save to file
    save_prompts(prompts, 'generated_prompts.json')
