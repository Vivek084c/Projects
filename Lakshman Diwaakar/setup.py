from src.connectDB import pineconeDB
from src.PreProcess import preprocess
from src.utils import Utils
from src.bedrock import Bedrock
from dotenv import load_dotenv
import os
import logging
load_dotenv()
import json



# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# Logging configuration
logger = logging.getLogger('setup')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

log_file_path = os.path.join(log_dir, 'setup.log')
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


def setup_base():
    #loading the params file - stage 1
    logging.debug("Started - Loading the params")
    params = Utils.load_params("config.yaml")
    logging.debug("Completed - Loading the params")


    logging.debug("Started - Connecting to the database")
    # connecting to the databse - stage 2
    pc = pineconeDB(index_name=params["pinecone"]["index_name"], api_key=os.getenv("PINECONE"), dimensions=1536 )
    pc.configureDB()
    index = pc.get_index()
    logging.debug("Completed - Connecting to the database")

    logging.debug("Started - Data Preprocessing")
    #preprocessing the data - stage 3
    data = preprocess.generate_embedding_data(path = "data/mutula_fund.csv", generation_count=-1)
    logging.debug("Completed - Data Preprocessing")

    logging.debug("Started - Bedrock client configuration")
    #configuring the aws client object -  stage 4
    client  = Bedrock(
        service_name = params["aws"]["service_name"], 
        modelId=params["aws"]["modelId"],
        region_name = params["aws"]["region"], 
        aws_access_key_id = params["aws"]["aws_access_key_id"], 
        secret_access_key = params["aws"]["secret_access_key"]
        )
    bedrock_client = client.configure_get_client()
    logging.debug("Completed - Bedrock client configuration")

    logging.debug("Started - Upadte the vectors to pinecone")
    # update the preprocess data to pinecone databse - stage 5
    client.upsert_to_pinecone(data, index, bedrock_client)
    logging.debug("Completed - Upadte the vectors to pinecone")

    return index, bedrock_client, client, data

def setup_get_config():
    """
    returns the pinecone index, bedrock_client(for aws embedding),bedrock_client(for aws llm) client object
    """

    logging.debug("Started - Loading the params")
    #loading the params file - stage 1
    params = Utils.load_params("config.yaml")
    logging.debug("Completed - Loading the params")

    logging.debug("Started - Connecting to the database")
    # connecting to the databse - stage 2
    pc = pineconeDB(index_name=params["pinecone"]["index_name"], api_key=os.getenv("PINECONE"), dimensions=1536 )
    pc.configureDB()
    index = pc.get_index()
    logging.debug("Completed - Connecting to the database")
    
    logging.debug("Started - Bedrock client configuration")
    #configuring the aws client object -  stage 3
    client  = Bedrock(
        service_name = params["aws"]["service_name"], 
        modelId=params["aws"]["modelId"],
        region_name = params["aws"]["region"], 
        aws_access_key_id = params["aws"]["aws_access_key_id"], 
        secret_access_key = params["aws"]["secret_access_key"]
        )
    bedrock_client = client.configure_get_client()
    logging.debug("Completed - Bedrock client configuration")

    logger.debug("Started - LLM configuration for aws")
    bedrock_client_llm = client.configure_get_llm_client()

    data = preprocess.generate_embedding_data(path = "data/mutula_fund.csv", generation_count=-1)
    logging.debug("Completed - Data Preprocessing")


    return index, bedrock_client, bedrock_client_llm, client, data

if __name__=="__main__":
    setup_base()

# q = "Zerodha Midcap Fund Month January 2024 Zerodha Large Cap Mid Cap Return (%) 11.44"
# output = client.query_pinecone(q, index, bedrock_client, top_k=3)
# print(output)
# # #updating the 


