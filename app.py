from fastapi import FastAPI
from database import get_post, insert_post
from models import Post, Posts
from sqlite3 import Connection, Row

app = FastAPI()

connection = Connection("social.db")
connection.row_factory = Row


# display the posts
@app.get("/posts")
async def posts() -> Posts:
    return get_post(connection=connection)


# add a post
@app.post("/post")
async def add_post(post: Post) -> Post:
    insert_post(connection=connection, post=post)
    return post
