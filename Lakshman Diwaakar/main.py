#setting up the app and getting the aws client, pinecone index 
from setup import setup_base, setup_get_config
from src.utils import Utils
from src.bedrock import Bedrock
from src.constants import extract_details_with_llm
import json

index, bedrock_client_embedding,bedrock_client_llm, client = setup_get_config()


# output = Utils.getresponse(bedrock_client_llm, "What is the capital of usa", )
# print(output)


outuput = extract_details_with_llm("Zerodha Midcap Fund Month January 2024 Zerodha Large Cap Mid Cap Return (%) 11.44", bedrock_client_llm)
print(outuput)
print("processed")







# q = "Zerodha Midcap Fund Month January 2024 Zerodha Large Cap Mid Cap Return (%) 11.44"
# output = client.query_pinecone(q, index, bedrock_client_embedding, top_k=3)
# print(output)
# #updating the 