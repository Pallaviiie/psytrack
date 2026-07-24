from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app import models, schemas
from app.recommendation import generate_recommendation

router = APIRouter(
    prefix="/recommendation",
    tags=["Recommendation"]
)


@router.post("/", response_model=schemas.RecommendationResponse)
def create_recommendation(
    data: schemas.RecommendationCreate,
    db: Session = Depends(get_db)
):

    result = generate_recommendation(
        depression_level=data.depression_level,
        text_prediction=data.text_prediction
    )

    recommendation = models.Recommendation(
        user_id=data.user_id,
        assessment_id=data.assessment_id,
        risk_level=result["risk_level"],
        recommendations="\n".join(result["recommendations"])
    )

    db.add(recommendation)
    db.commit()
    db.refresh(recommendation)

    return recommendation
@router.get(
    "/history",
    response_model=List[schemas.RecommendationHistory]
)
def recommendation_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    history = (
        db.query(models.Recommendation)
        .filter(
            models.Recommendation.user_id == current_user.id
        )
        .order_by(
            models.Recommendation.created_at.desc()
        )
        .all()
    )

    result = []

    for item in history:

        result.append(

            schemas.RecommendationHistory(
                id=item.id,
                risk_level=item.risk_level,
                recommendations=item.recommendations,
                created_at=str(item.created_at)
            )

        )

    return result