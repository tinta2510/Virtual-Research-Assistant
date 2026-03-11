// Create Vector Index
CREATE VECTOR INDEX paper_embedding_index
FOR (p:Paper)
ON (p.embedding)
OPTIONS {
 indexConfig: {
   `vector.dimensions`: 384,
   `vector.similarity_function`: 'cosine'
 }
}