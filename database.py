from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine("sqlite+aiosqlite:///PayDiv.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    ...


class UserOrm(Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str | None]
    email: Mapped[str]
    password: Mapped[str]

class RoomOrm(Model):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    password: Mapped[str]
    description: Mapped[str | None]
    creator_id: Mapped[int]

class UserIntoRoom(Model):
    __tablename__ = 'user_into_room'

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int]
    user_id: Mapped[int]


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
