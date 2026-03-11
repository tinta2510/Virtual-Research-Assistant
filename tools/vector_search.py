import time
from database.neo4j_client import Neo4jClient
from models.embedding import embed_text

def vector_search(query: str, top_k: int = 5):
    db = Neo4jClient()
    
    query_embedding = embed_text(query)

    cypher = """
    CALL db.index.vector.queryNodes(
        'paper_embedding_index',
        $top_k,
        $embedding
    )
    YIELD node, score
    RETURN node.title AS title,
           node.abstract AS abstract,
           node.year AS year,
           node.entry_id AS entry_id,
           score
    """

    params = {
        "embedding": query_embedding,
        "top_k": top_k
    }

    results = db.run_query(cypher, params)

    papers = []

    for r in results:
        papers.append({
            "entry_id": r["entry_id"],
            "title": r["title"],
            "abstract": r["abstract"],
            "year": r["year"],
            "score": r["score"]
        })

    return papers