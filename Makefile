TAIL = 100

build:
	docker compose -f docker-compose.yaml build
up:
	docker compose -f docker-compose.yaml up -d
down:
	docker compose -f docker-compose.yaml down
logs:
	docker logs -f --tail=${TAIL} telegram_bot_ege 2>&1
pre-commit:
	pip install pre-commit && pre-commit run --all-files
