import bcrypt
import sqlite3
from config import DB_PATH

def register_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                       (username, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Пользователь уже существует
    finally:
        conn.close()

def check_password(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    
    conn.close()

    if user and bcrypt.checkpw(password.encode(), user[0]):
        return True
    return False