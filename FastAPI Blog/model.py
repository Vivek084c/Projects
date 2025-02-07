from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., max_length=50)

class UpdateBlog(BaseModel):
    title: str = Field(None, max_length=100)
    content: str = Field(None, min_length=10)
    author: str = Field(None, max_length=50)