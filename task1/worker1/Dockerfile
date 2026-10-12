# Dockerfile for Program 1 (worker1)
# Variant 8: finds the largest file in /var/data
# and copies it to /var/result/data.txt

# Base image: official Python 3.12 (slim for smaller size)
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy application code
COPY app.py /app/app.py

# Run the script when container starts
CMD ["python", "/app/app.py"]
