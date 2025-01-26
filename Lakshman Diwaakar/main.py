# main.py
from connection_manager import get_connection_manager
from src.constants import extract_details_with_llm, process_rag_response

connection_manager = get_connection_manager()
index, bedrock_client_embedding, bedrock_client_llm, client = connection_manager.get_connections()

outuput_llm = extract_details_with_llm(
    "what is the Percentage Allocation change for Zerodha Midcap Fund HDFC Large Cap from 1/1/2024 january to 4/1/2024",
    bedrock_client_llm
)

print(outuput_llm)
output_rag = process_rag_response(
    "what is the Percentage Allocation change for Zerodha Midcap Fund HDFC Large Cap from 1/1/2024 january to 4/1/2024",
    outuput_llm,
    bedrock_client_llm
)

print(output_rag)