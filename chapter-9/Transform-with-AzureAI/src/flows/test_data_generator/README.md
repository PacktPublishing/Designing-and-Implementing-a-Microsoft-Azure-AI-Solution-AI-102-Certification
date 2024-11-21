# Topic-based Question Generation Flow
This flow is designed to generate a set of questions based on a specific topic, leveraging the capabilities of Large Language Models (LLMs) to ensure relevance and quality. It's an advanced application of chat flow, focusing on creating educational or informational content that can be used in quizzes, learning platforms, or conversational AI.

## Create Connection for LLM Tool
To utilize an LLM tool for generating questions, you first need to establish a connection. Supported connection types include "AzureOpenAI" and "OpenAI".

- **AzureOpenAI**: Requires creating an Azure OpenAI service. For setup, visit [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service/).
- **OpenAI**: Requires an OpenAI account. For setup, visit [OpenAI](https://platform.openai.com/).

```bash
# To avoid yaml file changes, override keys with --set
# For OpenAI
pf connection create --file openai.yaml --set api_key=<your_api_key> --name open_ai_connection

# For Azure OpenAI
pf connection create --file azure_openai.yaml --set api_key=<your_api_key> api_base=<your_api_base> --name azure_open_ai_connection
```

Ensure the connection named `open_ai_connection` or `azure_open_ai_connection` is used in your [flow.dag.yaml](flow.dag.yaml).

```bash
# To view the registered connection
pf connection show --name open_ai_connection
# Or for Azure OpenAI
pf connection show --name azure_open_ai_connection
```

For managing connections, refer to the [connections document](https://promptflow.azurewebsites.net/community/local/manage-connections.html) and [examples](https://github.com/microsoft/promptflow/tree/main/examples/connections).

## Developing a Topic-based Question Generation Flow

This flow involves the following key steps:

1. **Specify Topic**: Define the topic for which questions are to be generated. This could be anything from "Python programming" to "18th-century European history".

2. **Generate Questions**: Use the LLM tool connected to generate a set of questions relevant to the specified topic. Ensure the prompt to the LLM is clear about the topic and the type of questions desired (e.g., multiple choice, true/false, short answer).

3. **Review and Refine**: Review the generated questions for relevance and accuracy. Optionally, refine the questions or generate additional questions as needed.

4. **Output**: The final set of questions can be outputted to a desired format, such as JSON, for use in applications or stored for future reference.

This flow enables the rapid creation of educational content, making it easier for educators, content creators, and conversational AI developers to generate topic-specific questions efficiently and effectively.