from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# MongoDB connection URI
MONGO_DETAILS = "<CONNECTION URI>"
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