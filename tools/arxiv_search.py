import arxiv

def search_arxiv(query: str, max_results: int = 10):
    """
    Search papers from ArXiv
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )
    client = arxiv.Client()
    papers = []
    
    for result in client.results(search):
        papers.append({
            "id": result.entry_id.split("/")[-1],
            "title": result.title,
            "summary": result.summary,
            "published": result.published.year,
            "url": result.entry_id,
            "pdf_url": result.pdf_url,
            "authors": [a.name for a in result.authors],
            "categories": result.categories
        })

    return papers

if __name__ == "__main__":
    # Example usage
    results = search_arxiv("knowledge graph-based recommender", 3)

    print([result.title for result in results])
    