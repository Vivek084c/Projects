## Gen Ai RAG
|– Gen Ai RAG/                   
|–---- aws/                   
|–---- data/                   
|–---- logs/                   
|–---- reserch/                   
|–---- src/                   
|–---- connection_manager.py                   
|–---- main.py                   
|–---- ping.py                   

## Project Overview

I have integrated AWS Bedrock to develop a GenAI RAG-based application that processes user queries related to mutual fund data. The application leverages Amazon Titan LLM to parse queries, generates embeddings using an embedding model, and performs similarity searches in Pinecone to provide accurate responses.

## How It Works

1. **Query Parsing:**  
   The user query is parsed using Amazon Titan LLM.
   
2. **Embedding Generation:**  
   The output from the LLM is passed to an embedding generation model to create embeddings.
   
3. **Similarity Search:**  
   The generated embeddings are stored in the Pinecone vector database for performing similarity searches.

4. **Response Generation:**  
   Based on the search results, the LLM processes the output along with the original query, providing relevant responses to the user.

The system is designed to be scalable, future-proof, and highly efficient.

## Software Practices

- **Environment Management:**  
  Utilized a separate `.env` file for environment variables to ensure smooth configuration management.

- **Configuration Files:**  
  Maintained a dedicated config file for project settings to keep the configuration centralized and easily modifiable.

- **Clean and Scalable Pipeline:**  
  Ensured the code follows best practices for scalability and future-proofing, with a modular, maintainable pipeline for future enhancements.

- **Logging:**  
  Added logging to help users debug the application more effectively. This provides traceability and better error handling for users when running the app.

- **Deployment as Utility:**  
  With the environment variables and config files properly set up, the application can be easily deployed as a utility for various use cases.

## Future Integration

In the future, we can integrate **forecasting algorithms** to predict trends related to mutual fund data. Some potential forecasting algorithms include:

1. **ARIMA (AutoRegressive Integrated Moving Average):**  
   ARIMA can be used to forecast future values of mutual fund performance based on historical data. It combines autoregression and moving averages to predict future values, which could be beneficial for forecasting fund returns.

   *Integration Approach:* We can train the ARIMA model on historical fund return data, and use it to predict future percentage allocations and returns for specific mutual funds.

2. **Prophet (by Facebook):**  
   Prophet is a time-series forecasting algorithm that is robust to missing data and changes in trend. It can be useful for predicting long-term trends in mutual fund performance, including seasonality and holiday effects.

   *Integration Approach:* Prophet can be integrated by using historical monthly performance data to make future predictions about fund performance. The predictions could then be incorporated into the current system to enhance decision-making.

3. **LSTM (Long Short-Term Memory):**  
   LSTM, a type of recurrent neural network, is particularly effective for sequential data like time series. It can learn patterns in mutual fund performance over time and predict future trends.

   *Integration Approach:* An LSTM model could be trained on past mutual fund performance data and then used to predict future fund allocations and returns. The predictions can be fed into the existing pipeline to provide users with actionable insights.


These forecasting models will be integrated into the existing pipeline, allowing for more advanced analytics and predictions based on historical data.



## FastAPI Blog
               

├FastAPI Blog   
├── pycache       
├── database.py  
├── main.py    
├── model.py     
├── requirements.txt    
├── test.txt            

## Project Overview

This FastAPI application provides a CRUD API for managing blog posts stored in MongoDB. It supports creating, retrieving (single/all), updating, and deleting blogs asynchronously. The Blog and UpdateBlog models define validation rules. The database connection uses Motor (AsyncIOMotorClient). Each API route interacts with MongoDB, converting documents using blog_helper for consistency.

## Techonologies Used
📌 Technologies Used

1️⃣ FastAPI 

A high-performance web framework for building APIs with Python, using asynchronous capabilities and automatic OpenAPI documentation for quick API development.

2️⃣ Pydantic 

Used for data validation and serialization; ensures correct input structure for Blog models using BaseModel, enforcing field constraints and types.

3️⃣ MongoDB 

A NoSQL document database used to store blog posts as JSON-like objects, providing flexibility and scalability for dynamic content management.

4️⃣ Motor (AsyncIOMotorClient) 

An asynchronous Python driver for MongoDB, enabling non-blocking database operations, improving efficiency and performance in FastAPI applications handling concurrent requests.

5️⃣ Bson & ObjectId 

bson (Binary JSON) handles MongoDB’s native data format, and ObjectId uniquely identifies each document in the database for efficient querying.


## How It Works


1️⃣ Request Handling (20 words)
The FastAPI server receives an API request for creating, retrieving, updating, or deleting blog posts and routes it accordingly.

2️⃣ Data Validation (20 words)
The request data is validated using Pydantic models (Blog and UpdateBlog), ensuring correct field constraints, data types, and required fields.

3️⃣ Database Interaction (20 words)
The API uses Motor (AsyncIOMotorClient) to perform asynchronous CRUD operations on the MongoDB database, ensuring non-blocking execution.

4️⃣ Data Processing (20 words)
Retrieved MongoDB documents are converted into structured Python dictionaries using the blog_helper function to maintain a consistent API response format.

5️⃣ Response Generation (20 words)
The API returns a structured JSON response with blog data or an HTTPException if the requested blog post is not found.

=======
These forecasting models will be integrated into the existing pipeline, allowing for more advanced analytics and predictions based on historical data.