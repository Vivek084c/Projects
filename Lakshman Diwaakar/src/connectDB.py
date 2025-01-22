from pinecone import Pinecone, ServerlessSpec
import os
from dotenv import load_dotenv
load_dotenv()
import logging

# handling the logging
# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('model_building')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'connectDB.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class pineconeDB:
    def __init__(self, index_name, api_key, dimensions):
        self.index_name = index_name
        self.api_key = api_key
        self.dimensions = dimensions

    
    def configureDB(self):
        """
        connects to the database and return the pinecone object
        """    
        pc = Pinecone(api_key=self.api_key)
        logger.debug("Created the Pinecone Instance")

        existing_indexes = pc.list_indexes()
        logger.debug("Fetched the existing Index")

        if self.index_name not in existing_indexes:
            # Create the index if it doesn't exist    
            pc.create_index(
                name=self.index_name,
                dimension=self.dimensions,  # Dimension of your dense model
                metric='dotproduct',  # Metric for similarity search
                spec=ServerlessSpec(cloud='aws', region='us-east-1')
            )
            logger.debug(f"Index '{self.index_name}' created successfully.- dimensions: {self.dimensions}")
        else:
            logger.debug(f"Index '{self.index_name}' already exists.")

        return pc
    
