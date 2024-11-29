# Use Python 3.10-slim as the parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app
#WORKDIR /book_service

# Copy the current directory contents into the container at /app
COPY . /app
#COPY book-service/ /book_service
#COPY . /book_service

# Install required Python packages
RUN pip install flask flask_cors

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable for SQLite database location
#ENV DATABASE = /Users/tejaswath/Desktop/Build_something/bookstore-app/shared/bookstore.db
ENV DATABASE=/app/shared/bookstore.db

# Run book_service.py when the container launches
CMD ["python", "book_service.py"]