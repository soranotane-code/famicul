# Famicul

『ふぁみカル』はこどものかかりつけ医、受診記録、薬の処方内容を一括管理し、家族で共有できる医療記録管理アプリケーションです。

## 🚀 機能（予定含む）
- **ユーザー管理**：家族アカウントの作成、認証
- **こどもプロフィール**：複数のこどもの情報を管理
- **受診記録**：日付、症状、受診先、診断内容の管理
- **画像管理**：処方箋や患部の写真アップロード

## 🛠技術スタック

- **バックエンド**: FastAPI(Python 3.12)
- **データベース**: PostgreSQL 15
- **ORM**: SQLAlchemy
- **マイグレーション**: Alembic
- **インフラ**: Docker / Docker Compose

## 必要な環境

- Docker と Docker Compose（推奨）、または
- Python 3.12 以上、PostgreSQL 15

## 🏃セットアップ

### Docker で動かす場合（推奨）

1. リポジトリをクローンしたら、プロジェクトのルートで以下を実行します。

   ```bash
   docker-compose up --build
   ```

2. バックエンドは `http://localhost:8000` で起動します。
3. API の説明は `http://localhost:8000/docs`（Swagger UI）で確認できます。

### 手動で動かす場合

1. PostgreSQL を起動し、データベース `famicul_db` を作成します。
2. プロジェクトルートに `.env` を用意し、次のように設定します。

   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/famicul_db
   ```

3. バックエンドの依存関係をインストールします。

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Alembic でマイグレーションを実行します。

   ```bash
   alembic upgrade head
   ```

5. サーバーを起動します。

   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 主な API エンドポイント

| メソッド | パス | 説明 |
|---------|------|------|
| GET | `/` | API の動作確認 |
| POST | `/register` | ユーザー登録 |
| POST | `/children` | お子さん情報の登録 |
| POST | `/department` | 診療科の登録 |

詳細は起動後に `http://localhost:8000/docs` で確認してください。

## 📂プロジェクト構成

```
famicul/
├── backend/
│   ├── app/
│   │   ├── core/        # セキュリティ・共通設定
│   │   ├── models/      # DBモデル定義(SQLAlchemy)
│   │   ├── schemas/     # バリデーション定義(Pydantic)
│   │   ├── database.py  # DB接続設定
│   ├── alembic/         # マイグレーション設定・履歴
│   ├── main.py          # エントリーポイント
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```
## 📊 データベース設計
![ER図](docs/ふぁみカルER.svg)

## 📝 ライセンス
そらのたねコード