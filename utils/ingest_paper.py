import os
from tools.arxiv_search import search_arxiv
from database.paper_repository import PaperRepository
from models.embedding import embed_text
from utils.chunk_text import chunk_text
from utils.handle_pdf import download_pdf, extract_pdf_text

def ingest_topic(topic: str, max_results: int = 5):

    repo = PaperRepository()

    papers = search_arxiv(topic, max_results)

    for paper in papers:

        print("Ingesting:", paper["title"])

        repo.create_paper(paper)

        # authors
        for author in paper["authors"]:
            repo.link_author(paper["id"], author)

        # category
        for category in paper["categories"]:
            repo.link_category(paper["id"], category)

        # chunk paper text
        pdf_path = download_pdf(paper["pdf_url"], paper["id"])
        full_text = extract_pdf_text(pdf_path)
        chunks = chunk_text(full_text)
        chunks = chunks[:10] # limit to 10 chunks for prototyping
        # remove pdf after processing
        if os.path.exists(pdf_path):
            os.remove(pdf_path)
        
        prev_chunk_id = None

        for i, chunk in enumerate(chunks):

            chunk_id = f"{paper['id']}_{i}"

            embedding = embed_text(chunk)

            repo.create_chunk({
                "paper_id": paper["id"],
                "chunk_id": chunk_id,
                "text": chunk,
                "embedding": embedding
            })

            if prev_chunk_id:
                repo.link_chunks(prev_chunk_id, chunk_id)

            prev_chunk_id = chunk_id