import pandas as pd
import json
import logging
import os

# handling the logging
# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('PreProcess')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'PreProcess.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

class preprocess:
    def generate_embedding_data(self,path):
        df = pd.read_csv(path)
        logger.debug("Completed Reading the Data csv")
        clms = list(df.columns)
        no_of_rows = len(df.iloc[:,0:1])
        logger.debug("Started The emebeding_data generation process")

        embedding_data = []
        for i in range(no_of_rows):
            data = list(df.iloc[i,:])
            s = ""
            for j in range(len(clms)):
                s+=" "+str(clms[j])+" "+str(data[j])
            embedding_data.append(s)
            if i>=1:
                break

        data = [{"id": f"item-{i+1}", "text": embedding_data[i]} for i in range(len(embedding_data))]
        logger.debug("Completed The emebeding_data generation process")
        # for i in data:
        #     print(i)
        return data

    def generate_titan_embedding(self,text, bedrock, TITAN_EMBEDDING_MODEL):
        """
        Retures the Embedding data for a given text
        Args:
            text -  the input text
            bedrock - Bedrock client for AWS
            TITAN_EMBEDDING_MODEL - Embedding model name
        Returs:
            Embedding vector (dimension 1536)
        """
        logger.debug("Started - The Embedding vectore generation")
        response = bedrock.invoke_model(
            modelId=TITAN_EMBEDDING_MODEL,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({"inputText": text})
        )
        logger.debug("Completed -  The Embedding vectore generation")
        result = json.loads(response["body"].read())
        logger.debug("Completed -  Done with vector Extraction")
        return result["embedding"]  # Embedding vector
    
    def upsert_to_pinecone(self,data, index):
        """
        Data should be a list of dictionaries, where each dictionary contains:
        - 'id': unique ID for the item
        - 'text': the text to embed
        - 'index' : the index for the pinecone server
        """
        logger.debug("Started - the Upload to pinecone databse")
        for item in data:
            text = item["text"]
            embedding = self.generate_titan_embedding(text)
            index.upsert(vectors=[(item["id"], embedding)])
        logger.debug("Completed - the Upload to pinecone databse")