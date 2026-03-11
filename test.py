from tools.vector_search import vector_search

query = "multihop reasoning"

papers = vector_search(query, top_k=1)

for p in papers:
    print("\nTitle:", p["title"])
    print("Score:", p["score"])