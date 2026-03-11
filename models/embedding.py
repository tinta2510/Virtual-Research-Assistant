from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def embed_text(text: str):
    return embedding_model.encode(text).tolist()