import sqlite3
from sqlite3 import Connection


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

    # dictionary of test post
    test_post = {
        "post_title": "Third post",
        "post_text": "this is a Third post",
        "user_id": 2,
    }

    insert_post(connection=connection, post=test_post)
