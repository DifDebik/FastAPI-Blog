from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowCreator(BaseModel):
    name: str
    email: str


class ShowUser(ShowCreator):
    blogs: list[Blog]


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowCreator


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
