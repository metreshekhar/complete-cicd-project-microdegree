# Use a Python 3.7 slim image as the base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project into the container (including templates and static files)
COPY . .

# Expose port 80, since Flask runs on port 80 in the app
EXPOSE 80

# Set the command to run the Flask app
CMD ["python", "app.py"]
