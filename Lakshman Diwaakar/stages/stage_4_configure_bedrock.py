from src.bedrock import Bedrock

def configure_bedrock(params):
    """
    Configure the Bedrock client object.
    """
    client = Bedrock(
        service_name=params["aws"]["service_name"],
        modelId=params["aws"]["modelId"],
        region_name=params["aws"]["region"],
        aws_access_key_id=params["aws"]["aws_access_key_id"],
        secret_access_key=params["aws"]["secret_access_key"],
    )
    bedrock_client = client.configure_get_client()
    print("Bedrock client configured.")
    return bedrock_client