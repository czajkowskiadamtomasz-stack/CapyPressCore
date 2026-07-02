up:
	docker compose up --build

down:
	docker compose down

migrate:
	docker compose run web python manage.py migrate

shell:
	docker compose run web python manage.py shell
