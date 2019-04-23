build:
	docker-compose -f docker-compose.yml build
run:
	docker-compose -f docker-compose.yml up

run-d:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

tests:
	docker-compose exec api_monitoria py.test --cov=.
	