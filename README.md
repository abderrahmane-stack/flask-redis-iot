# Flask-Redis IoT Project

This project demonstrates an IoT setup where an ESP8266 module sends data to a Flask web application hosted in a Docker container. The data is stored in a Redis database, also running in Docker.

## Project Structure

- `app.py`: Flask application that receives data and stores it in Redis.
- `Dockerfile`: Configuration for building the Flask app Docker image.
- `docker-compose.yaml`: Configuration for setting up both Flask and Redis services.
- `requirements.txt`: Python dependencies required for the Flask app.
- `index.html`: HTML template for viewing stored data (optional).

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- Python 3.x and pip
- ESP8266 module (configured to send HTTP requests to the Flask app)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abderrahmane-stack/flask-redis-iot.git
   cd flask-redis-iot
2. Build and start the Docker containers:
  ```bash
  docker-compose up --build -d
   ```
## Usage
Ensure your ESP8266 is configured to send JSON data (only name field) to the Flask app's endpoint.
Open http://localhost:5000/ in your browser to view the JSON data.
Access http://localhost:5000/action to view data in a web interface.
