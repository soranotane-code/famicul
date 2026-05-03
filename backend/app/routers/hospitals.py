from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.hospital import HospitalCreate, HospitalUpdate, HospitalResponse
from app.core.dependencies import get_db, get_current_user
from app.services import hospital_service

router = APIRouter()

# 病院情報の登録
@router.post("/hospitals", response_model=HospitalResponse)
def create_hospital(
    hospital_in: HospitalCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # serviceに処理を委譲して結果だけを返す
    return hospital_service.create_hospital_service(db, hospital_in, current_user.id)

# 病院情報の全件表示
@router.get("/hospitals", response_model=list[HospitalResponse])
def get_hospitals(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # serviceに処理を委譲して結果だけを返す
    return hospital_service.get_hospitals_service(db, current_user.id)

# 病院情報の表示
@router.get("/hospitals/{id}", response_model=HospitalResponse)
def get_hospital(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # serviceに処理を委譲して結果だけを返す
    return hospital_service.get_hospital_service(db, id, current_user.id)

# 病院情報の更新
@router.put("/hospitals/{id}", response_model=HospitalResponse)
def update_hospital(
    id: int,
    hospital_in: HospitalUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # serviceに処理を委譲して結果だけを返す
    return hospital_service.update_hospital_service(db, id, hospital_in, current_user.id)

# 病院情報の削除
@router.delete("/hospitals/{id}")
def delete_hospital(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # serviceに処理を委譲して結果だけを返す
    return hospital_service.delete_hospital_service(db, id, current_user.id)