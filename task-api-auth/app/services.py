from app.auth import signup_user, login_user

def create_user(email: str, password: str):
    return signup_user(email, password)

def authenticate_user(email: str, password: str):
    return login_user(email, password)