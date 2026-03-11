from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

class Neo4jClient:

    def __init__(self):
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")

        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def run_query(self, query: str, params: dict = {}):
        with self.driver.session() as session:
            result = session.run(query, params)
            return result.data()

    def close(self):
        self.driver.close()