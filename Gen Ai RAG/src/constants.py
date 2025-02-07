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
    - Year (if specified)
    - Instrument Name (if applicable)
    - Percentage Allocation
    - Percentage Allocation Change
    - Instrument Count Across Funds
    - Category
    - Return (%)

    User Query: "{user_query}"

    Respond in the following precise format as a string output for use with the RAG model:
    Fund Name <Extracted Fund Name or null>
    Month <Extracted Month or null>
    Year <Extracted year or null>
    Instrument Name <Extracted Instrument Name or null>
    Percentage Allocation <Extracted Percentage Allocation or null>
    Percentage Allocation Change <Extracted Percentage Allocation Change or null>
    Instrument Count Across Funds <Extracted Instrument Count Across Funds or null>
    Category <Extracted Category or null>
    Return (%) <Extracted Return or null>
    """
    # Build payload for Bedrock API
    payload = {
        "inputText": llm_prompt,
        "textGenerationConfig": {
            "maxTokenCount": 60,
            "stopSequences": [],
            "temperature": 0.7,
            "topP": 0.9
        }
    }
    body = json.dumps(payload)

    # AWS Bedrock Model Invocation
    model_id = "amazon.titan-text-express-v1"
    response = bedrock_client_llm.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=body
    )
    item = response["body"].read()
    parsed_response = json.loads(item)
    output = parsed_response["results"][0]["outputText"]
    return output


# Function to process RAG response and provide insights
def process_rag_response(user_query, rag_response, bedrock_client_llm):
    """
    Process the RAG model's response and generate meaningful insights for the user query, 
    if required perform the necessary caluclations and return the response to user to answer his questions.
    
    Parameters:
        user_query (str): User's natural language query.
        rag_response (list): List of RAG output containing details about the funds.

    Returns:
        str: Insights and final verdict based on user input and RAG output.
    """
    # Prepare the LLM prompt for meaningful insights



    # llm_prompt = f"""
    # Based on the following user query and RAG model response, provide meaningful insights and perform mathematical calulations if specified in the user_query:
    
    # User Query: "{user_query}"
    
    # RAG Model Response:
    # {rag_response}
    
    # Analyze the data and include the following in your insights:
    # 1. Changes in percentage allocation for specified funds or instruments (if applicable).
    # 2. Recommended funds or instruments based on their consistency across funds.
    # 3. Overall returns or performance of the funds and instruments.
    
    # Provide a clear final verdict for the user query.
    # """

    llm_prompt = f"""
    You are given a user’s query and a RAG response. Based on the user’s query, extract the relevant 
    data from the RAG response and perform any necessary mathematical work (like subtraction, addition, etc.) if required to answer the query.
    User_Query:{user_query}
    RAG_Response:{rag_response}
    """



    # Build payload for Bedrock API
    payload = {
        "inputText": llm_prompt,
        "textGenerationConfig": {
            "maxTokenCount": 40,
            "stopSequences": [],
            "temperature": 0.2,
            "topP": 0.5
        }
    }
    body = json.dumps(payload)

    # AWS Bedrock Model Invocation
    model_id = "amazon.titan-text-express-v1"
    response = bedrock_client_llm.invoke_model(
        modelId=model_id,
        contentType="application/json",
        accept="application/json",
        body=body
    )
    item = response["body"].read()
    parsed_response = json.loads(item)
    output = parsed_response["results"][0]["outputText"]
    return output


