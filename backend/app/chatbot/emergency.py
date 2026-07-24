# ============================================
# Emergency Detection
# ============================================

EMERGENCY_KEYWORDS = [

    "kill myself",
    "end my life",
    "want to die",
    "commit suicide",
    "suicide",
    "self harm",
    "self-harm",
    "hurt myself",
    "take my life",
    "i don't want to live",
    "i want to die",
    "i am going to kill myself"
]


def is_emergency(text: str):

    text = text.lower()

    for keyword in EMERGENCY_KEYWORDS:

        if keyword in text:

            return True

    return False