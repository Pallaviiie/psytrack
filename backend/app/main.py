from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from sqlalchemy import text

from app.database import engine, Base
from app import models
from app.routers import users, assessment, mental_health, recommendation, dashboard, chatbot, conversation, emergency
# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PsyTrack API",
    version="1.0.0",
    description="AI-powered Mental Health Monitoring System"
)
# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Routers
app.include_router(users.router)
app.include_router(assessment.router)
app.include_router(mental_health.router)
app.include_router(recommendation.router)
app.include_router(dashboard.router)
app.include_router(chatbot.router)
app.include_router(conversation.router)
app.include_router(emergency.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to PsyTrack API 🚀"
    }


@app.get("/test-db")
def test_db():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))

        return {
            "message": "Database connected successfully ✅"
        }

    except Exception as e:
        return {
            "error": str(e)
        }