# test.py
def login_user(username):
    # Intentionally unsafe SQL injection trap for Gemini to catch
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return query
