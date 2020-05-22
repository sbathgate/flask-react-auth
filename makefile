default: help

help: ## Output available commands
	@echo "Available commands:"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

lint-client:  ## Run Prettier and Lint
	@docker-compose exec client npm run lint
	@docker-compose exec client npm run prettier:check
	@docker-compose exec client npm run prettier:write

lint-users:  ## Run Flake8, Black and iSort
	@docker-compose exec users flake8 project
	@echo "flake8 complete"
	@docker-compose exec users black project
	@docker-compose exec users /bin/sh -c "isort project/**/*.py"
	@echo "lint and format complete"

postgres:  ## Access db via psql
	@echo "# \c users_dev"
	@echo "# select * from users;"
	@docker-compose exec users-db psql -U postgres

rebuild:  ## Rebuild docker images
	@docker-compose up -d --build

reseed:  ## Recreate and Seed db
	@docker-compose exec users python manage.py recreate_db
	@docker-compose exec users python manage.py seed_db

start:  ## Run a development environment
	@docker-compose up -d

test-all: ## Run the current test suite
	@docker-compose exec users python -m pytest "project/tests" -p no:warnings
	@docker-compose exec client npm test --coverage

test-client:  ## Test frontend
	@docker-compose exec client npm test --coverage

test-users:  ## Test backend
	@docker-compose exec users python -m pytest "project/tests" -p no:warnings