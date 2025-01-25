def upsert_data(client, data, index, bedrock_client):
    """
    Upsert processed data into Pinecone database using Bedrock client.
    """
    client.upsert_to_pinecone(data, index, bedrock_client)
    print("Data upserted to Pinecone successfully.")