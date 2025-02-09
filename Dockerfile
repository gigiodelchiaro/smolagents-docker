FROM alpine:latest

# Install base packages
RUN apk add --no-cache python3 py3-pip

# Virtual Environment Setup
RUN python3 -m venv .venv
ENV PATH=".venv/bin:$PATH"

# Install Python packages
RUN pip install smolagents openai

# Copy and setup application files
COPY client.py .
RUN chmod +x client.py
VOLUME ["/files"]
ENTRYPOINT ["./client.py"]