# Use an official Python runtime as a parent image
FROM python:3.11.3-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

RUN pip install --upgrade pip

# Copy the .env file
COPY .env .env

# Copy the current directory contents into the container at /app
COPY requirements_docker.txt requirements_docker.txt
COPY setup.py setup.py
COPY yana/api yana/api
COPY yana/data yana/data
COPY yana/ml_logic yana/ml_logic
COPY yana/params.py yana/params.py



# Install any needed packages specified in requirements.txt
RUN pip install -r requirements_docker.txt

# Run app.py when the container launches
CMD uvicorn yana.api.api:app  --host 0.0.0.0 --port $PORT
