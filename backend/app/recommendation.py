from typing import List

def generate_recommendation(
    depression_level: str,
    text_prediction: str
):
    """
    Generate Risk Level and Personalized Recommendations
    using PHQ-9 Depression Level + BERT Prediction.
    """

    depression_level = depression_level.lower()
    text_prediction = text_prediction.lower()

    recommendations: List[str] = []
    risk = "Low"

    # =====================================================
    # Minimal Depression
    # =====================================================

    if depression_level == "minimal":

        risk = "Low"

        recommendations.extend([
            "Maintain a healthy daily routine.",
            "Exercise for at least 30 minutes.",
            "Sleep 7–8 hours every night.",
            "Practice gratitude journaling.",
            "Stay socially connected."
        ])

    # =====================================================
    # Mild Depression
    # =====================================================

    elif depression_level == "mild":

        risk = "Low"

        recommendations.extend([
            "Practice deep breathing exercises.",
            "Meditate for 10–15 minutes daily.",
            "Take regular study/work breaks.",
            "Talk with trusted friends or family.",
            "Maintain a consistent sleep schedule."
        ])

    # =====================================================
    # Moderate Depression
    # =====================================================

    elif depression_level == "moderate":

        risk = "Medium"

        recommendations.extend([
            "Consult a mental health professional.",
            "Practice Cognitive Behaviour Therapy (CBT) exercises.",
            "Exercise regularly.",
            "Reduce excessive screen time.",
            "Follow a healthy diet.",
            "Share your feelings with someone you trust."
        ])

    # =====================================================
    # Moderately Severe Depression
    # =====================================================

    elif depression_level == "moderately severe":

        risk = "High"

        recommendations.extend([
            "Seek professional counselling immediately.",
            "Schedule an appointment with a psychologist.",
            "Do not isolate yourself.",
            "Reach out to family members.",
            "Practice relaxation techniques."
        ])

    # =====================================================
    # Severe Depression
    # =====================================================

    elif depression_level == "severe":

        risk = "Critical"

        recommendations.extend([
            "Seek immediate professional help.",
            "Contact a psychiatrist.",
            "Inform a trusted family member.",
            "Do not stay alone.",
            "Activate volunteer support if available."
        ])

    # =====================================================
    # Extra Recommendations based on BERT Prediction
    # =====================================================

    if text_prediction == "stress":

        recommendations.extend([
            "Practice mindfulness.",
            "Manage your workload.",
            "Take frequent short breaks."
        ])

    elif text_prediction == "anxiety":

        recommendations.extend([
            "Practice box breathing.",
            "Avoid excessive caffeine.",
            "Ground yourself using the 5-4-3-2-1 technique."
        ])

    elif text_prediction == "depression":

        recommendations.extend([
            "Share your feelings with someone you trust.",
            "Avoid complete isolation.",
            "Consider counselling sessions."
        ])

    elif text_prediction == "bipolar disorder":

        recommendations.extend([
            "Maintain a regular sleep routine.",
            "Monitor mood changes daily.",
            "Consult your psychiatrist regularly."
        ])

    elif text_prediction == "personality disorder":

        recommendations.extend([
            "Practice emotional regulation techniques.",
            "Maintain healthy relationships.",
            "Consider Dialectical Behaviour Therapy (DBT)."
        ])

    # =====================================================
    # Remove duplicate recommendations
    # =====================================================

    recommendations = list(dict.fromkeys(recommendations))

    return {
        "risk_level": risk,
        "recommendations": recommendations
    }