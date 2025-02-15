from ocr.pdfReader import analyze_documents
from indexer.indexer import upload_documents
from config import assets_path

if __name__ == "__main__":
    # extract text from pdfs
    texts_per_document = analyze_documents(assets_path)

    # upload to index
    upload_documents(texts_per_document)