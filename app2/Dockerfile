# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt, including Gunicorn
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run the Gunicorn server with 4 worker processes
# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
