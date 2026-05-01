# Use a slim Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies if any (none required for these libs specifically, but good practice)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Create a directory for data
RUN mkdir /data
WORKDIR /data

# Set the entrypoint to the python script
ENTRYPOINT ["python", "/app/main.py"]
