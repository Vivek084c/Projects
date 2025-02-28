# Gen Ai RAG
Vivek084c: write a readme file with a file directory structure, create a basic 100 words detailed explaination of what code is doing and how it is doing it. add necessry details where ever necessary

Workspace: Collecting workspace information# Project README

## Directory Structure

```
__pycache__/
    connection_manager.cpython-311.pyc
    setup.cpython-311.pyc
aws/
    temp.ipynb
    test.json
connection_manager.py
data/
    data_nov.xlsx
    data_sep.xlsx
    Finance_data.csv
    mutula_fund.csv
    Original_data.csv
logs/
    bedrock.log
    connectDB.log
    PreProcess.log
    setup.log
    utils.log
main.py
ping.py
reserch/
    aws.ipynb
    temp.ipynb
setup.py
src/
    __pycache__/
        bedrock.cpython-311.pyc
        connectDB.cpython-311.pyc
        ...
    bedrock.py
    connectDB.py
    constants.py
    PreProcess.py
    utils.py
```

## Project Overview

This project is designed to preprocess financial data, configure AWS Bedrock clients, and interact with Pinecone for vector database operations. The main components include data preprocessing, AWS client configuration, and database interactions.

### Key Components

1. **Data Preprocessing**: The `preprocess` class in PreProcess.py reads CSV files and generates embedding data.
2. **AWS Bedrock Client Configuration**: The `Bedrock` class in bedrock.py configures AWS clients for embedding and LLM operations.
3. **Pinecone Database Interaction**: The `pineconeDB` class in connectDB.py manages connections and operations with the Pinecone vector database.

### How It Works

1. **Setup**: The setup.py script initializes logging, loads configuration parameters from a YAML file, and sets up the database and AWS clients.
2. **Data Preprocessing**: The `generate_embedding_data` method in the `preprocess` class reads financial data from CSV files and generates embedding data for further processing.
3. **AWS Client Configuration**: The `Bedrock` class configures AWS clients for embedding and LLM operations, enabling interaction with AWS services.
4. **Database Operations**: The `pineconeDB` class handles connections to the Pinecone vector database, allowing for data upsert and query operations.

### Running the Project

To run the project, execute the setup.py script:

```sh
python setup.py
```

This will initialize the necessary configurations and start the data preprocessing and database setup processes.

Vivek084c: write a readme file with a file directory structure, create a basic 100 words detailed explaination of what code is doing and how it is doing it. add necessry details where ever necessary

GitHub Copilot: Enable Claude 3.5 Sonnet (Preview) for all clients
Enable access to the latest Claude 3.5 Sonnet model from Anthropic. [Learn more about how GitHub Copilot serves Claude 3.5 Sonnet](https://docs.github.com/copilot/using-github-copilot/using-claude-sonnet-in-github-copilot).

Vivek084c: @GitHubCopilot Enable: "Enable Claude 3.5 Sonnet (Preview) for all clients"

GitHub Copilot: # RAG Implementation with AWS Bedrock and Pinecone

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) system using AWS Bedrock and Pinecone vector database. It processes financial data, generates embeddings, and enables semantic search capabilities.

## Directory Structure
```
.
├── aws/
│   ├── temp.ipynb
│   └── test.json
├── data/
│   ├── Finance_data.csv
│   ├── Original_data.csv
│   └── mutula_fund.csv
├── logs/
│   ├── bedrock.log
│   ├── connectDB.log
│   └── setup.log
├── src/
│   ├── bedrock.py
│   ├── connectDB.py
│   ├── constants.py
│   ├── PreProcess.py
│   └── utils.py
├── connection_manager.py
├── main.py
├── ping.py
└── setup.py
```

## Core Components

### 1. Data Processing (`src/PreProcess.py`)
```python
# Handles data preprocessing and embedding generation
- Reads financial CSV data
- Cleans and formats text data
- Generates embeddings using AWS Bedrock
```

### 2. AWS Bedrock Integration (`src/bedrock.py`)
```python
# Manages AWS Bedrock client operations
- Configures AWS credentials
- Handles embedding generation requests
- Manages Claude LLM interactions
```

### 3. Pinecone Database (`src/connectDB.py`)
```python
# Manages vector database operations
- Initializes Pinecone connection
- Handles vector upsert operations
- Performs similarity searches
```

## Setup and Configuration

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure AWS credentials:
```bash
aws configure
```

3. Set environment variables:
```bash
export PINECONE_API_KEY='your-api-key'
export AWS_REGION='your-region'
```

## Usage

1. Initialize the system:
```python
python setup.py
```

2. Run the main application:
```python
python main.py
```

## Logging
All operations are logged in the logs directory:
- `bedrock.log`: AWS Bedrock operations
- `connectDB.log`: Database operations
- `setup.log`: System initialization

## Key Features
- Document embedding generation
- Semantic search capabilities
- Vector database management
- AWS Bedrock LLM integration
- Robust logging system

## Requirements
- Python 3.8+
- AWS Account with Bedrock access
- Pinecone account
- Required Python packages in requirements.txt

## Error Handling
The system includes comprehensive error handling for:
- AWS service interruptions
- Database connection issues
- Data preprocessing errors

For detailed implementation and usage examples, refer to the Jupyter notebooks in the `/aws` directory.

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



# FastAPI Blog
               

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


# Custom Neural Network Implementation

## Overview
A custom implementation of a neural network using TensorFlow for binary classification on MNIST dataset. The network features an entropy-based approach with custom dense layers and activation functions, demonstrating both custom and TensorFlow-based solutions for even/odd digit classification.

## Directory Structure
```
.
├── custom_neural_netowrk_final.ipynb    # Main implementation notebook
├── requirements.txt                     # Project dependencies
└── README.md                           # Project documentation
```

## Features
- Custom Dense Layer Implementation
- Binary Cross-Entropy Loss Function
- Sigmoid Activation Layer
- GPU Acceleration Support
- Performance Benchmarking

## Requirements
```
tensorflow>=2.10.0
numpy>=1.21.0
matplotlib>=3.5.0
scikit-learn>=1.0.0
jupyter>=1.0.0
```

## Installation

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Mac/Linux
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `custom_neural_netowrk_final.ipynb`

3. Run all cells sequentially

## Implementation Details
- Input Layer: 784 neurons (28x28 MNIST images)
- Hidden Layer: Custom dense implementation
- Output Layer: Binary classification (Even/Odd)
- Training: Custom gradient tape implementation
- Optimization: Adam optimizer

## Performance
- Training accuracy(On custom neural network): ~89.03%
- Training accuracy(On pre-build neural network): ~86.26%


## License
MIT License

## Author
Vivek Choudhry