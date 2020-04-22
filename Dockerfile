# Use an official Python runtime as a parent image
FROM tiangolo/uvicorn-gunicorn-fastapi:latest


RUN pip install aiofiles jinja2 pymongo
# Copy the remaining directory contents into the container at /app
COPY ./app /app



