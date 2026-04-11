
from app.database import SessionLocal
from app.models.department import Department


departments = [
    "小児科",
    "耳鼻咽喉科",
    "皮膚科",
    "眼科",
    "外科",
    "整形外科",
    "歯科",
    "アレルギー科",
    "内科",
    "その他"
]

def seed_departments():
    db = SessionLocal()

    try:
        for name in departments:
            exists = db.query(Department).filter_by(name=name).first()

            if not exists:
                db.add(Department(name=name))

        db.commit()
    
    finally:
        db.close()

# 直接実行した時のみシーダーを投入
if __name__ == "__main__":
    seed_departments()