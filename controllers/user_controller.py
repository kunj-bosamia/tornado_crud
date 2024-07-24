from sqlalchemy.future import select
from sqlalchemy import delete , update
from models.database import SessionLocal
from models.user import User

async def create_user(user_data: dict):
    async with SessionLocal() as session:
        new_user = User(**user_data)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user

async def get_user(user_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

async def delete_user(user_id: int):
    user = await get_user(user_id)
    if user:
        async with SessionLocal() as session:
            await session.execute(
                delete(User).where(User.id == user_id)
            )
            await session.commit()
            return True
    else:
        return False
        

async def update_user(user_data: dict):
    async with SessionLocal() as session:
        result = await session.execute(select(User).where(User.id == user_data["id"]))
        user = result.scalars().first()
        if user:
            del user_data["id"]
            for key, value in user_data.items():
                setattr(user, key, value)
            await session.commit()
            await session.refresh(user)
        return user
