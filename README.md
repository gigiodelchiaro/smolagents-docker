# Smolagents Docker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Docker Pulls](https://img.shields.io/docker/pulls/gigiodc/smolagents-docker)](https://hub.docker.com/r/gigiodc/smolagents-docker)
[![Docker Image Size](https://img.shields.io/docker/image-size/gigiodc/smolagents-docker)](https://hub.docker.com/r/gigiodc/smolagents-docker)
[![Docker Stars](https://img.shields.io/docker/stars/gigiodc/smolagents-docker)](https://hub.docker.com/r/gigiodc/smolagents-docker)


<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/mascot.png" width="150">

## Overview
A Docker container for running smolagents with OpenAI-compatible models.

## Quick Start

### Running the Container 🚀
```bash
docker run -e PROMPT="Your prompt" -e MODEL_ID="model" -e API_URL="url" -e API_KEY="api_key" gigiodc/smolagents-docker
```


### Building the Container 🛠️
```bash
git clone https://github.com/gigiodelchiaro/smolagents-docker.git
cd smolagents-docker
docker build -t smolagents-docker .
docker run -e PROMPT="Your prompt" -e MODEL_ID="model" -e API_URL="url" -e API_KEY="api_key" smolagents-docker
```
## Configuration  (optional) ⚙️

Create a `.env` file in the root directory with the following variables:

```bash
MODEL_ID="model"          # Example: "gemini-2.0-flash"
API_URL="url"            # Example: "https://generativelanguage.googleapis.com/v1beta/openai/"
API_KEY="API_key"        # Example: "sk-..."
```



> [!NOTE]\
> The service requires an OpenAI-compatible model endpoint.