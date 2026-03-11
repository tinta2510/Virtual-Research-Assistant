from tools.search_arxiv import search_arxiv
from database.paper_repository import PaperRepository
from models.embeddings import embed_text

def ingest_topic(topic: str, max_results: int = 20):

    repo = PaperRepository()

    papers = search_arxiv(topic, max_results)

    for paper in papers:

        embedding = embed_text(f"Title: {paper.title}. Abstract: {paper.summary}")

        repo.create_paper(paper, embedding)

        print("Inserted:", paper.title)