import os
from openai import AzureOpenAI

from config import open_ai_endpoint, open_ai_key

def get_embedding(content): 
    client = AzureOpenAI(
        api_key = open_ai_key,  
        api_version = "2023-05-15",
        azure_endpoint = open_ai_endpoint, 
        azure_deployment="text-embedding"
    )

    response = client.embeddings.create(
        input = content,
        model= "text-embedding-ada-002"
    )

    embedding = response.data[0].embedding

    return embedding
