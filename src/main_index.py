from indexing.index import create_index
from ocr.pdfReader import analyze_documents
from indexing.indexer import upload_documents

from config import assets_path

if __name__ == "__main__":

    create_index()

    # extract text from pdfs
    texts_per_document = analyze_documents(assets_path)

    upload_documents(texts_per_document)
    

