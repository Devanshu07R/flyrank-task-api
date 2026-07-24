from fastapi import APIRouter
from app.schemas import UserSignup, UserLogin
from app.services import create_user, authenticate_user

router = APIRouter()


@router.post("/signup")
def signup(user: UserSignup):
    response = create_user(user.email, user.password)
    return response

@router.post("/login")
def login(user: UserLogin):
    response = authenticate_user(user.email, user.password)
    return response