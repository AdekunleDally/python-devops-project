# Overview

This repository contains a Python script that prints the current timestamp to the console. We will deploy this script as a web service in a Kubernetes cluster, allowing it to be invoked via an HTTP GET request and return the timestamp. KIND(Kubernetes in Docker) was used to achieve this

# Implementation Details
* Install Python flask
* Install Flask-RESTful 
* Dockerise the application; create an image of your application and push to dockerhub
* Create an instance of your image(I.e. create a container)
* Install KIND on your terminal
*Create a KIND cluster and load the docker image into KIND
* Create Kubernetes deployment and kubernetes service
* Forward the port to access the service from your machine

1. Containerization: We will use Docker to containerize the Python script. The Dockerfile will use a lightweight Python image and copy the script into the container. We would set the container host to a port 5000 and the container to port 5000

2. Kubernetes Deployment: We will create a Kubernetes deployment YAML file  and a service YAML file to deploy the containerized script. The deployment will include:
    - A pod with a single container running the script
    - A service exposing the pod on port 80
    - Autoscaling configuration to scale based on CPU usage

3. Helm Chart: We will package the Kubernetes deployment as a Helm chart for easy installation and management.

4. Monitoring: We will implement basic monitoring using Prometheus and Grafana. The script will expose metrics on port 8000, and Prometheus will scrape these metrics. Grafana will display the metrics in a dashboard.

Design Choices

- Lightweight Container: We chose a lightweight Python image to keep the container size small.
- Autoscaling: We implemented autoscaling based on CPU usage to ensure the service can handle increased traffic.
- Monitoring: We chose Prometheus and Grafana for monitoring, as they are widely used and provide a flexible monitoring solution.

Repository Structure

- app.py: The Python script
- Dockerfile: The Dockerfile for containerization
- deployment.yaml: The Kubernetes deployment YAML file
- service-definition.yaml : The service definition YAML file that defines how kubernetes objects(such as pods) communicate with each other
- helm_chart: The Helm chart directory
- prometheus_config.yaml: The Prometheus configuration file
- grafana_dashboard.json: The Grafana dashboard configuration file

Deployment Steps

1. Build the Docker image: docker build -t print-timestamp .
2. Push the image to a container registry: docker push <registry>/print-timestamp
3. Install the Helm chart: helm install print-timestamp helm_chart
4. Apply the Kubernetes deployment: kubectl apply -f deployment.yaml
5. Configure Prometheus and Grafana: kubectl apply -f prometheus_config.yaml and kubectl apply -f grafana_dashboard.json

Invoking the Service

To invoke the service, send an HTTP GET request to http://<service-ip>:80. The service will return the current timestamp.