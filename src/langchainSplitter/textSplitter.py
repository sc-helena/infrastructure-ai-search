from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_text(text, chunk_size=1000 , chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False,
    )

    splitted_text = text_splitter.split_text(text)

    return splitted_text