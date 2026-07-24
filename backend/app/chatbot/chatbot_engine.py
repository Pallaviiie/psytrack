from app.ml.bert_predict import predict_mental_health
from app.chatbot.prompts import get_response
from app.chatbot.emergency import is_emergency
from app.chatbot.small_talk import check_small_talk


# ==========================================
# Chatbot Engine
# ==========================================

def chatbot_reply(user_message: str, history=None):
    # Previous conversation context
    if history is None:
        history = []
    # --------------------------------------
    # Build conversation context
    # --------------------------------------
    previous_user_messages = []

    for item in history:
        if item.role == "user":
           previous_user_messages.append(item.message.lower())

    current_message = user_message.lower()
    # Build previous context
    context = ""

    for item in history:
        context += f"{item.role}: {item.message}\n"
    
    if (
        "exam" in current_message
        and any("stress" in msg for msg in previous_user_messages)
    ):
       return {
            "prediction": "Stress",
            "confidence": 100,
            "reply": (
               "Earlier you mentioned feeling stressed, and now you've shared that your exams are contributing to it.\n\n"
               "Exam stress is very common. Try breaking your study into smaller sessions, taking regular breaks, sleeping well, and avoiding last-minute cramming.\n\n"
               "Would you like me to help you create a study timetable?"
            ),
            "emergency": False
        }
    
    if (
       "sleep" in current_message
       and any("stress" in msg or "anxious" in msg for msg in previous_user_messages)
    ):
        return {
            "prediction": "Stress",
            "confidence": 100,
            "reply": (
               "You mentioned feeling stressed earlier, and now you're also having trouble sleeping.\n\n"
               "Stress and anxiety can often affect sleep. Try limiting screen time before bed, maintaining a regular sleep schedule, and practicing relaxation techniques.\n\n"
               "Has this been happening for several days or just recently?"
            ),
           "emergency": False
        }
    
    if (
       "family" in current_message
       and any("stress" in msg or "sad" in msg for msg in previous_user_messages)
    ):
       return {
           "prediction": "Stress",
           "confidence": 100,
           "reply": (
               "I understand that family situations can sometimes be a major source of stress.\n\n"
               "Talking to someone you trust or taking some time to process your feelings can help.\n\n"
               "Would you like to tell me more about what's happening?"
            ),
           "emergency": False
        }
    
    if (
       "college" in current_message
       or "work" in current_message
    ):
        return {
           "prediction": "Stress",
           "confidence": 100,
           "reply": (
               "Balancing responsibilities at college or work can feel overwhelming.\n\n"
               "Breaking tasks into smaller goals and taking regular breaks can make things more manageable.\n\n"
               "Which part has been the most difficult recently?"
            ),
           "emergency": False
        }
    # --------------------------------------
    # Emergency Detection
    # --------------------------------------
    if is_emergency(user_message):
        return {
            "prediction": "Emergency",
            "confidence": 100,
            "reply": (
                "⚠️ I'm really sorry you're feeling this way.\n\n"
                "You deserve support, and you don't have to face this alone.\n\n"
                "Please reach out to a trusted family member, friend, or a mental health professional as soon as possible.\n\n"
                "If you feel you are in immediate danger, contact your local emergency services or a suicide prevention helpline right away."
            ),
            "emergency": True
        }

    # --------------------------------------
    # Small Talk Detection
    # --------------------------------------
    small_reply = check_small_talk(user_message)

    if small_reply:
        return {
            "prediction": "Small Talk",
            "confidence": 100,
            "reply": small_reply,
            "emergency": False
        }
    lower = user_message.lower()

    if "exam" in lower:

       return {
          "prediction": "Stress",
           "confidence": 100,
           "reply":
               "Earlier you mentioned feeling stressed, and now you've shared that your exams are contributing to it.\n\n"
               "Many students experience exam-related stress. Breaking your study into smaller sessions, taking short breaks, getting enough sleep, and avoiding last-minute cramming can really help.\n\n"
               "Would you like me to help you create a study schedule or suggest some relaxation techniques?",
           "emergency": False
        }
    # --------------------------------------
    # BERT Prediction
    # --------------------------------------
    result = predict_mental_health(user_message)

    prediction = result["prediction"]
    confidence = result["confidence"]

    # --------------------------------------
    # Build Reply
    # --------------------------------------
    response = get_response(prediction)

    reply = (
        f"{response['intro']}\n\n"
        f"{response['support']}\n\n"
        f"💡 Suggestion:\n"
        f"{response['advice']}\n\n"
        f"{response['question']}"
    )

    # --------------------------------------
    # Return Result
    # --------------------------------------
    return {
        "prediction": prediction,
        "confidence": confidence,
        "reply": reply,
        "emergency": False
    }