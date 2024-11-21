import os
import json
import logging
import math
import random
from datetime import datetime
from pathlib import Path

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.ai.generative.synthetic.qa import QADataGenerator, QAType

from promptflow.core import tool, AzureOpenAIModelConfiguration
from promptflow.connections import AzureOpenAIConnection, CognitiveSearchConnection

import logging
import sys

# Configure logger to print to standard output
logger = logging.getLogger("scripts")
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

def generate_test_qa_data(
    openai_config: dict,
    search_client: SearchClient,
    num_questions_total: int,
    num_questions_per_source: int,
    output_file: Path,
    citation_field_name: str,
    content_field_name: str = "content",
):
    logger.info(
        "Generating %d questions total, %d per source, based on search results",
        num_questions_total,
        num_questions_per_source,
    )

    qa_generator = QADataGenerator(model_config=openai_config)

    r = search_client.search("", top=1000)
    qa: list[dict] = []
    for doc in r:
        if len(qa) > num_questions_total:
            break
        logger.info("Processing search document %s", doc[citation_field_name])
        text = doc[content_field_name]

        result = qa_generator.generate(
            text=text,
            qa_type=QAType.LONG_ANSWER,
            num_questions=num_questions_per_source,
        )

        for question, answer in result["question_answers"]:
            citation = f"[{doc[citation_field_name]}]"
            qa.append({"question": question, "truth": answer + citation})

    logger.info("Writing %d questions to %s", len(qa), output_file)
    directory = Path(output_file).parent
    if not directory.exists():
        directory.mkdir(parents=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for item in qa:
            f.write(json.dumps(item) + "\n")


@tool
def my_python_tool(aoai_conn: AzureOpenAIConnection,
    aoai_deployment: str,
    aoai_model: str,
    aisearch_conn: CognitiveSearchConnection,
    aisearch_index: str,
    numquestionstotal: int,
    numquestionspersource: int,
    outputfile: str,
    citationfieldname: str,
    content_field_name: str,
    topic: str) -> str:
    
        openai_config={
            "api_type": "azure",
            "api_base": aoai_conn.api_base,
            "api_key": aoai_conn.api_key,
            "api_version": "2024-02-15-preview",
            "deployment": aoai_deployment,
            "model": aoai_model,
        }
               
        search_client = SearchClient(
            endpoint=aisearch_conn.api_base,
            index_name=aisearch_index,
            credential=AzureKeyCredential(aisearch_conn.api_key),
        )
        
        # Create the output folder if it doesn't exist
        output_path = Path.cwd() / "output"
        output_path.mkdir(parents=True, exist_ok=True)
    
        generate_test_qa_data(
            openai_config = openai_config,
            search_client=search_client,
            num_questions_total=numquestionstotal,
            num_questions_per_source=numquestionspersource,
            output_file=output_path / outputfile,
            citation_field_name=citationfieldname,
            content_field_name=content_field_name,
        )
        
        return f"{output_path / outputfile}"
    
    
    
