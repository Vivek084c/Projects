import boto3
import json

prompt_data = """ 
what is the capital of india.?
"""


bedrock = boto3.client(service_name = "bedrock-runtime")

body = {
    "inputText": "What is the capital of india", 
    "textGenerationConfig": {
        "maxTokenCount": 30,  # Adjust the maximum token count as needed
        "stopSequences": [],   # List of stop sequences
        "temperature": 0.7,    # Temperature for randomness
        "topP": 1              # Top-p sampling parameter
    }
}

body = json.dumps(body)
model_id = "amazon.titan-text-lite-v1"

respnse  = bedrock.invoke_model(
    modelId = model_id,
    contentType = "application/json",
    accept = "application/json",
    body = body
)


item = respnse["body"].read()
i = json.loads(item)
print(i["results"][0]["outputText"])