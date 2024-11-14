import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import create_app, db

app = create_app()  # アプリケーションインスタンスの作成

with app.app_context():
    # 既存のテーブルをすべて削除
    db.drop_all()
    
    # 新しいスキーマでテーブルを作成
    db.create_all()
    
    print("Database has been reset.")
