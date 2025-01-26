# connection_manager.py
from setup import setup_get_config

class ConnectionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConnectionManager, cls).__new__(cls)
            cls._instance.initialize_connections()
        return cls._instance

    def initialize_connections(self):
        print("Initializing connections...")
        self.index, self.bedrock_client_embedding, self.bedrock_client_llm, self.client, self.data= setup_get_config()
        print("Connections initialized.")

    def get_connections(self):
        return self.index, self.bedrock_client_embedding, self.bedrock_client_llm, self.client, self.data

# Singleton access method
def get_connection_manager():
    return ConnectionManager()