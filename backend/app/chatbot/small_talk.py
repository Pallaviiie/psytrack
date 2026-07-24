import random

SMALL_TALK = {

    "greeting": {
        "keywords": [
            "hi", "hello", "hey", "hii", "good morning",
            "good afternoon", "good evening", "namaste"
        ],
        "responses": [
            "Hello! 😊 I'm PsyTrack AI. How are you feeling today?",
            "Hi! It's nice to talk with you. How have you been feeling lately?",
            "Hey! I'm here to listen. What's on your mind today?"
        ]
    },

    "thanks": {
        "keywords": [
            "thanks", "thank you", "thx", "thankyou"
        ],
        "responses": [
            "You're most welcome! 😊",
            "I'm glad I could help. Remember, I'm always here if you need someone to talk to.",
            "Take care of yourself, and don't hesitate to come back anytime."
        ]
    },

    "bye": {
        "keywords": [
            "bye", "goodbye", "see you", "take care", "good night"
        ],
        "responses": [
            "Take care! 🌸 Wishing you a peaceful day ahead.",
            "Goodbye! Remember to be kind to yourself.",
            "See you soon. Stay healthy and stay positive."
        ]
    },

    "who_are_you": {
        "keywords": [
            "who are you",
            "what are you",
            "your name"
        ],
        "responses": [
            "I'm PsyTrack AI, your mental health support assistant. I'm here to listen and provide supportive guidance."
        ]
    },

    "what_can_you_do": {
        "keywords": [
            "what can you do",
            "help me",
            "your features"
        ],
        "responses": [
            "I can assess your mental well-being, analyze how you're feeling, provide supportive suggestions, detect emergencies, and chat with you."
        ]
    }

}


def check_small_talk(message):

    message = message.lower().strip()

    for category in SMALL_TALK.values():

        for keyword in category["keywords"]:

            if keyword in message:

                return random.choice(category["responses"])

    return None