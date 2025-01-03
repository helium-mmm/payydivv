from fastapi import APIRouter
from fastapi.params import Depends
from typing import Annotated


from schemas import UserAdd, User, UserId
from repositories.user import UserRepository

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.post("")
async def add_user(user: Annotated[UserAdd, Depends()]) -> UserId:
    user_id = await UserRepository.add_one(user)
    return {"ok": True, "user_id": user_id}

@router.get("")
async def get_rooms() -> list[User]:
    users = await UserRepository.find_all()
    return users