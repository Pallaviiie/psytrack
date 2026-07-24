import random

RESPONSES = {

    "Depression": [

        {
            "intro": "I'm really sorry you're feeling this way.",
            "support": "It sounds like you're going through a difficult time, and I appreciate you sharing your feelings with me.",
            "advice": "Sometimes talking to someone you trust, maintaining a regular sleep schedule, and doing small enjoyable activities can help. If these feelings continue, consider reaching out to a mental health professional.",
            "question": "Would you like to tell me what has been making you feel this way?"
        },

        {
            "intro": "Thank you for opening up.",
            "support": "Feeling low can be emotionally exhausting, but you don't have to face it alone.",
            "advice": "Taking one small positive step today, like going for a short walk or speaking with someone you trust, can make a difference.",
            "question": "How long have you been feeling like this?"
        }

    ],

    "Anxiety": [

        {
            "intro": "I understand that anxiety can feel overwhelming.",
            "support": "Many people experience anxiety before interviews, exams, or important events.",
            "advice": "Try taking slow deep breaths, focus on one task at a time, and avoid overthinking situations that haven't happened yet.",
            "question": "Can you tell me what has been worrying you recently?"
        },

        {
            "intro": "Thank you for sharing your thoughts.",
            "support": "Anxiety often makes us imagine the worst possible outcome.",
            "advice": "Try the 4-7-8 breathing technique or grounding exercises to calm your mind.",
            "question": "Is there a particular situation causing your anxiety?"
        }

    ],

    "Stress": [

        {
            "intro": "It sounds like you've been under a lot of pressure.",
            "support": "Stress can affect both your mind and body.",
            "advice": "Try taking short breaks, staying hydrated, exercising regularly, and planning your work into smaller tasks.",
            "question": "What's been causing the most stress lately?"
        }

    ],

    "Bipolar Disorder": [

        {
            "intro": "Thank you for sharing how you're feeling.",
            "support": "Mood changes can be difficult to manage.",
            "advice": "Keeping a mood journal and maintaining a consistent daily routine may help. If symptoms continue, professional support is recommended.",
            "question": "Have you noticed changes in your mood over several days or weeks?"
        }

    ],

    "Personality Disorder": [

        {
            "intro": "I appreciate you talking about this.",
            "support": "Emotional and interpersonal challenges can be difficult.",
            "advice": "Professional guidance can help you better understand and manage these experiences.",
            "question": "Would you like to describe what happened recently?"
        }

    ],

    "Unknown": [

        {
            "intro": "I'm here to listen.",
            "support": "Thank you for sharing your thoughts.",
            "advice": "Please tell me more about what's been on your mind.",
            "question": "How have you been feeling lately?"
        }

    ]
}


def get_response(prediction):

    responses = RESPONSES.get(
        prediction,
        RESPONSES["Unknown"]
    )

    return random.choice(responses)