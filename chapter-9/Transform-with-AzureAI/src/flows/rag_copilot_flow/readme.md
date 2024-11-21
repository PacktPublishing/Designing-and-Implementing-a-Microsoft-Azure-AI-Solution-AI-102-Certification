# Template Chat Flow README

## Overview

The Template Chat Flow is designed to facilitate interactive chat experiences by processing user queries and fetching relevant documents to generate informed responses. This flow is particularly useful for applications requiring access to a vast repository of information, enabling them to provide context-aware responses based on the content of fetched documents.

## Flow Description

- **ID**: `template_chat_flow`
- **Name**: Template Chat Flow
- **Environment**:
    - Utilizes a `python_requirements_txt` file named `requirements.txt` for managing Python dependencies.

## Inputs

   - `inputs` contain the `query` made by the user.
   - `outputs`:
        - `current_query_intent`: This field captures the intent of the user's query, providing a clear understanding of what the user is asking for. It's crucial for tailoring the search for relevant documents and for shaping the generated response to be as informative and helpful as possible.

        - `fetched_docs`: Contains a list of documents fetched based on the query's intent. Each document is selected for its relevance to the query, ensuring that the information used to generate responses is accurate and pertinent. This list includes document identifiers, titles, and snippets of content that are directly related to the user's query.

        - `generated_response`: This is the final output of the flow, where a response is crafted using the information gathered from the `fetched_docs`. The response is designed to directly answer the user's query or provide them with information that is relevant to their request. The generation of this response takes into account the context of the conversation, the user's intent, and the most relevant information extracted from the fetched documents.


### Example Input

```yaml
- inputs:
        query: how old do I need to be to drive?