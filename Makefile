manage_path=src/manage.py  # manage.py path

.PHONY: runserver
runserver:
	poetry run python $(manage_path) runserver

.PHONY: migrate
migrate:
	poetry run python $(manage_path) migrate

.PHONY: makemigrations
makemigrations:
	poetry run python $(manage_path) makemigrations

.PHONY: superuser
superuser:
	poetry run python $(manage_path) createsuperuser
