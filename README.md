# Ollama Docker with FastAPI (Docker Compose)

This repository provides a setup for running a **FastAPI** application using **Docker Compose**. It simplifies managing multiple services and configurations, making it easy to deploy and run locally.

---

## Features

- **Docker Compose Setup**: Orchestrates the application and its dependencies.
- **FastAPI Framework**: High-performance API development made simple.
- **Easy Deployment**: Launch the entire stack with a single command.
- **Extensible Design**: Add more services or scale as needed.

---

## Prerequisites

Before getting started, ensure you have the following installed:

- [Docker](https://www.docker.com/) (latest version recommended)
- [Docker Compose](https://docs.docker.com/compose/) (comes bundled with Docker Desktop)

---

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/surya-1729/Ollama-docker-FastAPI.git
cd Ollama-docker-FastAPI
```

### Run the Application

Start the application stack using Docker Compose:

```bash
docker-compose up --build
```

This command will:
1. Build the necessary Docker images.
2. Start all services defined in the `docker-compose.yml` file.

The FastAPI application will be accessible at `http://localhost:8000`.

---

## API Endpoints

Once the application is running, explore the API using:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`

These interfaces provide an interactive way to test and understand the API.

---

## Stopping the Application

To stop the running containers, use:

```bash
docker-compose down
```

This will stop and remove all containers defined in the `docker-compose.yml` file.

---

## Development Workflow

For local development:

1. Edit the FastAPI source code in the repository.
2. Restart the stack to apply changes:
   ```bash
   docker-compose up --build
   ```
3. Test your updates via Swagger UI or other tools.

---

## Directory Structure

```plaintext
Ollama-docker-FastAPI/
├── app/                   # FastAPI application code
│   ├── main.py            # Main entry point for the FastAPI app
│   ├── ...                # Additional app files (routes, models, etc.)
├── docker-compose.yml     # Docker Compose configuration file
├── Dockerfile             # Dockerfile for building FastAPI service image
├── requirements.txt       # Python dependencies for FastAPI
└── README.md              # Project documentation (this file)
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`feature/my-feature`).
3. Commit your changes.
4. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to the creators of **FastAPI**, **Docker**, and **Docker Compose** for their incredible tools that make this project possible!

---
Answer from Perplexity: pplx.ai/share
