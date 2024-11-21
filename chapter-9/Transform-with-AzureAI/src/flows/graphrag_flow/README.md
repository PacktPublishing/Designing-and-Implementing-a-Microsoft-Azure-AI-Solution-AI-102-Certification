# Graphrag Flow
GraphRAG is a new approach to Retrieval-Augmented Generation (RAG) using graph databases. It builds upon the capabilities of standard RAG by leveraging the strengths of graph databases for enhanced data retrieval and relationship management. With GraphRAG, you can efficiently create a system that handles complex queries and provides more accurate and contextually relevant responses by utilizing the interconnected nature of graph data.

## Create Graphrag connection  to use
You can follow these steps to create a connection required to the GraphRag service.

Use a custom connection `CustomConnection`

- endpoint : APIM endpoint for GraphRag Service
- api_key : APIM subscription key for GraphRag Service


## GraphRag Flow
- graph_conn : Connection of the graphrag service 
- index_name : GraphRag index to search.

## Execute Flow
- Inputs:
  - question - Query to perform agains the specified GraphRag `index_name`

- Outputs:
  - Answer - Full response from graphrag query, includes generated response in addition to referenced graph docs. 
