from pydantic import BaseModel


class post(BaseModel):

    post_title: str
    post_text: str
    user_id: int


class posts(BaseModel):

    posts: list[post]
