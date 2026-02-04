# generate_prompts.py

from curriculum import TIERS, TIER_PROFILES
from arcs import ARCS, check_arc_compatible
from prompt_builder import build_prompt
from skills import SKILLS
from capabilities import check_capability_compatibility
from names import get_name
import sys




def generate_prompts(
):
    prompts = []

    for tier in TIERS:
        tier_data = TIERS[tier]
        for profile in TIER_PROFILES[tier]:
            for arc in ARCS:
                is_arc_compatible = check_arc_compatible(tier, arc, tier_data) # should this be here or build prompt func?

                if not is_arc_compatible:
                    continue
                
                skill = None
                skill_phase = None
                phase_data = None

                if arc["skill"]:
                    skill = SKILLS[arc["skill"]]

                    skill_phase = arc["skill_phase"]

                    phases = skill["phases"]

                    for phase in phases:
                        if phase["phase"] == skill_phase:
                            phase_data = phase

                    # Validate skill compatibility
                    is_compatible = check_capability_compatibility(
                        phase_data,
                        tier_data
                    )

                    if not is_compatible:
                        continue


                for location in arc["locations"]:
                    name = get_name()
                    result = build_prompt(tier_data, profile, arc, skill, phase_data, name, location)
                    prompts.append(result)
        return prompts


if __name__ == "__main__":
    prompts = generate_prompts()

    # Print example
    example = prompts[0]
    # print("METADATA:", example["metadata"])
    print("\nPROMPT:\n")
    print(example["prompt"])
