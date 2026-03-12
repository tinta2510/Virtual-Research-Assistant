// Paper primary key
CREATE CONSTRAINT paper_id IF NOT EXISTS
FOR (p:Paper)
REQUIRE p.id IS UNIQUE;

// Author primary key
CREATE CONSTRAINT author_id IF NOT EXISTS
FOR (a:Author)
REQUIRE a.id IS UNIQUE;

// Category primary key
CREATE CONSTRAINT category_name IF NOT EXISTS
FOR (c:Category)
REQUIRE c.name IS UNIQUE;

// Chunk primary key
CREATE CONSTRAINT chunk_id IF NOT EXISTS
FOR (ch:Chunk)
REQUIRE ch.id IS UNIQUE;

// Full-text index on Paper title and abstract
CREATE FULLTEXT INDEX paper_text_index IF NOT EXISTS
FOR (n:Paper)
ON EACH [n.title, n.summary];

// Vector index on Chunk embedding
CREATE VECTOR INDEX chunk_embedding_index IF NOT EXISTS
FOR (c:Chunk) ON (c.embedding)
OPTIONS {
 indexConfig: {
  `vector.dimensions`: 384,
  `vector.similarity_function`: 'cosine'
 }
};