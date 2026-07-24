from pydantic import BaseModel, EmailStr


# =====================================
# User Schemas
# =====================================

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


# =====================================
# Assessment Schemas
# =====================================

class AssessmentCreate(BaseModel):
    questionnaire_type: str

    phq1: int
    phq2: int
    phq3: int
    phq4: int
    phq5: int
    phq6: int
    phq7: int
    phq8: int
    phq9: int


class AssessmentResponse(BaseModel):
    id: int
    user_id: int
    questionnaire_type: str

    phq1: int
    phq2: int
    phq3: int
    phq4: int
    phq5: int
    phq6: int
    phq7: int
    phq8: int
    phq9: int

    total_score: int
    depression_level: str | None = None

    class Config:
        from_attributes = True
# ============================================
# Mental Health Text Analysis
# ============================================

class TextAnalysisRequest(BaseModel):
    text: str


class TextAnalysisResponse(BaseModel):
    prediction: str
    confidence: float
# =====================================
# Recommendation Schemas
# =====================================

class RecommendationRequest(BaseModel):
    depression_level: str
    text_prediction: str


class RecommendationResponse(BaseModel):
    risk_level: str
    recommendations: list[str]

# =====================================
# Recommendation Schemas
# =====================================

class RecommendationCreate(BaseModel):
    user_id: int
    assessment_id: int
    depression_level: str
    text_prediction: str


class RecommendationResponse(BaseModel):
    id: int
    user_id: int
    assessment_id: int
    risk_level: str
    recommendations: str

    class Config:
        from_attributes = True

# =====================================
# Assessment History
# =====================================

class AssessmentHistory(BaseModel):
    id: int
    questionnaire_type: str

    total_score: int
    depression_level: str

    created_at: str

    class Config:
        from_attributes = True

# =====================================
# Text Analysis History
# =====================================

class TextAnalysisHistory(BaseModel):
    id: int

    input_text: str

    prediction: str

    confidence: str

    created_at: str

    class Config:
        from_attributes = True

# =====================================
# Recommendation History
# =====================================

class RecommendationHistory(BaseModel):
    id: int

    risk_level: str

    recommendations: str

    created_at: str

    class Config:
        from_attributes = True