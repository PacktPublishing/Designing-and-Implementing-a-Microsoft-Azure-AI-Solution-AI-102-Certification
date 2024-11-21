# Copilot application that implements RAG

This is a sample copilot that application that implements RAG via custom Python code, and can be used with the Azure AI Studio. This sample aims to provide a starting point for an enterprise copilot grounded in custom data that you can further customize to add additional intelligence or capabilities.  

Following the below steps, you will: set up your development environment, create or reference your Azure AI resources, explore prompts, build an index containing product information, run your copilot, evaluate it, and deploy your copilot to a managed endpoint.

> [!IMPORTANT]
> We do not guarantee the quality of responses produced by these samples or their suitability for use in your scenarios, and responses will vary as development of the samples is ongoing. You must perform your own validation the outputs of the application and its suitability for use within your company.


## Step 1: Az login
If you haven't already done so, run `az login` to authenticate to Azure in your terminal.
    - Note: if you are running from within a Codespace or the curated VS Code cloud container, you will need to use `az login --use-device-code`
    
## (Optional) use Service Principal in GH codespaces
Steps for creating Service Principal: 
- [CLI Instructions](https://learn.microsoft.com/en-us/cli/azure/azure-cli-sp-tutorial-1?tabs=bash)
- [Portal Instructions](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal)*
*  Use create new secret option and record secret for later step.
  
Ensure the SP has sufficient permissions to deploy the GraphRAG solution. 
- [Required Permissions](https://github.com/Azure-Samples/graphrag-accelerator/blob/main/docs/DEPLOYMENT-GUIDE.md#rbac-permissions)


Use the following az login command using SP:
```bash
az login --service-principal -u <app-id> -p <password-or-cert> --tenant <tenant>
```

Note: Step 2 & 3 provisions necessary azure AI resources including Hub, Project, AOAI, AI Search and creates the index. If you have all of these resources created already, you can skip steps 2 & 3 by copying the sample.env file and renaming it as .env file. Update .env file with your resource names. Place .env file under src/ folder. 

## Step 2: Reference Azure AI resources
Based on the instructions [here](https://microsoft-my.sharepoint.com/:w:/p/mesameki/Ed5UKepTDSpCpUCwigrxFrsBKMBZrEugqhSrosnz8jtdZQ?e=cudeiv), you already have everything you need. Navigate to your hub and project, click on "Settings" from the left menu, scroll down to "Connected Resource" and click on "View all". We need the information here to fill some of the details of our yaml file below. Open your ./provisioning/provision.yaml file and let's fill it together step by step:

### For the section under "ai":

Under your AI Studio project's "Settings" tab, there is a section called "Project properties". Copy paste all the info you need from there into this part of the yaml file. Note that:
- "hub_name": copy paste what you see under "hub resource name" in the UI 
- "project_name"= The string under field "Name" in the UI

### For the section under "aoai":
Click on "Settings" from the left menu of Azure AI Studio, scroll down to "Connected Resource" and click on "View all". Click on the table row whose type is "Azure OpenAI". Once opened:

- aoai_resource_name: What comes under "Resource" in your table
- kind: "OpenAI" (keep it as is)
- connection_name: Title of the page (written above "Connection Details")
### For the section under "deployments":

Click on the "Deployments" tab from the left menu of Azure AI Studio. If you followed all the steps in the workshop guide doc, you already have two deployments here. One embedding model and one GPT model. Insert information from that table here (the table has column headers name, model name, and version. Exactly what you will use here):

- name: from your Deployments table, copy what is under "name". Example: "gpt-4" 

  model: from your Deployments table, copy what is under "model name". Example: "gpt-4"

  version: from your Deployments table, copy what is under "Model version". Example: 1106.
  
  Repeat this for your embedding model:

- name: from your Deployments table, copy what is under "name"/ Example: "text-embedding-ada-002"
  
  model: from your Deployments table, copy what is under "model name". Example: "gpt-4""text-embedding-ada-002"

  version: from your Deployments table, copy what is under "Model version". Example: "2" # if you don't know, comment this line and we'll pick default
### For the section under "search":
Click on "Settings" from the left menu of Azure AI Studio, scroll down to "Connected Resource" and click on "View all". Click on the table row whose type is "Azure AI Search (Cognitive Search)". Once opened:

- search_resource_name: What comes under "Resource" in your table
- connection_name: Title of the page (written above "Connection Details")


Once you set up those parameters, run:

    ```bash
    # Note: make sure you run this command from the src/ directory so that your .env is written to the correct location (src/)
    cd src
    python provisioning/provision.py --export-env .env

    ```

The script will check whether the resources you specified exist, otherwise it will create them. It will then construct a .env for you that references the provisioned or referenced resources, including your keys. Once the provisioning is complete, you'll be ready to move to step 3.

### Step 3: Set the index reference

Use your own index and **Once you have the index you want to use, add the below entry to your .env file.** Note that the copilot code relies on this environment variable.

``` text
AZUREAI_SEARCH_INDEX_NAME=<index-name>
```

## Step 4: Run the copilot

Navigate to the src/flows/rag_copilot_flow directory and open the "flow.dag.yaml" file.  Open the "Visual Editor" in the top left corner of the YAML file.

### Step 4a: Create the flow connections

Open the Promptflow VSCode extension and navigate to the "Extensions" tab.
- Click the Create button ("+") next the "Azure OpenAI" connection option.
  - Fill in the following fields:
    - name: "Default_AzureOpenAI"
    - api_base: "to_replace_with_azure_openai_api_endpoint" <-- Replace with your Azure OpenAI endpoint ex: "https://foo.openai.azure.com/"
  - Click "create connection" near bottom of the file.
    - In the terminal, paste the "api_key" from the Azure OpenAI connection details to securely store the key in your environment.

- #### Alternative Method:
  - Fill in connection information for [/src/flows/aoai_connection.yaml](/src/flows/aoai_connection.yaml)
  - Run command in terminal:

  ``` 
  pf connection create -f aoai_connection.yaml
  ```

- Click the Create button ("+") next the "Azure Search" connection option.
  - Fill in the following fields:
    - name: "Default_AzureSearch"
    - api_base: "to_replace_with_azure_search_api_endpoint" <-- Replace with your Azure Search endpoint ex: "https://bar.search.windows.net"
    - Click "create connection" near bottom of the file.
    - In the terminal, paste the "api_key" from the Azure OpenAI connection details to securely store the key in your environment.

- #### Alternative Method:
  - Fill in connection information for [/src/flows/ai_search_connection.yaml](/src/flows/ai_search_connection.yaml)
  - Run command in terminal:
  ``` 
  pf connection create -f ai_search_connection.yaml
  ```

### Step 4b: Setup the flow connections

- Open the Visual Editor in the top left corner of the YAML file.
- Select the "DetermineIntent" step and click the "Edit" button.
  - Select the "Default_AzureOpenAI" connection you created in the previous step.
  - Select the "chat" api
  - Enter the desired model in the "Deployment" field.
- Select the "RetrieveDocuments" step and click the "Edit" button.
  - Select the "AzureSearch" connection you created in the previous step.
  - Enter the "index_name" of your search index.
  - Select the "Default_AzureOpenAI" connection you created in the previous step.
  - Enter the "embedding_model" of Azure OpenAI deployment.
  # Note - if you are using your own index, remember to update the fields vectorFields, content_field_name, citation_field_name with equivalent field values from your index. 
- Select the "DetermineReply" step and click the "Edit" button.
  - Select the "Default_AzureOpenAI" connection you created in the previous step.
  - Select the "chat" api
  - Enter the desired model in the "Deployment" field.

### Step 4c: Run the copilot
- Enter a question related to your search index in the "query" field.
- Click the "Run" button in the top right corner of the Visual Editor.

## Optional (Generate a RAG evaluation dataset for your copilot)

To evaluate the performance of your copilot, you can generate a dataset of questions and answers. This dataset can be used to evaluate the quality of the responses generated by your copilot.

### Step 4d: Configure the test data generator
- Open `test_data_generator/flow.dag.yaml` in the Visual Editor.
- Configure the inputs to the `generate_qna` step:
  - Connections: The same settings as in Step 4. 
  - `topic`: The topic for which you want to generate questions.
  - `num_questions`: The number of questions you want to generate.
  - `num_questions_per_doc`: The number of questions you want to generate per document.
  - `citation_field_name`: The name of the citation field (used by the generator to provide reference to source context) in the search index, created in Step 3.
  - `content_field_name` : The name of the content field
  - `outputfile`: Name of output jsonl file to be saved.  File saved in the '/output' directory. 

### Step 4e: Run the test data generator
- Click the "Run" button in the top right corner of the Visual Editor.
  
### Step 4f: Inspect the test data generator output
- Inspect the outputfile in the `/output` directory to view the generated questions and answers.
- Check the Question and Answer pairs for relevance and accuracy.

## Step 5: Evaluate the copilot

To start use a set of ground truth questions and answers to evaluate the performance of your copilot.  This dataset should span the breadth of topics that your copilot is expected to handle.

### Step 5a: Execute batch run of test data
- Open `rag_copilot_flow/flow.dag.yaml` in the Visual Editor.
- Create a batch run experiment to run the copilot on a set of questions.
- Configure the inputs to the `batch_run` step:
  - `data`: Name of the input jsonl file to be used.  File should be saved in the '/input' directory.
  - [fill in fields]
  
### Step 5b: Run the batch run experiment
- Save the batch execution yaml file.
- Run the batch execution file.

### Step 6: Perform evaluation of the copilot against ground truth data
- Open the `model_as_a_judge/flow.dag.yaml` in the Visual Editor.
- Create a batch run experiment to evaluate the copilot responses against the ground truth data.
- Select 'Existing Run' to perform the evaluation against the generated answers in step 5
  - Uncomment the `# data` to provide the qna data set and provide ground_truth inputs to the evaluation promptflow.
- Configure the inputs to the batch run job:
  - `data`: Name of the test_data jsonl file used. 
  - [fill in fields]

### Step 6b: Run the evaluation
- Save the batch execution yaml file.
- Run the batch execution file.
- Inspect the output to evaluate the performance of your copilot.
- Check the evaluation metrics to determine the quality of the responses generated by your copilot.
  - Output Example Metrics:
    - ```json
        gpt_coherence: 3.8
        gpt_similarity: 3.65
        gpt_fluency: 3.55
        gpt_relevance: 4
        gpt_groundedness: 3.3
        f1_score: 0.47
        ada_similarity: 0.92

### Step 6c: Inspect evaluation results
- Inspect the output to evaluate the performance of your copilot.
- Check high-scoring responses and low-scoring responses to understand the strengths and weaknesses of your copilot.

Example:
- High-scoring responses: Responses that have high coherence, similarity, fluency, relevance, and groundedness.

- Low-scoring responses: Responses that have low coherence, similarity, fluency, relevance, and groundedness.

### Step 6d: Iterate on your copilot
- Use the evaluation results to identify areas for improvement in your copilot.
- Modify prompts, add documents, or adjust parameters to improve the performance of your copilot.

## Step 7: Deploy the copilot to a managed endpoint
- Open the `rag_copilot_flow/flow.dag.yaml` in the Visual Editor.
- Build the promptflow to docker using promptflow build option.
- Built promptflow can be deployed to an Azure Container Instance (ACI) or Azure Kubernetes Service (AKS) and served via Azure App Service.
