start:
	docker compose up -d
	sleep 3
	python project/manage.py runserver
stop:
	docker compose down
static:
	python project/manage.py collectstatic
format:
	black --config black.toml .
