#!/usr/bin/env python3
import os
from smolagents import OpenAIServerModel, DuckDuckGoSearchTool, HfApiModel, CodeAgent, OpenAIServerModel

model = OpenAIServerModel(
    model_id=os.environ["MODEL_ID"],
    api_base=os.environ["API_URL"],
    api_key=os.environ["API_KEY"],
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run(os.environ["PROMPT"])