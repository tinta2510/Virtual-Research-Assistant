from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
        chunk_size=600,
        chunk_overlap=100,
        length_function=len,
        separators=["\n\n", "\n", ". ", " "]
    )


def chunk_text(text: str):
    return splitter.split_text(text)