# Flask-Terraform Deployment App

This is a simple Flask application that allows you to deploy Terraform configurations using a REST API. The application clones a repository with the specified branch, changes the directory to a specified folder in the cloned repository, and runs Terraform commands on the configuration found there. The app runs with Gunicorn and is served behind an Nginx reverse proxy using Docker Compose.

## Prerequisites

- Docker
- Docker Compose
- Git

## Usage

1. Clone this repository:

`git clone https://github.com/your-repo-url.git`

2. Change to the repository directory:

`cd your-repo-directory`

3. Build the Docker images using the provided Makefile:

`make build`

4. Start the containers:

make run

5. Access the Flask application via the Nginx reverse proxy at `http://localhost:8080`


