# Build the Docker Image
- Open a terminal and navigate to the directory where your classification.py, Dockerfile, and requirements.txt are located.
- Build the Docker image using the following command:
```commandline
docker build -t streamlit-classification-app .
```
# Run the Docker Container
```commandline
docker run -p 8501:8501 streamlit-classification-app
```
