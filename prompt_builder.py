# prompt_builder.py

import random
from typing import Dict
from curriculum import TIERS, TIER_PROFILES
from skills import SKILLS, build_skill_constraints
from capabilities import check_capability_compatibility
from names import NAMES

TONES = [
    "The tone should be calm and simple.",
    "The tone should show curiosity.",
    "The tone should show gentle effort and learning."
]

def merge_lists(*lists):
    result = []
    for lst in lists:
        if lst:
            result.extend(lst)
    return sorted(set(result))


def enforce_capability_bounds(phase, tier):
    required = phase.get("requires_capabilities", {})
    for cap, needed in required.items():
        if needed and not tier["capabilities"].get(cap, False):
            raise ValueError(
                f"Phase requires capability '{cap}' not allowed by tier {tier['id']}"
            )


def collect_constraints(tier_data, profile, phase_data):
    constraints = []

    limits = tier_data["limits"]
    language = tier_data["language"]
    forbidden = tier_data.get("forbidden_words", [])

    constraints.append(f"- Max {limits['max_sentences']} sentences")
    constraints.append(f"- Max {limits['max_sentence_length']} words per sentence")

    if language["tense"] == "present_only":
        constraints.append("- Use present tense only")

    if not language.get("allow_dialogue", True):
        constraints.append("- No dialogue")

    if not language.get("allow_questions", True):
        constraints.append("- No questions")

    # if forbidden:
    #     constraints.append(
    #         "- Do NOT use these words: " + ", ".join(forbidden)
    #     )

    # Profile surface constraints
    surface = profile.get("surface_constraints", {})
    if surface.get("ban_numbers"):
        constraints.append("- Do not use numbers")

    if "allowed_verbs" in surface:
        constraints.append(
            "- Only use these verbs: " + ", ".join(surface["allowed_verbs"])
        )

    if "allowed_nouns" in surface:
        constraints.append(
            "- Only use these nouns: " + ", ".join(surface["allowed_nouns"])
        )

    # Phase constraints
    if phase_data:
        phase_surface = phase_data.get("surface_constraints", {})
        if phase_surface.get("forbid_internal_states_of_others"):
            constraints.append("- Do not describe thoughts or feelings of other characters")

        if "allowed_actions" in phase_surface:
            constraints.append(
                "- Only describe these actions: " + ", ".join(phase_surface["allowed_actions"])
            )

    return constraints




def format_story_beats(beats):
    return "\n".join(
        f"{i + 1}. {beat.upper()}" for i, beat in enumerate(beats)
    )


def build_prompt(tier_data, profile, arc, skill, phase_data, name, location):
    constraints = collect_constraints(tier_data, profile, phase_data)
    constraints_text = "\n".join(constraints)


    structure = arc.get("structure", [])

    structure_text = ""
    if structure:
        structure_text = "STRUCTURE (in order):\n"
        for step in structure:
            structure_text += f"- {step}\n"


    goal_text = ""
    if arc["arc_type"] != "exposure":
        goal_text = f"GOAL:\nShow a child learning to {phase_data['goal']}.\n"     

    prompt = f"""
You are generating a short story for a machine learning dataset.

TARGET AGE:
Approximate age: {tier_data['approx_age']}

{goal_text}

CHARACTER:
- Main character: {name}

SETTING:
- Location: {location}
- Objects may include: {", ".join(arc.get("objects", []))}

{structure_text}

CONSTRAINTS:
{constraints_text}

OUTPUT:
Write only the story text.
""".strip()

    print(prompt)

    return prompt

        

    # # Merge constraints
    # constraints = merge_constraints(
    #     tier,
    #     profile,
    #     skill
    # )

    # print(constraints)



# def build_prompt(tier, arc, seed):
#     rng = random.Random(seed)
#     skill = SKILLS[arc["skill"]]

#     name = rng.choice(NAMES)
#     location = rng.choice(arc["locations"])

#     skill_constraints = build_skill_constraints(skill, arc)

#     prompt_text = f"""
# You are generating a short story for a machine learning dataset.

# GOAL:
# Show a child learning to {arc["goal"]}.

# STRUCTURE:
# Write the story using the following stages in order:
# {format_story_beats(arc["story_beats"])}

# CONSTRAINTS:
# - Maximum {tier["max_sentences"]} sentences total
# - Maximum {tier["max_sentence_length"]} words per sentence
# - Use age-appropriate, concrete language
# - Do not explain lessons directly
# {skill_constraints}

# CONTENT:
# - Main character: {name}
# - Location: {location}

# IMPORTANT:
# Show confusion, awkwardness, or uncertainty before improvement.
# End with emotional or practical understanding.
# """.strip() # not sure if important thing should always be the same

#     return {
#         "prompt": prompt_text,
#         "metadata": {
#             "tier": tier["id"],
#             "arc": arc["arc_id"],
#             "skill": arc["skill"],
#             "seed": seed
#         }
#     }
