from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import List

from fastapi import Depends

from app.database import get_db
from app.auth import get_current_user
from app import models, schemas

from app.ml.bert_predict import predict_mental_health

router = APIRouter(
    prefix="/mental-health",
    tags=["Mental Health"]
)


# ============================================
# Analyze Mental Health using BERT
# ============================================
@router.post(
    "/analyze",
    response_model=schemas.TextAnalysisResponse
)
def analyze_text(
    request: schemas.TextAnalysisRequest,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Predict using BERT
    result = predict_mental_health(request.text)

    # Save prediction in database
    analysis = models.TextAnalysis(
        user_id=current_user.id,
        input_text=request.text,
        prediction=result["prediction"],
        confidence=str(result["confidence"])
    )

    db.add(analysis)
    db.commit()
    db.refresh(analysis)

    # Return prediction
    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }
@router.get(
    "/history",
    response_model=List[schemas.TextAnalysisHistory]
)
def get_text_analysis_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    history = (
        db.query(models.TextAnalysis)
        .filter(
            models.TextAnalysis.user_id == current_user.id
        )
        .order_by(
            models.TextAnalysis.created_at.desc()
        )
        .all()
    )

    result = []

    for item in history:

        result.append(

            schemas.TextAnalysisHistory(
                id=item.id,
                input_text=item.input_text,
                prediction=item.prediction,
                confidence=item.confidence,
                created_at=str(item.created_at)
            )

        )

    return result