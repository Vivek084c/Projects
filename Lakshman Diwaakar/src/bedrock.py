import boto3
import json
import os
import logging


# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('bedrock')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'bedrock.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


class Bedrock:
    def __init__(self, service_name, region_name, aws_access_key_id, secret_access_key ):
        self.service_name = service_name
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

        logger.debug("Completed - Returned the aws client")

        return bedrock
    

        

 