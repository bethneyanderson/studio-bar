# Studio Bar - Development Commands
# Virtual environment Python path
PYTHON = .venv/bin/python
PIP = .venv/bin/pip
FLAKE8 = .venv/bin/flake8
AUTOPEP8 = .venv/bin/autopep8

.PHONY: help install lint lint-fix test format check-all clean

help:  ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install dependencies
	$(PIP) install -r requirements.txt

lint:  ## Run flake8 linting
	$(FLAKE8) --statistics

lint-fix:  ## Auto-fix linting issues with autopep8
	$(AUTOPEP8) --in-place --recursive --aggressive --aggressive --max-line-length=88 .
	@echo "Fixed formatting issues. Run 'make lint' to check remaining issues."

format:  ## Format code (alias for lint-fix)
	@make lint-fix

test:  ## Run Django tests
	$(PYTHON) manage.py test

check-all:  ## Run all checks (lint, test)
	@echo "Running code quality checks..."
	@make lint
	@echo "\nRunning tests..."
	@make test
	@echo "\nAll checks completed!"

clean:  ## Clean Python cache files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

dev-setup:  ## Set up development environment
	@echo "Setting up development environment..."
	@make install
	@echo "Running initial code formatting..."
	@make lint-fix
	@echo "Development environment ready!"
