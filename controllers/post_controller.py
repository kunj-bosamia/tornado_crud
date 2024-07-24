from sqlalchemy.future import select
from models.database import SessionLocal
from models.post import Post

async def create_post(post_data: dict):
    async with SessionLocal() as session:
        new_post = Post(**post_data)
        session.add(new_post)
        await session.commit()
        await session.refresh(new_post)
        return new_post

async def get_post(post_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Post).where(Post.id == post_id))
        return result.scalars().first()

async def update_post(post_data: dict):
    async with SessionLocal() as session:
        result = await session.execute(select(Post).where(Post.id == post_data["id"]))
        post = result.scalars().first()
        if post:
            del post_data["id"]
            for key, value in post_data.items():
                setattr(post, key, value)
            await session.commit()
            await session.refresh(post)
        return post

async def delete_post(post_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Post).where(Post.id == post_id))
        post = result.scalars().first()
        if post:
            await session.delete(post)
            await session.commit()
        return post
