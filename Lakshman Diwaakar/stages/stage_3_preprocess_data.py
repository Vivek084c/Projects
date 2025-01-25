from src.PreProcess import preprocess

def preprocess_data():
    """
    Generate embedding data from a CSV file.
    """
    data = preprocess.generate_embedding_data(
        path="data/mutula_fund.csv", 
        generation_count=5
    )
    print(data)
    print(f"Type of processed data: {type(data)}")
    return data