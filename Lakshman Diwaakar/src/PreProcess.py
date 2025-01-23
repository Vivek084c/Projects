import pandas as pd
import json

class preprocess:
    def generate_embedding_data(self,path):
        df = pd.read_csv(path)
        clms = list(df.columns)
        no_of_rows = len(df.iloc[:,0:1])
        embedding_data = []
        for i in range(no_of_rows):
            data = list(df.iloc[i,:])
            s = ""
            for j in range(len(clms)):
                s+=" "+str(clms[j])+" "+str(data[j])
            embedding_data.append(s)
            if i>=1:
                break

        data = [{"id": f"item-{i+1}", "text": embedding_data[i]} for i in range(len(embedding_data))]
        for i in data:
            print(i)
        return data

    def generate_titan_embedding(self,text, bedrock, TITAN_EMBEDDING_MODEL):
        """
        Retures the Embedding data for a given text
        Args:
            text -  the input text
            bedrock - Bedrock client for AWS
            TITAN_EMBEDDING_MODEL - Embedding model name
        Returs:
            Embedding vector (dimension 1536)
        """
        response = bedrock.invoke_model(
            modelId=TITAN_EMBEDDING_MODEL,
            contentType="application/json",
            accept="application/json",
            body=json.dumps({"inputText": text})
        )
        result = json.loads(response["body"].read())
        return result["embedding"]  # Embedding vector
    
    def upsert_to_pinecone(self,data, index):
        """
        Data should be a list of dictionaries, where each dictionary contains:
        - 'id': unique ID for the item
        - 'text': the text to embed
        - 'index' : the index for the pinecone server
        """
        for item in data:
            text = item["text"]
            embedding = self.generate_titan_embedding(text)
            index.upsert(vectors=[(item["id"], embedding)])