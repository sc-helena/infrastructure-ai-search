# import libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

from config import di_api_key, di_endpoint

def _read_pdfs_from_directory(directory_path):
    pdf_files = {}

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(directory_path, filename)
            # Read the file in binary mode
            with open(file_path, 'rb') as file:
                pdf_files[filename] = file.read()
    
    return pdf_files


def analyze_documents(directory_path):

    document_intelligence_client = DocumentIntelligenceClient(
        api_version="2024-11-30", endpoint=di_endpoint, credential=AzureKeyCredential(di_api_key)
    )

    file_binaries = _read_pdfs_from_directory(directory_path)

    result_texts = {}

    for filename, content in file_binaries.items():
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-read", AnalyzeDocumentRequest(bytes_source=content))

        result = poller.result()

        result_texts[filename] = result.content
    

    return result_texts

