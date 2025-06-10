up:
	docker compose up
down:
	docker compose down
static:
	python project/manage.py collectstatic
format:
	black --config black.toml .
superuser:
	python project/manage.py create_superuser