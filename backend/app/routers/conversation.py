from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import models
from app.auth import get_current_user

router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"]
)


# ==========================================
# Conversation History
# ==========================================

@router.get("/history")
def get_conversation_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    conversations = (
        db.query(models.ConversationMemory)
        .filter(
            models.ConversationMemory.user_id == current_user.id
        )
        .order_by(
            models.ConversationMemory.created_at.asc()
        )
        .all()
    )

    return conversations


# ==========================================
# Clear Conversation
# ==========================================

@router.delete("/clear")
def clear_conversation(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    db.query(models.ConversationMemory).filter(
        models.ConversationMemory.user_id == current_user.id
    ).delete()

    db.commit()

    return {
        "message": "Conversation history cleared successfully."
    }