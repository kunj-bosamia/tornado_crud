import sqlalchemy.exc
from tornado.web import RequestHandler
import json
from controllers.user_controller import create_user, get_user, delete_user, update_user
from sqlalchemy.exc import IntegrityError

class UserHandler(RequestHandler):
    async def post(self):
        try:
            data = json.loads(self.request.body)
            new_user = await create_user(data)
            self.set_status(201)
            self.write(json.dumps({"id": new_user.id, "name": new_user.name, "email": new_user.email}))
        except IntegrityError as e:
            self.set_status(400)
            self.write(json.dumps({"message" : "DB integrity error occurred" , "error_message" : f"{e.orig.args[0]}"}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))
            
    async def get(self, user_id):
        try:
            user = await get_user(int(user_id))
            if user:
                self.set_status(200)
                self.write(json.dumps({"id": user.id, "name": user.name, "email": user.email}))
            else:
                self.set_status(404)
                self.write({"message": "User not found"})
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))

    
    async def delete(self , user_id):
        try:
            res = await delete_user(int(user_id))
            if res:
                self.write(json.dumps({"message" : f"User deleted with user id {user_id}"}))
            else:
                self.write(json.dumps({"message" : f"User id {user_id} does not exists / already deleted"}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))

    
    async def put(self):
        try:
            data = json.loads(self.request.body)
            if "id" not in data:
                self.set_status(400)
                return self.write(json.dumps({"error_message" : "User id not passed"}))     
            updated_user = await update_user(data)
            if updated_user:
                self.write(json.dumps({"id": updated_user.id, "name": updated_user.name, "email": updated_user.email}))
            else:
                self.set_status(404)
                self.write({"error_message": f"User not found with user id {data['id']}"})
        except IntegrityError as e:
            self.set_status(400)
            self.write(json.dumps({"message" : "DB integrity error occurred" , "error_message" : f"{e.orig.args[0]}"}))
        except Exception as e:
            self.set_status(500)
            self.write(json.dumps({"message" : "Internal Server Error" , "error_message" : f"{e.args[0]}"}))
