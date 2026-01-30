from typing import TypedDict
from pydantic import BaseModel

class Blog(BaseModel):
    title: str = Field(description="Title of the blog post")
    content: str = Field(description="Content of the blog post")
    tags: list[str] = Field(description="Tags for the blog post")

class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str
    