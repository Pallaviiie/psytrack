from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


# -----------------------------
# User Table
# -----------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)

    # One user can have many assessments
    assessments = relationship(
        "Assessment",
        back_populates="user",
        cascade="all, delete"
    )
    recommendations = relationship(
        "Recommendation",
        back_populates="user",
        cascade="all, delete"
    )
    chat_messages = relationship(
        "ChatMessage",
        back_populates="user",
        cascade="all, delete"
    )
    conversation_memory = relationship(
       "ConversationMemory",
       back_populates="user",
       cascade="all, delete"
    )
    emergency_alerts = relationship(
        "EmergencyAlert",
        back_populates="user",
        cascade="all, delete"
    )
# -----------------------------
# Assessment Table
# -----------------------------
class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    questionnaire_type = Column(
        String(20),
        nullable=False
    )

    phq1 = Column(Integer)
    phq2 = Column(Integer)
    phq3 = Column(Integer)
    phq4 = Column(Integer)
    phq5 = Column(Integer)
    phq6 = Column(Integer)
    phq7 = Column(Integer)
    phq8 = Column(Integer)
    phq9 = Column(Integer)

    total_score = Column(Integer)

    depression_level = Column(
        String(50)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="assessments"
    )
    recommendation = relationship(
        "Recommendation",
        back_populates="assessment",
        uselist=False
    )

# -----------------------------
# AI Text Analysis Table
# -----------------------------
class TextAnalysis(Base):
    __tablename__ = "text_analysis"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    input_text = Column(
        String,
        nullable=False
    )

    prediction = Column(
        String(100),
        nullable=False
    )

    confidence = Column(
        String(20),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship("User")

# -----------------------------
# Recommendation Table
# -----------------------------
class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    assessment_id = Column(
        Integer,
        ForeignKey("assessments.id"),
        nullable=False
    )

    risk_level = Column(
        String(50),
        nullable=False
    )

    recommendations = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="recommendations"
    )

    assessment = relationship(
        "Assessment",
        back_populates="recommendation"
    )
# -----------------------------
# Chat Messages Table
# -----------------------------
class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    user_message = Column(
        String,
        nullable=False
    )

    bot_reply = Column(
        String,
        nullable=False
    )

    prediction = Column(
        String(100),
        nullable=False
    )

    confidence = Column(
        String(20),
        nullable=False
    )

    emergency = Column(
        String(10),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="chat_messages"
    )
# -----------------------------
# Conversation Memory
# -----------------------------
class ConversationMemory(Base):
    __tablename__ = "conversation_memory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False
    )

    message = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship(
        "User",
        back_populates="conversation_memory"
    )
class EmergencyAlert(Base):
    __tablename__ = "emergency_alerts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    message = Column(
        String,
        nullable=False
    )

    prediction = Column(
        String(50),
        nullable=False
    )

    status = Column(
        String(20),
        default="Pending"
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship("User")