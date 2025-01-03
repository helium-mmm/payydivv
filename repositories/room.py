from schemas import RoomAdd, Room
from database import RoomOrm, new_session
from sqlalchemy import select


class RoomRepository:
    @classmethod
    async def add_one(cls, data: RoomAdd) -> int:
        async with new_session() as session:
            room_dict = data.model_dump()

            room = RoomOrm(**room_dict)
            session.add(room)
            await session.flush()
            await session.commit()
            return room.id

    @classmethod
    async def find_all(cls) -> list[Room]:
        async with new_session() as session:
            query = select(RoomOrm)
            result = await session.execute(query)
            room_models = result.scalars().all()
            return room_models