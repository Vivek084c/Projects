from src.connectDB import pineconeDB
import os

def connect_db(params):
    """
    Connect to Pinecone database and return the Pinecone index object.
    """
    pc = pineconeDB(
        index_name=params["pinecone"]["index_name"],
        api_key=os.getenv("PINECONE"),
        dimensions=1536,
    )
    pc.configureDB()
    index = pc.get_index()
    print(f"Connected to Pinecone index: {params['pinecone']['index_name']}")
    return index