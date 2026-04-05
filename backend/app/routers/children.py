from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.child import Child
from app.schemas.child import ChildCreate
from app.core.dependencies import get_db, get_current_user

router = APIRouter()

@router.post("/children")
def create_child(
    child_in: ChildCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_child = Child(
        name = child_in.name,
        gender = child_in.gender,
        birthday = child_in.birthday,
        weight = child_in.weight,
        chronic_disease = child_in.chronic_disease,
        allergy = child_in.allergy,
        # memo = child_in.memo,
        user_id = current_user.id
    )
    db.add(new_child)
    db.commit()
    db.refresh(new_child)

    return {
        "id": new_child.id,
        "name": new_child.name,
        "gender": new_child.gender,
        "birthday": new_child.birthday,
        "weight": new_child.weight,
        "chronic_disease": new_child.chronic_disease,
        "allergy": new_child.allergy,
        "message": "Child created successfully!" 
    }
