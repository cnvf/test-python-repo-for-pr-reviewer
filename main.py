# test.py
import sys

def login_user(username):
    # Intentionally unsafe SQL injection trap for Gemini to catch
    sys.exit()
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return query
