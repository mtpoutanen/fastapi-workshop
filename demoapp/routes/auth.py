from fastapi import APIRouter

from demoapp.models import AuthResponse, AuthRequest

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def login(user_auth: AuthRequest) -> AuthResponse:
    if user_auth.username == "demo" and user_auth.password == "demo":
        return AuthResponse(token="demo-token")
    raise ValueError("Invalid credentials")


