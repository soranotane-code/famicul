from passlib.context import CryptContext

# bcryptを使う設定
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    """生パスワードをハッシュ化する（登録時）"""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """入力されたパスワードとDBのハッシュが一致するか検証する"""
    return pwd_context.verify(plain_password, hashed_password)