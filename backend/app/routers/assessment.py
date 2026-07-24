from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth import get_current_user
from typing import List

router = APIRouter(
    prefix="/assessments",
    tags=["Assessments"]
)


@router.post("/submit", response_model=schemas.AssessmentResponse)
def submit_assessment(
    assessment: schemas.AssessmentCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Calculate PHQ-9 total score
    total_score = (
        assessment.phq1 +
        assessment.phq2 +
        assessment.phq3 +
        assessment.phq4 +
        assessment.phq5 +
        assessment.phq6 +
        assessment.phq7 +
        assessment.phq8 +
        assessment.phq9
    )

    # Depression severity
    if total_score <= 4:
        depression_level = "Minimal"

    elif total_score <= 9:
        depression_level = "Mild"

    elif total_score <= 14:
        depression_level = "Moderate"

    elif total_score <= 19:
        depression_level = "Moderately Severe"

    else:
        depression_level = "Severe"

    new_assessment = models.Assessment(
        user_id=current_user.id,
        questionnaire_type=assessment.questionnaire_type,

        phq1=assessment.phq1,
        phq2=assessment.phq2,
        phq3=assessment.phq3,
        phq4=assessment.phq4,
        phq5=assessment.phq5,
        phq6=assessment.phq6,
        phq7=assessment.phq7,
        phq8=assessment.phq8,
        phq9=assessment.phq9,

        total_score=total_score,
        depression_level=depression_level
    )

    db.add(new_assessment)
    db.commit()
    db.refresh(new_assessment)

    return new_assessment

@router.get(
    "/history",
    response_model=List[schemas.AssessmentHistory]
)
def assessment_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    history = (
        db.query(models.Assessment)
        .filter(
            models.Assessment.user_id == current_user.id
        )
        .order_by(
            models.Assessment.created_at.desc()
        )
        .all()
    )

    result = []

    for item in history:

        result.append(

            schemas.AssessmentHistory(
                id=item.id,
                questionnaire_type=item.questionnaire_type,
                total_score=item.total_score,
                depression_level=item.depression_level,
                created_at=str(item.created_at)
            )

        )

    return result