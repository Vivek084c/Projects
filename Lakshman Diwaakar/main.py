from src.connectDB import pineconeDB
from src.PreProcess import preprocess
from src.utils import Utils
from src.bedrock import Bedrock
from dotenv import load_dotenv
import os
load_dotenv()
import json
# connecting to the databse


# pc = pineconeDB(index_name="lakshmandiwakar", api_key=os.getenv("PINECONE"), dimensions=1536 )
# pc.configureDB()
# data = preprocess.generate_embedding_data("data/mutula_fund.csv")
# preprocess.generate_titan_embedding(data, )

params = Utils.load_params("config.yaml")

client  = Bedrock(
    service_name = params["aws"]["service_name"], 
    region_name = params["aws"]["region"], 
    aws_access_key_id = params["aws"]["aws_access_key_id"], 
    secret_access_key = params["aws"]["secret_access_key"]
    )
bedrock_client = client.configure_get_client()



payload = {
    "inputText": "What is the capital of india", 
    "textGenerationConfig": {
        "maxTokenCount": 30,  # Adjust the maximum token count as needed
        "stopSequences": [],   # List of stop sequences
        "temperature": 0.7,    # Temperature for randomness
        "topP": 1              # Top-p sampling parameter
    }
}


body = json.dumps(payload)
model_id = "amazon.titan-text-lite-v1"

respnse  = bedrock_client.invoke_model(
    modelId = model_id,
    contentType = "application/json",
    accept = "application/json",
    body = body
)

item = respnse["body"].read()
i = json.loads(item)

print(i["results"][0]["outputText"])


