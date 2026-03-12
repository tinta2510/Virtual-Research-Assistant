from tools.retriever import retrieve_relevant_chunks

query = "methods to detect hallucination in large language models"

docs = retrieve_relevant_chunks(query)

for d in docs:

    print("\nTITLE:", d["title"])
    print("AUTHORS:", d["authors"])
    print("TEXT:", d["chunk_text"][:200])