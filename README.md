# Virtual-Research-Assistant

User Query
   ↓
LangGraph Agent
   ↓
Tool: Search Arxiv
   ↓
Tool: Extract Metadata
   ↓
Store Papers in Neo4j
   ├─ Graph structure
   └─ Vector embeddings
   ↓
Agent retrieves:
   ├─ vector similarity
   └─ graph relations
   ↓
LLM generates literature review


![alt text](image.png)