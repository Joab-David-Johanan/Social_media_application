import sqlite3
from sqlite3 import Connection
from models import post, posts


def get_post(connection: Connection) -> list[dict]:

    with connection:
        cur = connection.cursor()
        cur = cur.execute(
            """
            SELECT post_title, post_text, user_id
            FROM posts;
            """
        )
        return cur.fetchall()


def insert_post(connection: Connection, post: dict):
    # we do this inside context manager
    # so we do not have to worry about closing the db and cleaning it up
    with connection:
        cur = connection.cursor()
        cur.execute(
            """
            INSERT INTO posts (post_title,post_text,user_id)
            VALUES
            ( :post_title , :post_text , :user_id  )
            """,
            post,
        )


if __name__ == "__main__":

    connection = sqlite3.connect("social.db")
    connection.row_factory = sqlite3.Row
    # dictionary of test post
    test_post = {
        "post_title": "Fourth post",
        "post_text": "this is the fourth post",
        "user_id": 4,
    }

    insert_post(connection=connection, post=test_post)
    for post in get_post(connection):
        print(dict(post))
