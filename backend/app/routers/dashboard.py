from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app import models

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    assessment = (
        db.query(models.Assessment)
        .filter(models.Assessment.user_id == current_user.id)
        .order_by(models.Assessment.created_at.desc())
        .first()
    )

    text_analysis = (
        db.query(models.TextAnalysis)
        .filter(models.TextAnalysis.user_id == current_user.id)
        .order_by(models.TextAnalysis.created_at.desc())
        .first()
    )

    recommendation = (
        db.query(models.Recommendation)
        .filter(models.Recommendation.user_id == current_user.id)
        .order_by(models.Recommendation.created_at.desc())
        .first()
    )

    return {

        "user": {
            "id": current_user.id,
            "name": current_user.full_name,
            "email": current_user.email
        },

        "latest_assessment": None if assessment is None else {
            "questionnaire_type": assessment.questionnaire_type,
            "score": assessment.total_score,
            "depression_level": assessment.depression_level,
            "date": assessment.created_at
        },

        "latest_text_analysis": None if text_analysis is None else {
            "prediction": text_analysis.prediction,
            "confidence": text_analysis.confidence,
            "text": text_analysis.input_text,
            "date": text_analysis.created_at
        },

        "latest_recommendation": None if recommendation is None else {
            "risk_level": recommendation.risk_level,
            "recommendations": recommendation.recommendations,
            "date": recommendation.created_at
        }

    }