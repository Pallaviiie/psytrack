from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth import get_current_user
from app import models

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency Alerts"]
)


# ---------------------------------------
# Get all emergency alerts
# ---------------------------------------
@router.get("/alerts")
def get_alerts(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    alerts = (
        db.query(models.EmergencyAlert)
        .order_by(models.EmergencyAlert.created_at.desc())
        .all()
    )

    return alerts


# ---------------------------------------
# Get pending alerts
# ---------------------------------------
@router.get("/pending")
def pending_alerts(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    alerts = (
        db.query(models.EmergencyAlert)
        .filter(models.EmergencyAlert.status == "Pending")
        .order_by(models.EmergencyAlert.created_at.desc())
        .all()
    )

    return alerts


# ---------------------------------------
# Mark alert as resolved
# ---------------------------------------
@router.put("/resolve/{alert_id}")
def resolve_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    alert = (
        db.query(models.EmergencyAlert)
        .filter(models.EmergencyAlert.id == alert_id)
        .first()
    )

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    alert.status = "Resolved"

    db.commit()
    db.refresh(alert)

    return {
        "message": "Emergency alert resolved successfully",
        "alert": alert
    }