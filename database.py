import sqlite3
from sqlite3 import Connection
from models import Post, Posts


def get_post(connection: Connection) -> Posts:

    with connection:
        cur = connection.cursor()
        cur = cur.execute(
            """
            SELECT post_title, post_text, user_id
            FROM posts;
            """
        )
        return Posts(posts=[Post.model_validate(dict(post)) for post in cur])


def insert_post(connection: Connection, post: Post):
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
            post.model_dump(),
        )


if __name__ == "__main__":

    connection = sqlite3.connect("social.db")
    connection.row_factory = sqlite3.Row

    # dictionary of test post
    # test_post = {
    #     "post_title": "Pydantic post",
    #     "post_text": "this is the type checking post",
    #     "user_id": 10,
    # }

    # pydantic model type post
    test_post = Post(
        post_title="Pyantic post", post_text="Checking the type", user_id=10
    )

    insert_post(connection=connection, post=test_post)
    print(get_post(connection=connection))
