
from handlers import post_handler

post_routes =  [
    (r"/posts/([0-9]+)", post_handler.PostHandler),
    (r"/posts", post_handler.PostHandler),
]
