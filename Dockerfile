# Use an official python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the curent directory contents into the container at /app
COPY . /app

# Install the needed packags specified in the requirement.txt file
RUN pip install -r requirements.txt

# Make port 8080 available globally
EXPOSE 8080

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]