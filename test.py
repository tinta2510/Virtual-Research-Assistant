from utils.ingest_paper import ingest_topic

if __name__ == "__main__":

    topic = "knowledge graph-based recommender"

    ingest_topic(topic, max_results=10)