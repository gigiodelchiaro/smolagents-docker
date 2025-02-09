FROM alpine:latest

# Install base packages
RUN apk add --no-cache python3 py3-pip

# Virtual Environment Setup
RUN python3 -m venv /home/aiuser/.venv
ENV PATH="/home/aiuser/.venv/bin:$PATH"

# Install Python packages
RUN pip install smolagents openai

# Create user and group
RUN addgroup -g 1000 ai && adduser -u 1000 -G ai -s /bin/sh -D aiuser

WORKDIR /home/aiuser

# Setup sandbox directory
RUN mkdir /home/aiuser/sandbox && \
    chown aiuser:ai /home/aiuser/sandbox && \
    chmod 700 /home/aiuser/sandbox

# Copy and setup application files
COPY client.py .
COPY .env .
RUN chmod +x client.py

USER aiuser

ENTRYPOINT ["/home/aiuser/client.py"]