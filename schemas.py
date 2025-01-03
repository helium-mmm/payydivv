from pydantic import BaseModel
from typing import Optional


class RoomAdd(BaseModel):
    name: str
    description: Optional[str] = None
    creator_id: int
    password: str


class UserAdd(BaseModel):
    name: str
    surname: Optional[str] = None
    email: str
    password: str

class Room(RoomAdd):
    id: int

class User(UserAdd):
    id: int

class RoomId(BaseModel):
    ok: bool = True
    room_id: int

class UserId(BaseModel):
    ok: bool = True
    user_id: int