#setting up the app and getting the aws client, pinecone index 
from setup import setup_base, setup_get_config


index, bedrock_client_embedding, client = setup_get_config()

q = "Zerodha Midcap Fund Month January 2024 Zerodha Large Cap Mid Cap Return (%) 11.44"
output = client.query_pinecone(q, index, bedrock_client_embedding, top_k=3)
print(output)
# #updating the 