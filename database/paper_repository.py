from database.neo4j_client import Neo4jClient
from arxiv import paper

class PaperRepository:

    def __init__(self):
        self.db = Neo4jClient()

    def create_paper(self, paper: paper, embedding: list):
        """
        Parameters:
        - paper (arxiv.paper): The paper to be added to the database
        """
    
        query = """
        CREATE (p:Paper {
            entry_id: $entry_id,
            title: $title,
            abstract: $abstract,
            year: $year
            embedding: $embedding
        })
        """
        params = {
            "entry_id": paper.entry_id,
            "title": paper.title,
            # "authors": [author.name for author in paper.authors],
            "abstract": paper.summary,
            "year": paper.published.year,
            "embedding": embedding,
            # "journal_ref": paper.journal_ref,
            # "primary_category": paper.primary_category,
            # "categories": paper.categories,
        }

        self.db.run_query(query, params)