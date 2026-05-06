TEST_CASES = [

    # -------- BASIC PREFERENCE --------
    {
        "name": "simple_preference",
        "steps": [
            "i like birds"
        ],
        "query": "what do i like",
        "expected": "i like birds"
    },

    # -------- CONFLICT --------
    {
        "name": "conflict_resolution",
        "steps": [
            "i like birds",
            "i dont like birds"
        ],
        "query": "what do i like",
        "expected": "i dont like birds"
    },

    # -------- NOISE --------
    {
        "name": "noise_resistance",
        "steps": [
            "i like birds",
            "random blah blah",
            "more useless noise"
        ],
        "query": "what do i like",
        "expected": "i like birds"
    },

    # -------- MULTI MEMORY --------
    {
        "name": "multiple_preferences",
        "steps": [
            "i like birds",
            "i like dogs"
        ],
        "query": "what do i like",
        "expected": "i like birds"  # highest confidence first
    },

    # -------- STABILITY --------
    {
        "name": "stability_test",
        "steps": [
            "i like birds"
        ],
        "query": "what do i like",
        "repeat": 5,
        "expected": "i like birds"
    },

    # -------- NEGATION EDGE --------
    {
        "name": "negation_flip",
        "steps": [
            "i like birds",
            "i dont like birds",
            "i like birds again"
        ],
        "query": "what do i like",
        "expected": "i like birds"
    },

    # -------- DIFFERENT ENTITY --------
    {
        "name": "different_entities",
        "steps": [
            "i like cats",
            "i like birds"
        ],
        "query": "what do i like",
        "expected": "i like cats"
    },

]