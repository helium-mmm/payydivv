from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables
from routers.room import router as room_router
from routers.user import router as user_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print('База готова')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(room_router)
app.include_router(user_router)
