# main.py
from connection_manager import get_connection_manager
from src.constants import extract_details_with_llm, process_rag_response

connection_manager = get_connection_manager()
index, bedrock_client_embedding, bedrock_client_llm, client, data = connection_manager.get_connections()


outuput_llm = extract_details_with_llm(
    "what is the Percentage Allocation change for Zerodha Midcap Fund HDFC Large Cap from 1/1/2024 january to 4/1/2024",
    bedrock_client_llm
)

print(outuput_llm)

output_rage =  client.query_pinecone(query_text = outuput_llm, index = index, bedrock = bedrock_client_embedding, top_k=4)
# print(output_rage)
ids_to_retrieve = [result["id"] for result in output_rage]
# print(ids_to_retrieve)
filtered_texts = [entry['text'] for entry in data if entry['id'] in ids_to_retrieve]
single_string = " ".join(filtered_texts)


output_rag = process_rag_response(
    "what is the Percentage Allocation change for Zerodha Midcap Fund HDFC Large Cap from 1/1/2024 january to 4/1/2024",
    single_string,
    bedrock_client_llm
)

print(output_rag)

