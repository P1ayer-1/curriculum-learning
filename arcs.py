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