import boto3
import json
import os
import logging

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logger = logging.getLogger('bedrock')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_dir, 'bedrock.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Include the function name in the log formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - [%(funcName)s] - %(message)s'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class Bedrock:
    def __init__(self, service_name, modelId,region_name, aws_access_key_id, secret_access_key ):
        self.service_name = service_name
        self.modelId = modelId
        self.regioin_name = region_name
        self.aws_access_key_id = aws_access_key_id
        self.secret_access_key = secret_access_key

    def configure_get_client(self):
        """
        configure aws client and return the object
        """    
        logger.debug("Started - Creating the aws client")

        bedrock = boto3.client(
            service_name = self.service_name,
            aws_access_key_id = self.aws_access_key_id,
            aws_secret_access_key = self.secret_access_key
        )

        logger.debug("Completed - Creating the aws client")

        return bedrock
    
    def configure_get_llm_client(self):
        logger.debug("Started - Creating the aws client")
        
        bedrock = boto3.client(
        service_name = "bedrock-runtime",
        aws_access_key_id = self.aws_access_key_id,
        aws_secret_access_key = self.secret_access_key
        )   

        return bedrock

    def generate_titan_embedding(self,text, bedrock):
        """
        Retures the Embedding data for a given text
        Args:
            text -  the input text
            bedrock - Bedrock client for AWS
        Returs:
            Embedding vector (dimension 1536)
        """
        logger.debug("Started - The Embedding vectore generation")
        response = bedrock.invoke_model(
            modelId=self.modelId,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({"inputText": text})
        )
        logger.debug("Completed -  The Embedding vectore generation")
        result = json.loads(response["body"].read())
        logger.debug("Completed -  Done with vector Extraction")
        return result["embedding"]  # Embedding vector
    
    def upsert_to_pinecone(self,data, index, bedrock):
        """
        Data should be a list of dictionaries, where each dictionary contains:
        - 'id': unique ID for the item
        - 'text': the text to embed
        - 'index' : the index for the pinecone server
        - 'bedrock' : configured bedrock client for embeding generation
        """
        logger.debug("Started - the Upload to pinecone databse")
        for item in data:
            text = item["text"]
            embedding = self.generate_titan_embedding(text, bedrock)
            index.upsert(vectors=[(item["id"], embedding)])
        logger.debug("Completed - the Upload to pinecone databse")


    def query_pinecone(self, query_text, index, bedrock, top_k=5):
        """
        Query Pinecone index with a text query and return results sorted by score in descending order.
        
        Args:
            query_text (str): The text to query.
            index : pinecone index object
            top_k (int): The number of top results to retrieve.

        Returns:
            list: List of results sorted by score in descending order.
        """
        # Generate embedding for the query
        logger.debug("Started -  Embedding generation ")
        query_embedding = self.generate_titan_embedding(query_text, bedrock)
        logger.debug("Completed -  Embedding generation ")
        
        # Query Pinecone index
        logger.debug("Started - Pinecone Query")
        results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
        logger.debug("Completed - Pinecone Query")
        
        # Sort results by score in descending order (if not already sorted)
        sorted_results = sorted(results["matches"], key=lambda x: x["score"], reverse=True)
        logger.debug("Returned the results")
        
        return sorted_results

        

 