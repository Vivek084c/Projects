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
logger = logging.getLogger('connectDB')
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
        self.pc = None  # To store the Pinecone instance

    def configureDB(self):
        """
        Connects to the database and returns the Pinecone object
        """
        try:
            self.pc = Pinecone(api_key=self.api_key)
            logger.debug("Created the Pinecone Instance")
        except Exception as e:
            logger.error(f"Error creating Pinecone instance: {e}")
            raise

        try:
            existing_indexes = self.pc.list_indexes()
            logger.debug("Fetched the existing Index")
        except Exception as e:
            logger.error(f"Error fetching existing indexes: {e}")
            raise

        try:
            if self.index_name not in existing_indexes:
                try:
                    self.pc.create_index(
                        name=self.index_name,
                        dimension=self.dimensions,
                        metric='dotproduct',
                        spec=ServerlessSpec(cloud='aws', region='us-east-1'),
                    )
                    logger.debug(f"Index '{self.index_name}' created successfully.- dimensions: {self.dimensions}")
                except Exception as e:
                    if "ALREADY_EXISTS" in str(e):
                        logger.warning(f"Index '{self.index_name}' already exists. Proceeding without creating it.")
                    else:
                        logger.error(f"Unexpected error during index creation: {e}")
                        raise
            else:
                logger.debug(f"Index '{self.index_name}' already exists.")
        except Exception as e:
            logger.error(f"Error creating or checking the index '{self.index_name}': {e}")
            raise

        return self.pc

    def get_index(self):
        """
        Returns the Pinecone index object for the configured index name
        """
        if not self.pc:
            raise ValueError("Pinecone is not configured. Call configureDB() first.")
        try:
            return self.pc.Index(self.index_name)
        except Exception as e:
            logger.error(f"Error retrieving the index '{self.index_name}': {e}")
            raise
