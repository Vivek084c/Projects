import yaml
import os
import logging
import json

# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('utils')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'utils.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

class Utils:
        
    def load_params(params_path: str) -> dict:
        """Load parameters from a YAML file."""
        try:
            with open(params_path, 'r') as file:
                params = yaml.safe_load(file)
            logger.debug('Parameters retrieved from %s', params_path)
            return params
        except FileNotFoundError:
            logger.error('File not found: %s', params_path)
            raise
        except yaml.YAMLError as e:
            logger.error('YAML error: %s', e)
            raise
        except Exception as e:
            logger.error('Unexpected error: %s', e)
            raise

    def getresponse(bedrock_client_llm, inputPrompt,max_tokens=30):
        payload = {
        "inputText": inputPrompt, 
        "textGenerationConfig": {
            "maxTokenCount": max_tokens,  # Adjust the maximum token count as needed
            "stopSequences": [],   # List of stop sequences
            "temperature": 0.7,    # Temperature for randomness
            "topP": 1              # Top-p sampling parameter
        }
        }

        body = json.dumps(payload)

        model_id = "amazon.titan-text-lite-v1"
        respnse  = bedrock_client_llm.invoke_model(
            modelId = model_id,
            contentType = "application/json",
            accept = "application/json",
            body = body
        )
        item = respnse["body"].read()
        i = json.loads(item)
        output = i["results"][0]["outputText"]
        return output

        

    