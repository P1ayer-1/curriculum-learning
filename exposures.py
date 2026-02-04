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
