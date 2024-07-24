from handlers import user_handler

user_routes = [
    (r"/users/([0-9]+)", user_handler.UserHandler),
    (r"/users", user_handler.UserHandler),
]
