## <p align="right">**Chapter 7**</p>

1. Which component in Azure AI Search is responsible for creating and managing the search index?<br><br>

<!-- -->
<ol type="A">
<li>Indexer </li>
<li>Skillset </li>
<li>Synonym Map </li>
<li>Analyzer</li>
</ol>

<br>

<ins>Correct answer: C</ins>
In Azure AI Search, the Indexer component is responsible for creating and managing the search index

##
2. What feature in Azure AI Search allows you to improve search relevance by re-ranking search results based on semantic understanding? <br><br>

<!-- -->
<ol type="A">
<li>Vector Search </li>
<li>Semantic Reranking   </li>
<li>Custom Skill </li>
<li>Indexer </li>
</ol>

<br>

<ins>Correct answer: C</ins>
In Azure AI Search, the feature that allows you to improve search relevance by re-ranking search results based on semantic understanding is Semantic Reranking.

##
3. You are creating an index that includes a field named modified_date. You want to ensure that the modified_date field can be included in search results. Which attribute must you apply to the modified_date field in the index definition? <br><br>

<!-- -->
<ol type="A">
<li>Filterable</li>
<li>Sortable</li>
<li>Facetable</li>
<li>Retrievable </li>
</ol>

<br>

<ins>Correct answer: D</ins>
To ensure that the modified_date field can be included in search results, you must apply the "retrievable" attribute to the field in the index definition.

##
4. You have created a data source and an index. What must you create to map the data values in the data source to the fields in the index? <br><br>

<!-- -->
<ol type="A">
<li>Indexer</li>
<li>Skillset</li>
<li>Synonym Map</li>
<li>Analyzer</li>
</ol>

<br>

<ins>Correct answer: A</ins>
To map the data values in the data source to the fields in the index, you must create an Indexer. The indexer is responsible for mapping source data to the appropriate fields in the index during the indexing process.

##
5. You want to create a search solution that uses a built-in AI skill to determine the language in which each indexed document is written, and enrich the index with a field indicating the language. Which kind of Azure AI Search object must you create? <br><br>

<!-- -->
<ol type="A">
<li>Indexer</li>
<li>Skillset</li>
<li>Synonym Map</li>
<li>Analyzer</li>
</ol>

<br>

<ins>Correct answer: B</ins>
To create a search solution that uses a built-in AI skill to determine the language in which each indexed document is written and enrich the index with a field indicating the language, you must create a Skillset. Skillsets allow you to attach various AI skills, including language detection, to the indexing process.

##
## <p align="right">**Chapter 8**</p>

1. Which key values are required to use the SDK to send a prompt message and get a response from Azure OpenAI Service?<br><br>

<!-- -->
<ol type="A">
<li>api_key, api_version, azure_endpoint </li>
<li>subscription_id, resource_group, api_version </li>
<li>client_id, client_secret, azure_endpoint </li>
<li>tenant_id, subscription_id, api_key</li>
</ol>

<br>

<ins>Correct answer: A</ins>
In order to use the SDK to send a prompt message and get a response from Azure OpenAI Service, you need the following key values: api_key, api_version, and azure_endpoint. 

##

2. Which steps should you take to configure parameters to optimize a generative AI model's behavior for consistent responses from a LLM?<br><br>

<!-- -->
<ol type="A">
<li>Use untrusted data sources, enable full access to sensitive resources, and avoid setting strict parameters. </li>
<li>Provide trusted data, configure custom parameters such as "strictness" and "limit responses to data content," and augment prompts with data retrieved from trusted sources.</li>
<li>Disable logging and monitoring of LLM interactions and allow unrestricted input length and structure. </li>
<li>Restrict usage rate limits to a minimum and avoid human review of outputs before dissemination.</li>
</ol>

<br>

<ins>Correct answer: B</ins>
To optimize a generative AI model's behavior for consistent responses from an LLM, you should: <br>
<ul>
<li>Provide trusted data: Ensure that the data used for training and responses is reliable and relevant. </li>
<li>Configure custom parameters: Adjust settings such as "strictness" and "limit responses to data content" to tailor the model's behavior to specific use cases.</li>
<li>Augment prompts with data from trusted sources: Use features like Azure OpenAI "on your data" to enhance the accuracy and groundedness of the responses.</li>
</ul>

##   


3. Which of the following outlines the correct steps for implementing the RAG pattern to generate accurate answers based on user data?<br><br>

<!-- -->
<ol type="A">
<li>Store all possible answers within the model itself, send user questions directly to the model, and rely on its pre-trained data for responses. </li>
<li>Search a data store based on user input, combine the user question with matching results, send the combined data and question as a prompt to the LLM, and then generate the desired answer.</li>
<li>Use the model to generate responses without any data retrieval, update the model periodically with new data, and ensure responses are based solely on updated model knowledge. </li>
<li>Retrieve data randomly, send it to the LLM without combining with user input, and rely on the model to filter out irrelevant information.</li>
</ol>

<br>

<ins>Correct answer: B</ins>
The correct steps for implementing the RAG pattern are: <br>
<ul>
<li>Search a data store based on user input: This involves querying your data repository to find relevant information that matches the user's question. </li>
<li>Combine the user question with matching results: Once relevant data is retrieved, it is combined with the user’s question to create a comprehensive prompt. </li>
<li>Send the combined data and question as a prompt to the LLM: This prompt is then sent to the LLM, which uses the provided context to generate a more accurate and relevant response.</li>
<li>IV.	Generate the desired answer: The LLM processes the prompt and generates a response based on the combined data and user input.</li>
</ul>

##   

4. Which of the following outlines the best approach to optimize the search process in the RAG pattern?<br><br>

<!-- -->
<ol type="A">
<li>Use a randomly ordered data store, avoid indexing, and rely solely on keyword searches to retrieve data. </li>
<li>Implement an index that includes keyword searches, semantic searches, and vector searches, and ensure the index is optimized for efficient retrieval.</li>
<li>Depend on the pre-trained knowledge of the LLM without utilizing any external data sources or indexes. </li>
<li>Use a basic text search algorithm without incorporating semantic or vector search capabilities.</li>
</ol>

<br>

<ins>Correct answer: B</ins>
The best approach to optimize the search process in the RAG pattern involves: <br>
<ul>
<li>Implementing an index: This allows for efficient retrieval of data. </li>
<li>Including keyword searches, semantic searches, and vector searches: These search capabilities ensure that the most relevant and accurate data is retrieved. </li>
<li>o	Ensuring the index is optimized for efficient retrieval: This involves using an embedding model to convert text data into number sequences (vectors), which improves the search efficiency and relevance.</li>
</ul>

##   