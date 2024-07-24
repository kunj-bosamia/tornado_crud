from tornado.web import RequestHandler
import json
from controllers.post_controller import create_post, get_post, update_post, delete_post
from sqlalchemy.exc import IntegrityError

class PostHandler(RequestHandler):
    async def post(self):
        try:
            data = json.loads(self.request.body)
            new_post = await create_post(data)
            self.write(json.dumps({"id": new_post.id, "title": new_post.title, "content": new_post.content, "user_id": new_post.user_id}))
        except IntegrityError as e:
            self.set_status(400)
            self.write(json.dumps({"message" : "DB integrity error occurred" , "error_message" : f"{e.orig.args[0]}"}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))

    async def get(self, post_id):
        try:
            post = await get_post(int(post_id))
            if post:
                self.write(json.dumps({"id": post.id, "title": post.title, "content": post.content, "user_id": post.user_id}))
            else:
                self.set_status(404)
                self.write({"error": "Post not found"})
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))

    async def put(self):
        try:
            data = json.loads(self.request.body)
            if "id" not in data:
                self.set_status(400)
                return self.write(json.dumps({"error_message" : "Post id  not passed"}))     
            updated_post = await update_post(data)
            if updated_post:
                self.write(json.dumps({"id": updated_post.id, "title": updated_post.title, "content": updated_post.content, "user_id": updated_post.user_id}))
            else:
                self.set_status(404)
                self.write({"error_message": f"Post not found with psot id {data['id']}"})
        except IntegrityError as e:
            self.set_status(400)
            self.write(json.dumps({"message" : "DB integrity error occurred" , "error_message" : f"{e.orig.args[0]}"}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))

    async def delete(self, post_id):
        try:
            deleted_post = await delete_post(int(post_id))
            if deleted_post:
                self.write({"success": "Post deleted"})
            else:
                self.set_status(404)
                self.write({"error": "Post not found"})
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))
