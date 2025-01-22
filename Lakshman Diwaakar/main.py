from src.connectDB import pineconeDB
from dotenv import load_dotenv
import os
load_dotenv()
# connecting to the databse

pc = pineconeDB(index_name="lakshmandiwakar", api_key=os.getenv("PINECONE"), dimensions=1536 )
pc.configureDB()
