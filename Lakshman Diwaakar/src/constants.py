import openai
import json

# Function to query LLM for extraction
def extract_details_with_llm(user_query, bedrock_client_llm):
    """
    Extract details such as Fund Name, Month, Instrument Name, Percentage Allocation, 
    Percentage Allocation Change, Instrument Count Across Funds, Category, and Return (%) using an LLM.
    """
    llm_prompt = f"""
    Extract the following details from the user query:
    - Fund Name
    - Month (if specified)
    - Instrument Name (if applicable)
    - Percentage Allocation
    - Percentage Allocation Change
    - Instrument Count Across Funds
    - Category
    - Return (%)

    User Query: "{user_query}"

    Respond in the following precise format for use with the RAG model:
    Fund Name <Extracted Fund Name or null>
    Month <Extracted Month or null>
    Instrument Name <Extracted Instrument Name or null>
    Percentage Allocation <Extracted Percentage Allocation or null>
    Percentage Allocation Change <Extracted Percentage Allocation Change or null>
    Instrument Count Across Funds <Extracted Instrument Count Across Funds or null>
    Category <Extracted Category or null>
    Return (%) <Extracted Return or null>
    """
    
    # Call aws llm
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant."},
    #         {"role": "user", "content": llm_prompt}
    #     ]
    # )

    payload = {
        "inputText": llm_prompt, 
        "textGenerationConfig": {
            "maxTokenCount": 50,  # Adjust the maximum token count as needed
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
    
    # Parse the response
    extracted_details = response['choices'][0]['message']['content']
    return extracted_details