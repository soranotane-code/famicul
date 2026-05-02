from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.visit import VisitImageCreate
from app.core.dependencies import get_db
from app.services import visit_image_service

router = APIRouter()

# 画像の登録
@router.post("/visits/{visit_id}/images")
def create_visit_image(
    visit_id: int,
    visit_image_in: VisitImageCreate,
    db: Session = Depends(get_db),
):
    # serviceの処理を委譲し結果だけを返す
    return visit_image_service.create_visit_image_service(db, visit_id, visit_image_in)

# 画像の一覧取得
@router.get("/visits/{visit_id}/images")
def get_visit_images(
    visit_id: int,
    db: Session = Depends(get_db),
):
    return visit_image_service.get_visit_images_service(db, visit_id)

# 画像の削除
@router.delete("/visits/{visit_id}/images/{image_id}")
def delete_visit_image(
    visit_id: int,
    image_id: int,
    db: Session = Depends(get_db),
):

    # serviceに処理を委譲して結果だけを返す
    return visit_image_service.delete_visit_image_service(db, visit_id, image_id)