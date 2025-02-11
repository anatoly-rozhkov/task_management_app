start:
	docker compose up -d
	sleep 3
	python project/manage.py runserver
static:
	python project/manage.py collectstatic
format:
	black --config black.toml .