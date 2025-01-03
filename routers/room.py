from fastapi import APIRouter
from fastapi.params import Depends
from typing import Annotated


from schemas import RoomAdd, Room, RoomId
from repositories.room import RoomRepository

router = APIRouter(
    prefix="/rooms",
    tags=["Комнаты"]
)


@router.post("")
async def add_room(room: Annotated[RoomAdd, Depends()]) -> RoomId:
    room_id = await RoomRepository.add_one(room)
    return {"ok": True, "room_id": room_id}

@router.get("")
async def get_rooms() -> list[Room]:
    rooms = await RoomRepository.find_all()
    return rooms