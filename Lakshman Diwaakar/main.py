from src.connectDB import pineconeDB
from src.PreProcess import preprocess
from src.utils import Utils
from src.bedrock import Bedrock
from dotenv import load_dotenv
import os
load_dotenv()
import json
#loading the params file - stage 1
params = Utils.load_params("config.yaml")


# connecting to the databse - stage 2
pc = pineconeDB(index_name=params["pinecone"]["index_name"], api_key=os.getenv("PINECONE"), dimensions=1536 )
pc.configureDB()
print(params["pinecone"]["index_name"])
index = pc.get_index()




#preprocessing the data - stage 3
data = preprocess.generate_embedding_data(path = "data/mutula_fund.csv", generation_count=5)
print(data)
print(type(data))





#configuring the aws client object -  stage 4
client  = Bedrock(
    service_name = params["aws"]["service_name"], 
    modelId=params["aws"]["modelId"],
    region_name = params["aws"]["region"], 
    aws_access_key_id = params["aws"]["aws_access_key_id"], 
    secret_access_key = params["aws"]["secret_access_key"]
    )
bedrock_client = client.configure_get_client()

# update the preprocess data to pinecone databse - stage 5
client.upsert_to_pinecone(data, index, bedrock_client)

q = "Zerodha Midcap Fund Month January 2024 Zerodha Large Cap Mid Cap Return (%) 11.44"
output = client.query_pinecone(q, index, bedrock_client, top_k=3)
print(output)
# #updating the 


