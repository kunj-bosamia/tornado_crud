import asyncio
import tornado.web
from tornado.platform.asyncio import AsyncIOMainLoop
from routes.user_routes import user_routes
from routes.post_routes import post_routes
from models.database import init_db

async def main():
    await init_db()
    
    routes = user_routes + post_routes
    app = tornado.web.Application(routes)
    app.listen(8888)
    print("Server started on port 8888")
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    AsyncIOMainLoop().install()
    asyncio.run(main())
