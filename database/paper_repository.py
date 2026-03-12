import re
import unicodedata
from database.neo4j_client import Neo4jClient


class PaperRepository:

    def __init__(self):
        self.db = Neo4jClient()

    def create_paper(self, paper: dict):
        query = """
        MERGE (p:Paper {id:$id})
        SET p.title = $title,
            p.summary = $summary,
            p.published = $published,
            p.url = $url
        """

        self.db.run_query(query, paper)

    @staticmethod
    def _normalize_author_id(name):
        # 1. Convert to lowercase and strip whitespace
        name = name.lower().strip()
        # 2. Normalize unicode (e.g., converts 'é' to 'e')
        name = unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('ascii')
        # 3. Replace non-alphanumeric characters with underscores
        name = re.sub(r'[^a-z0-9]+', '_', name)
        # 4. Strip trailing underscores
        return name.strip('_')
    
    def link_author(self, paper_id, author_name):
        author_id = self._normalize_author_id(author_name)

        query = """
        MERGE (a:Author {id:$author_id})
        SET a.name = $author_name
        WITH a
        MATCH (p:Paper {id:$paper_id})
        MERGE (a)-[:AUTHORED]->(p)
        """

        params = {
            "author_id": author_id,
            "author_name": author_name,
            "paper_id": paper_id
        }

        self.db.run_query(query, params)

    def link_category(self, paper_id, category):

        query = """
        MERGE (c:Category {name:$category})
        WITH c
        MATCH (p:Paper {id:$paper_id})
        MERGE (p)-[:BELONGS_TO]->(c)
        """

        params = {
            "category": category,
            "paper_id": paper_id
        }

        self.db.run_query(query, params)

    def create_chunk(self, chunk):

        query = """
        MATCH (p:Paper {id:$paper_id})
        MERGE (c:Chunk {id:$chunk_id})
        SET c.text = $text,
            c.embedding = $embedding
        MERGE (p)-[:HAS_CHUNK]->(c)
        """

        self.db.run_query(query, chunk)

    def link_chunks(self, chunk1, chunk2):

        query = """
        MATCH (c1:Chunk {id:$chunk1})
        MATCH (c2:Chunk {id:$chunk2})
        MERGE (c1)-[:NEXT_CHUNK]->(c2)
        """

        params = {
            "chunk1": chunk1,
            "chunk2": chunk2
        }

        self.db.run_query(query, params)