from database.neo4j_client import Neo4jClient
from models.embedding import embed_text


def retrieve_relevant_chunks(query: str, top_k: int = 5):

    db = Neo4jClient()

    embedding = embed_text(query)

    cypher = """
    CALL db.index.vector.queryNodes(
        'chunk_embedding_index',
        $top_k,
        $embedding
    )
    YIELD node, score

    MATCH (p:Paper)-[:HAS_CHUNK]->(node)
    OPTIONAL MATCH (a:Author)-[:AUTHORED]->(p)
    OPTIONAL MATCH (p)-[:BELONGS_TO]->(c:Category)

    RETURN
        p.id AS paper_id,
        p.title AS title,
        p.summary AS summary,
        collect(DISTINCT a.name) AS authors,
        collect(DISTINCT c.name) AS categories,
        node.text AS chunk_text,
        score
    ORDER BY score DESC
    """

    params = {
        "embedding": embedding,
        "top_k": top_k
    }

    results = db.run_query(cypher, params)

    documents = []

    for r in results:
        documents.append({
            "paper_id": r["paper_id"],
            "title": r["title"],
            "authors": r["authors"],
            "categories": r["categories"],
            "chunk_text": r["chunk_text"],
            "score": r["score"]
        })

    return documents