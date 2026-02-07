# exposures.py
TONES = {
    "curious": "Shows curiosity and wondering.",
    "excited": "Shows excitement and enthusiasm.",
    "playful": "Light, fun, and silly.",
    "encouraging": "Supports effort and participation.",
    "calm": "Slow, simple, and reassuring.",
    "gentle": "Soft guidance and learning.",
    "reassuring": "Provides safety and emotional comfort.",
    "patient": "Allows repetition and mistakes.",
    "imaginative": "Supports pretend and make-believe.",
    "caring": "Warm and nurturing."
}



EXPOSURES = {

    "number_words": {
        "min_tier": 0,
        "max_tier": 0,
        "description": "rote number words", 
        "exposure_goal": "rote number words",
        "tones": ["curious", "excited", "playful", "patient"],
        "locations": ["home", "school", "car ride"]
    },

    "object_categories": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "animals, toys, foods",
        "exposure_goal": "simple object categories such as: animals, toys and foods",
        "tones": ["curious", "excited", "playful", "encouraging"],
        "locations": ["home", "school", "park", "car ride", "library"]
    },

    "time_words": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "yesterday, today, tomorrow",
        "exposure_goal": "basic time concepts such as yesterday, today, tomorrow, now, and later",
        "tones": ["calm", "patient", "reassuring"],
        "locations": ["home", "school", "bedtime", "mealtime"]
    },

    "social_rules": {
        "min_tier": 0,
        "max_tier": 3,
        "description": "turn-taking, fairness",
        "exposure_goal": "basic social rules such as turn-taking, sharing, fairness, and following simple group rules",
        "tones": ["encouraging", "calm", "gentle", "reassuring"],
        "locations": ["school", "playground", "home", "daycare"]
    },

    "colors": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "basic colors",
        "exposure_goal": "basic color words such as red, blue, yellow, and green",
        "tones": ["excited", "playful", "curious"],
        "locations": ["home", "school", "park", "art table"]
    },

    "shapes": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "basic shapes",
        "exposure_goal": "basic shape concepts such as circle, square, triangle, and rectangle",
        "tones": ["curious", "playful", "patient"],
        "locations": ["home", "school", "playroom", "block area"]
    },

    "emotions": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "emotional states",
        "exposure_goal": "basic emotions such as happy, sad, angry, scared, and excited",
        "tones": ["gentle", "caring", "reassuring", "calm"],
        "locations": ["home", "school", "bedtime", "playground"]
    },

    "daily_routines": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "everyday activities",
        "exposure_goal": "common daily routines such as eating, sleeping, bathing, and getting dressed",
        "tones": ["calm", "patient", "encouraging"],
        "locations": ["home", "bathroom", "bedroom", "kitchen"]
    },

    "polite_language": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "social language",
        "exposure_goal": "polite and functional phrases such as please, thank you, sorry, and asking for help",
        "tones": ["gentle", "encouraging", "caring"],
        "locations": ["home", "school", "playground", "store"]
    },

    "pretend_play": {
        "min_tier": 0,
        "max_tier": 3,
        "description": "imaginative play",
        "exposure_goal": "pretend play scenarios such as playing house, caring for toys, and role-playing simple situations",
        "tones": ["imaginative", "playful", "excited", "happy"],
        "locations": ["playroom", "school", "home", "outdoors"]
    },

    "safety_concepts": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "basic safety awareness",
        "exposure_goal": "simple safety concepts such as hot vs cold, staying close to caregivers, and not touching dangerous objects",
        "tones": ["calm", "reassuring", "gentle"],
        "locations": ["home", "kitchen", "bathroom", "outdoors"]
    },
}
