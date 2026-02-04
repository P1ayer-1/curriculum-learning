


SKILLS = {
    "object_naming": {
        "description": "learning names of concrete objects",
        "phases": [
            {
                "phase": "perceptual_labeling",
                "description": "naming objects that are directly present",
                "recommended_tiers": [0, 1],
                "requires_capabilities": {
                    "abstract_reasoning": False
                },
                "surface_constraints": {
                    "ban_numbers": True,
                    "allowed_nouns": ["ball", "toy", "cup", "block"],
                    "allowed_verbs": ["see", "hold", "touch"],
                    "no_cross_sentence_reference": True
                }
            },
            {
                "phase": "stable_reference",
                "description": "referring to the same object across sentences",
                "recommended_tiers": [1, 2],
                "surface_constraints": {
                    "allow_pronouns": True
                }
            },
            {
                "phase": "category_awareness",
                "description": "recognizing shared object categories",
                "recommended_tiers": [2, 3],
                "requires_capabilities": {
                    "abstract_reasoning": True
                }
            }
        ]
    },


    "action_exposure": {
        "description": "learning basic physical actions",
        "phases": [
            {
                "phase": "single_action",
                "recommended_tiers": [0, 1],
                "surface_constraints": {
                    "allowed_verbs": ["pick", "drop", "open", "close"],
                    "max_actions_per_sentence": 1,
                    "no_cause_effect": True
                }
            },
            {
                "phase": "action_sequences",
                "recommended_tiers": [1, 2],
                "requires_capabilities": {
                    "multi_step_reasoning": True
                },
                "surface_constraints": {
                    "max_actions_per_sentence": 2
                }
            },
            {
                "phase": "goal_directed_actions",
                "recommended_tiers": [2, 3],
                "requires_capabilities": {
                    "planning": True
                }
            }
        ]
    },


    "sensory_labels": {
        "description": "learning sensory properties",
        "phases": [
            {
                "phase": "direct_sensation",
                "recommended_tiers": [0, 1],
                "surface_constraints": {
                    "allowed_adjectives": ["red", "big", "soft", "loud"],
                    "no_comparatives": True
                }
            },
            {
                "phase": "relative_comparison",
                "recommended_tiers": [1, 2],
                "requires_capabilities": {
                    "abstract_reasoning": True
                }
            }
        ]
    },


    "social_presence": {
        "description": "recognizing other people",
        "phases": [
            {
                "phase": "physical_presence",
                "recommended_tiers": [0, 1],
                "surface_constraints": {
                    "allowed_nouns": ["mom", "dad", "child"],
                    "forbid_internal_states_of_others": True
                }
            },
            {
                "phase": "agentive_presence",
                "recommended_tiers": [1, 2],
                "surface_constraints": {
                    "allow_simple_actions_of_others": True
                }
            },
            {
                "phase": "mental_presence",
                "recommended_tiers": [2, 3],
                "requires_capabilities": {
                    "perspective_taking": True
                }
            }
        ]
    },

    "counting": {
        "description": "understanding quantity and number",
        "phases": [
            {
                "phase": "enumeration_small",
                "description": "counting concrete objects up to five",
                "goal": "count objects correctly up to five",
                "recommended_tiers": [1, 2],
                "surface_constraints": {
                    "numbers": { "range": [1, 5], "operations": ["count"] }
                },
                "requires_capabilities": {
                    "counting": True,
                    "abstract_reasoning": False
                }
            },
            {
                "phase": "enumeration_extended",
                "description": "counting larger sets",
                "recommended_tiers": [2, 3],
                "surface_constraints": {
                    "numbers": { "range": [1, 20], "operations": ["count"] }
                },
                "requires_capabilities": {
                    "counting": True,
                    "abstract_reasoning": False
                }
            },
            {
                "phase": "operational_counting",
                "description": "using counting to support goals",
                "recommended_tiers": [3, 4],
                "surface_constraints": {
                    "operations": ["count", "add", "subtract"]
                },
                "requires_capabilities": {
                    "multi_step_reasoning": True
                }
            }
        ]
    },

    "social_interaction": {
        "description": "learning to interact with others",
        "phases": [
            {
                "phase": "co_presence",
                "description": "being near others without social coordination",
                "goal": "learn to share objects with another child",
                "recommended_tiers": [0, 1],
                "requires_capabilities": {
                    "perspective_taking": False
                },
                "surface_constraints": {
                    "allowed_actions": ["sit", "stand", "watch"],
                    "forbid_internal_states_of_others": True
                }
            },
            {
                "phase": "reactive_interaction",
                "description": "responding to others' actions",
                "recommended_tiers": [1, 2],
                "requires_capabilities": {
                    "cause_effect": True
                },
                "surface_constraints": {
                    "allow_turn_taking": True
                }
            },
            {
                "phase": "intentional_interaction",
                "description": "acting with awareness of others’ goals",
                "recommended_tiers": [2, 3],
                "requires_capabilities": {
                    "perspective_taking": True
                }
            },
            {
                "phase": "norm_based_interaction",
                "description": "following shared rules and expectations",
                "recommended_tiers": [3, 4],
                "requires_capabilities": {
                    "abstract_reasoning": True
                },
                "surface_constraints": {
                    "allow_rules": ["take turns", "be fair"]
                }
            },
            {
                "phase": "negotiation_and_repair",
                "description": "resolving conflict through discussion",
                "recommended_tiers": [4, 5],
                "requires_capabilities": {
                    "multi_step_reasoning": True
                }
            },
            {
                "phase": "identity_and_values",
                "description": "social behavior shaped by identity and values",
                "recommended_tiers": [5, 6],
                "requires_capabilities": {
                    "metacognition": True
                }
            }
        ]
    }

}




def build_skill_constraints(skill_spec, arc): # broken now
    lines = []

    if skill_spec.get("ban_numbers"):
        lines.append("- Do not use numbers or counting")

    if "allow_numbers" in skill_spec and skill_spec["allow_numbers"]:
        lines.append(f"- Only use these numbers if needed: {skill_spec['allow_numbers']}")

    if skill_spec.get("grammar_focus"):
        focus = ", ".join(skill_spec["grammar_focus"])
        lines.append(f"- Focus on using clear {focus}")

    if skill_spec.get("emotion_words_allowed"):
        emotions = ", ".join(arc.get("emotions", []))
        if emotions:
            lines.append(f"- Emotion words allowed: {emotions}")

    return "\n".join(lines)


