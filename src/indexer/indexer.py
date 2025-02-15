from langchainSplitter.textSplitter import split_text
from embedder.embedder import get_embedding
import uuid

from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from config import ai_search_api_key, ai_search_endpoint, index_name

def _create_index_entries(splitted_texts, filename):
    documents = []
    for splitted_text in splitted_texts:

        index_mask = {
            "id": str(uuid.uuid4()),
            "embeddedContent": get_embedding(splitted_text),
            "content": splitted_text,
            "filename": filename
        }

        documents.append(index_mask)

    return documents

def upload_documents(texts):
       
       for filename, text in texts.items():

            splitted_texts = split_text(text)
            documents = _create_index_entries(splitted_texts, filename)
        
            search_client = SearchClient(endpoint=ai_search_endpoint,
                        index_name=index_name,
                        credential=AzureKeyCredential(ai_search_api_key))
            try:
                result = search_client.upload_documents(documents=documents)
                print("Upload of new document succeeded: {}".format(result[0].succeeded))
            except Exception as e:
                print(e)

