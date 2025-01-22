from src.connectDB import pineconeDB
from dotenv import load_dotenv
import os
load_dotenv()
# connecting to the databse
print("hellow world")
pc = pineconeDB("vivek_1", os.getenv("PINECONE") )
print("hellow world 2")
