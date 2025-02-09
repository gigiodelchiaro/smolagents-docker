#!/usr/bin/env python3
import os
from smolagents import OpenAIServerModel, DuckDuckGoSearchTool, HfApiModel, CodeAgent, OpenAIServerModel, tool

model = OpenAIServerModel(
    model_id=os.environ["MODEL_ID"],
    api_base=os.environ["API_URL"],
    api_key=os.environ["API_KEY"],
)

@tool
def write_to_file(file_name:str, content: str) -> str:
    """
    This is a tool that writes to a file.

    Args:
        file_name: The name of the file to write to.
        content: The content to write to the file.
    """
    os.chdir("/files")
    with open(f"{file_name}", "w") as f:
        f.write(content)

    return f"File '{file_name}' written successfully."

agent = CodeAgent(tools=[DuckDuckGoSearchTool(), write_to_file], model=model)

agent.run(os.environ["PROMPT"])