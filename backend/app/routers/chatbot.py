from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app import models

from app.chatbot.chatbot_engine import chatbot_reply

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)


@router.post("/chat")
def chat(
    message: str,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    history = (
        db.query(models.ConversationMemory)
        .filter(
           models.ConversationMemory.user_id == current_user.id
        )
        .order_by(
            models.ConversationMemory.created_at.desc()
        )
        .limit(6)
        .all()
    )
    
    history.reverse()
    result = chatbot_reply(message, history)
    if result["emergency"]:

       print(">>> Emergency detected")

       alert = models.EmergencyAlert(
           user_id=current_user.id,
           message=message,
           prediction=result["prediction"],
           status="Pending"
        )

       db.add(alert)

       db.flush()

       print(">>> Emergency Alert ID:", alert.id)

    # Save user message
    user_message = models.ConversationMemory(
        user_id=current_user.id,
        role="user",
        message=message
    )

    # Save bot reply
    bot_message = models.ConversationMemory(
        user_id=current_user.id,
        role="assistant",
        message=result["reply"]
    )

    # Save chat history
    chat = models.ChatMessage(
        user_id=current_user.id,
        user_message=message,
        bot_reply=result["reply"],
        prediction=result["prediction"],
        confidence=str(result["confidence"]),
        emergency=str(result["emergency"])
    )

    db.add(user_message)
    db.add(bot_message)
    db.add(chat)

    try:
       db.commit()
       print(">>> Commit successful")
    except Exception as e:
       db.rollback()
       print(">>> DATABASE ERROR:", e)
       raise

    return result
@router.get("/history")
def chat_history(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    chats = (
        db.query(models.ChatMessage)
        .filter(models.ChatMessage.user_id == current_user.id)
        .order_by(models.ChatMessage.created_at.desc())
        .all()
    )

    return chats