from promptflow.core import tool
from promptflow.connections import CustomConnection
import requests, json


# a helper function to parse out the result from a query response
def parse_query_response(
    response: requests.Response, return_context_data: bool = False
) -> requests.Response | dict[list[dict]]:
    """
    Prints response['result'] value and optionally
    returns associated context data.
    """
    if response.ok:
        print(json.loads(response.text)["result"])
        if return_context_data:
            return json.loads(response.text)["context_data"]
        return response
    else:
        print(response.reason)
        print(response.content)
        return response
    
# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def my_python_tool(graph_conn: CustomConnection, index_name:str, query: str ) -> str:
    headers = {"Ocp-Apim-Subscription-Key": graph_conn.secrets["api_key"]}
    """Run a global query over the knowledge graph(s) associated with one or more indexes"""
    url = graph_conn.configs["endpoint"] + "/query/global"
    request = {"index_name": index_name, "query": query}
    return requests.post(url, json=request, headers=headers).json()["result"]
