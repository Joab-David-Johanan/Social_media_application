from fastapi import FastAPI
from database import get_post
from models import Posts
from sqlite3 import Connection, Row

app = FastAPI()

connection = Connection("social.db")
connection.row_factory = Row


@app.get("/posts")
async def posts() -> Posts:
    return get_post(connection=connection)
