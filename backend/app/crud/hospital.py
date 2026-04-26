from sqlalchemy.orm import Session

from app.models import Hospital
from app.schemas.hospital import HospitalCreate, HospitalUpdate

# 病院IDとユーザーIDから病院情報を取得
def get_hospital_by_id_and_user_id(
    db: Session,
    hospital_id: int,
    user_id: int
):
    return db.query(Hospital).filter(Hospital.id == hospital_id, Hospital.user_id == user_id).first()

# 病院情報の新規作成
def create_hospital(
    db: Session,
    hospital_in: HospitalCreate,
    user_id: int
):
    # 入力データから病院モデルを作成して保存する
    new_hospital = Hospital(
        user_id = user_id,
        name = hospital_in.name,
        # 今後受診科カラム入る予定
        address = hospital_in.address,
        tel = hospital_in.tel,
        memo = hospital_in.memo
    )
    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)

    return new_hospital

# 病院情報の更新
def update_hospital(
    db: Session,
    hospital: Hospital,
    hospital_in: HospitalUpdate
):
    update_data = hospital_in.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(hospital, key, value)

    db.commit()
    db.refresh(hospital)

    return hospital

# 病院情報の削除
def delete_hospital(
    db: Session,
    hospital: Hospital
) -> None:
    db.delete(hospital)
    db.commit()
    # 削除が実行されるとdbから削除されるためrefresh(hospital)は不要