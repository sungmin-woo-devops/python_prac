from typing import Optional
import fastapi
from fastapi import Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []

class User(BaseModel):
    id: int
    email: str
    is_active: bool
    name: Optional[str]
    gender: Optional[str]
    address: Optional[str]

# Users
@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User has been created successfully."}

@router.get("/users", response_model=list[User])
async def get_users():
    return users

@router.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The ID of the user you want to retrieve"),
):
    return {"user": users[id]}