# exposures.py
TONES = {
    "curious": "The tone should show curiosity.",
    "excited": "The tone should show excitement.",
    "happy": "The tone should show happiness.",
    "playful": "The tone should be playful.",
    "encouraging": "The tone should be encouraging.",
    "calm": "The tone should be calm and simple.",
    "gentle": "The tone should show gentle effort and learning."
}



EXPOSURES = {
    "number_words": {
        "min_tier": 0,
        "max_tier": 0,
        "description": "rote number words", 
        "exposure_goal": "rote number words",
        "lexicon": {
            "nouns": ["ball", "block", "cup", "toy", "apple", "dog", "cat", "car"],
            "verbs": ["see", "look", "have", "count", "hold"],
            "adjectives": ["big", "small", "red", "blue"],
            },
        "tones": ["curious", "excited"],
        "locations": ["home", "school"]

    },

    "object_categories": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "animals, toys, foods",
        "exposure_goal": "simple object categories such as: animals, toys and foods",
        "lexicon": {
            "nouns": ["ball", "toy", "cup"],
            "verbs": ["see", "hold"],
            "adjectives": ["red", "big"],
            "emotion_vocab": ["happy", "sad"]
            },
        "tones": ["curious", "excited", "happy", "playful", "encouraging"],
        "locations": ["home", "school", "park", "car ride", "library"]
    },
    "time_words": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "yesterday, today, tomorrow",
        "exposure_goal": "basic time concepts such as yesterday, today, tomorrow, now, and later"
    },

    "social_rules": {
        "min_tier": 0,
        "max_tier": 3,
        "description": "turn-taking, fairness",
        "exposure_goal": "basic social rules such as turn-taking, sharing, fairness, and following simple group rules"
    },

    "colors": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "basic colors",
        "exposure_goal": "basic color words such as red, blue, yellow, and green"
    },

    "shapes": {
        "min_tier": 0,
        "max_tier": 1,
        "description": "basic shapes",
        "exposure_goal": "basic shape concepts such as circle, square, triangle, and rectangle"
    },

    "emotions": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "emotional states",
        "exposure_goal": "basic emotions such as happy, sad, angry, scared, and excited"
    },

    "daily_routines": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "everyday activities",
        "exposure_goal": "common daily routines such as eating, sleeping, bathing, and getting dressed"
    },

    "polite_language": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "social language",
        "exposure_goal": "polite and functional phrases such as please, thank you, sorry, and asking for help"
    },

    "pretend_play": {
        "min_tier": 0,
        "max_tier": 3,
        "description": "imaginative play",
        "exposure_goal": "pretend play scenarios such as playing house, caring for toys, and role-playing simple situations"
    },

    "safety_concepts": {
        "min_tier": 0,
        "max_tier": 2,
        "description": "basic safety awareness",
        "exposure_goal": "simple safety concepts such as hot vs cold, staying close to caregivers, and not touching dangerous objects"
    },
    
}