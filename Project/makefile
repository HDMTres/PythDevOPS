include .env
export
.PHONY: init build run stop clean test help

# Show help
help:
	@echo "Available commands:"
	@echo "  make build    - Build the Docker image"
	@echo "  make run      - Run the Flask app in a Docker container"
	@echo "  make stop     - Stop the running container"
	@echo "  make clean    - Remove stopped containers"
	@echo "  make test     - Run the unit tests"

# Initialization:
init:
	@echo "Initializing the project..."
	python3 -m venv .venv
	@echo "Activating the virtual environment and installing libraries..."
	. .venv/bin/activate && pip install -r requirements.txt
	@mkdir -p logs
	@touch logs/error.log logs/info.log
	@echo "Project initialized"
	@echo "------------------------"

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Flask app
run:
	docker run -d -p $(PORT):5000 $(IMAGE_NAME)

# Stop the running container
stop:
	docker stop $$(docker ps -q --filter ancestor=$(IMAGE_NAME))

# Clean up stopped containers
clean:
	docker rm $$(docker ps -a -q)

# Run the tests
test:
	python -m unittest discover
