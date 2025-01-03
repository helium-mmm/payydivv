from schemas import UserAdd, User
from database import UserOrm, new_session
from sqlalchemy import select


class UserRepository:
    @classmethod
    async def add_one(cls, data: UserAdd) -> int:
        async with new_session() as session:
            user_dict = data.model_dump()

            user = UserOrm(**user_dict)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def find_all(cls) -> list[User]:
        async with new_session() as session:
            query = select(UserOrm)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models