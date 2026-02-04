# arcs.py

ARC_TYPES = {
    "exposure": {
        "requires_capabilities": [],
        "allows_learning": False,
        "allows_adjustment": False
    },
    "conditioning": {
        "requires_capabilities": ["learning"],
        "allows_learning": True,
        "allows_adjustment": True
    },
    "skill_learning": {
        "requires_capabilities": ["learning", "multi_step_reasoning"],
        "allows_learning": True,
        "allows_adjustment": True
    }
}


ARCS = [
    {
        "arc_id": "counting_basic",
        "arc_type": "conditioning",               # NOT exposure
        "skill": "counting",
        "skill_phase": "enumeration_small",

        # conditioning implies a single adjustment, not full arc
        "structure": ["attempt", "cue", "response"],

        "locations": ["school", "home"],
        "min_tier": 1,
        "max_tier": 2
    },

    {
        "arc_id": "sharing_exposure",
        "arc_type": "exposure",                   # KEY CHANGE
        "skill": None,                            # no skill at tier 0
        "skill_phase": None,

        # no time, no feedback, no improvement
        "structure": ["co_presence", "object_contact"],

        "objects": ["crayons", "snacks", "toys"],
        "locations": ["school", "home", "playground"],
        "min_tier": 0,
        "max_tier": 0
    },

    {
        "arc_id": "sharing_conditioning",
        "arc_type": "conditioning",
        "skill": "social_interaction",
        "skill_phase": "co_presence",

        # minimal learning allowed
        "structure": ["conflict", "cue", "single_adjustment"],

        "objects": ["crayons", "snacks", "toys"],
        "locations": ["school", "home", "playground"],
        "min_tier": 1,
        "max_tier": 1
    }
]



def check_arc_compatible(tier, arc, tier_data):
    arc_type = arc["arc_type"]
    arc_rules = ARC_TYPES[arc_type]

    # Check tier range
    if not (arc["min_tier"] <= tier <= arc["max_tier"]):
        return False

    # Check required capabilities
    for cap in arc_rules["requires_capabilities"]:
        if not tier_data["capabilities"].get(cap, False):
            return False

    # Tier 0 cannot have skills or learning
    if tier == 0:
        if arc_type != "exposure":
            return False
        if arc.get("skill") is not None:
            return False

    return True
