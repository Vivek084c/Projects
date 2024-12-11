from fastapi import FastAPI, HTTPException, status
# from models import Blog, UpdateBlog
from database import blog_collection, blog_helper
from bson import ObjectId
from typing import List


#debug
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., min_length=10)
    author: str = Field(..., max_length=50)

class UpdateBlog(BaseModel):
    title: str = Field(None, max_length=100)
    content: str = Field(None, min_length=10)
    author: str = Field(None, max_length=50)

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# MongoDB connection URI
MONGO_DETAILS = "<CONNECTION URI>
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.school_blog
blog_collection = database.get_collection("blogs")

# Helper to convert MongoDB documents to dicts
def blog_helper(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "content": blog["content"],
        "author": blog["author"],
    }

app = FastAPI()

# Create a new blog post
@app.post("/blogs/", response_description="Add new blog", response_model=Blog)
async def create_blog(blog: Blog):
    blog_data = blog.dict()
    result = await blog_collection.insert_one(blog_data)
    return blog_helper(await blog_collection.find_one({"_id": result.inserted_id}))

# Retrieve all blog posts
@app.get("/blogs/", response_description="List all blogs", response_model=List[Blog])
async def get_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs

# Retrieve a single blog post
@app.get("/blogs/{id}", response_description="Get a single blog", response_model=Blog)
async def get_blog(id: str):
    blog = await blog_collection.find_one({"_id": ObjectId(id)})
    if blog is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog_helper(blog)

# Update a blog post
@app.put("/blogs/{id}", response_description="Update a blog", response_model=Blog)
async def update_blog(id: str, blog: UpdateBlog):
    updated_blog = {k: v for k, v in blog.dict().items() if v is not None}
    if len(updated_blog) >= 1:
        result = await blog_collection.update_one({"_id": ObjectId(id)}, {"$set": updated_blog})
        if result.modified_count == 1:
            updated_blog = await blog_collection.find_one({"_id": ObjectId(id)})
            return blog_helper(updated_blog)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

# Delete a blog post
@app.delete("/blogs/{id}", response_description="Delete a blog")
async def delete_blog(id: str):
    result = await blog_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 1:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
