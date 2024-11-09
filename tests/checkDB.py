import sqlite3

# データベースに接続する
conn = sqlite3.connect('instance/app.db')
cursor = conn.cursor()

# emailがNULLのレコードを取得
cursor.execute("SELECT user_id FROM users WHERE email IS NULL")
null_email_users = cursor.fetchall()

# 各レコードに対して一意のメールアドレスを設定する
for i, (user_id,) in enumerate(null_email_users, start=1):
    unique_email = f"sample{i}@hoge.com"
    cursor.execute("UPDATE users SET email = ? WHERE user_id = ?", (unique_email, user_id))

# 変更をコミットして保存する
conn.commit()

# 更新結果を確認するため、emailが'sample%'で始まるレコードを表示
cursor.execute("SELECT * FROM users WHERE email LIKE 'sample%@hoge.com'")
results = cursor.fetchall()
for row in results:
    print(row)

# 接続を閉じる
conn.close()
