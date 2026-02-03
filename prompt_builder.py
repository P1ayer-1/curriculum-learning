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


def merge_constraints(tier_data, profile, skill, phase_data=None):
    """
    Merge tier, profile, skill, and phase constraints into a single bundle.
    Tier constraints are absolute.
    """

    # --- 1. Start with tier (hard base) ---
    merged = {
        "limits": dict(tier_data.get("limits", {})),
        "language": dict(tier_data.get("language", {})),
        "surface": {},
        "forbidden_words": list(tier_data.get("forbidden_words", [])),
        "capabilities": dict(tier_data.get("capabilities", {}))
    }

    # --- 2. Apply profile (surface-only) ---
    profile_surface = profile.get("surface_constraints", {})
    for key, value in profile_surface.items():
        merged["surface"][key] = value

    # --- 3. Apply skill-level defaults (weak, optional) ---
    skill_surface = skill.get("surface_constraints", {})
    for key, value in skill_surface.items():
        merged["surface"].setdefault(key, value)

    # --- 4. Apply phase (may further restrict) ---
    if phase_data:

        phase_surface = phase.get("surface_constraints", {})
        for key, value in phase_surface.items():
            merged["surface"][key] = value  # phase overrides profile/skill

        # Phases may add forbidden words
        merged["forbidden_words"] = merge_lists(
            merged["forbidden_words"],
            phase.get("forbidden_words", [])
        )

    # --- 5. Final safety checks ---
    if merged["surface"].get("ban_numbers"):
        merged["surface"].pop("allowed_numbers", None)

    return merged



def format_story_beats(beats):
    return "\n".join(
        f"{i + 1}. {beat.upper()}" for i, beat in enumerate(beats)
    )


def build_prompt(tier_data, profile, arc, skill, phase_data, name, location):
    limits = tier_data["limits"]
    language = tier_data["language"]
    capabilities = tier_data["capabilities"]

    forbidden_words = tier_data.get("forbidden_words", [])
    surface = profile.get("surface_constraints", {})
    phase_surface = phase_data.get("surface_constraints", {})

    allowed_verbs = surface.get("allowed_verbs", [])
    allowed_nouns = surface.get("allowed_nouns", [])
    emotion_vocab = surface.get("emotion_vocab", [])

    allowed_actions = phase_surface.get("allowed_actions", [])
    forbid_internal_states = phase_surface.get(
        "forbid_internal_states_of_others", False
    )

    prompt = f"""
You are generating a short story for a machine learning dataset.

GOAL:
Show a child learning to {phase_data["goal"]}.

CHARACTERS:
- Main character: {name}
- Other characters may be present but unnamed

SETTING:
- Location: {location}
- Objects may include: {", ".join(arc["objects"])}

STORY STRUCTURE:
- Use the following story beats in order: {", ".join(arc["story_beats"])}

HARD CONSTRAINTS:
- Write at most {limits["max_sentences"]} sentences total
- Each sentence may contain at most {limits["max_sentence_length"]} words
- Use only present tense
- Do not use dialogue
- Do not ask questions
- Do not explain lessons or meanings

LANGUAGE LIMITS:
- Use simple, concrete language only
- Do not refer to past or future events
- Do not refer back to earlier sentences
- Avoid abstract concepts

FORBIDDEN WORDS:
- Do NOT use any of the following words:
  {", ".join(forbidden_words)}

SURFACE CONSTRAINTS:
- Allowed verbs: {", ".join(allowed_verbs)}
- Allowed nouns: {", ".join(allowed_nouns)}
- Allowed actions: {", ".join(allowed_actions)}
- Allowed emotion words: {", ".join(emotion_vocab)}

ADDITIONAL RULES:
- Do not use numbers
- Do not describe thoughts, beliefs, or plans
""".strip()

    if forbid_internal_states:
        prompt += """
- Do not describe what other characters think, feel, want, or know
""".rstrip()

    # Explicit capability bans (belt + suspenders)
    if not capabilities.get("cause_effect", True):
        prompt += """
- Do not explain why events happen
""".rstrip()

    if not capabilities.get("perspective_taking", True):
        prompt += """
- Do not describe understanding another person's point of view
""".rstrip()

    if not capabilities.get("planning", True):
        prompt += """
- Do not describe decisions or plans
""".rstrip()

    prompt += """

OUTPUT FORMAT:
- Output only the story text
- No titles
- No explanations
- No metadata
"""

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
