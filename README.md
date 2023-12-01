#Streamlit Docker App
This project provides a simple setup for deploying a Streamlit app using Docker containers.

Prerequisites
Make sure you have  Docker installed on your machine

Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/nat997/MicroServ
cd streamlit-docker-app
Build the Docker Images:

docker-compose up --build

This command will build the Docker images for your Streamlit app, backend, and database.

Access the Streamlit App:

Open your browser and navigate to http://localhost:8501 to view your Streamlit app or http://localhost.

Stopping the Containers:

To stop the Docker containers, run:

docker-compose down

Customization

Streamlit App: Place your Streamlit app files in the frontend directory.
Backend: Customize your backend in the backend directory.
Database: Adjust database configurations in the docker-compose.yml file.
Notes
The app is configured to run on http://localhost:8501.
Nginx is used as a reverse proxy and is configured in the nginx.conf file.

