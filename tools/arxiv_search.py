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
    
    return list(client.results(search))

if __name__ == "__main__":
    # Example usage
    results = search_arxiv("knowledge graph-based recommender", 3)

    print([result.title for result in results])
    