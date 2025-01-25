from src.utils import Utils
from dotenv import load_dotenv
import os

load_dotenv()

def load_params():
    """
    Load configuration parameters from a YAML file.
    """
    params = Utils.load_params("config.yaml")
    return params