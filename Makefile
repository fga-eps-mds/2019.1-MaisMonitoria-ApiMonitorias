build:
	docker-compose -f docker-compose.yml build

run:
	docker-compose -f docker-compose.yml up -d db
	sleep 60
	docker-compose -f docker-compose.yml up api_monitoria

run-d:
	docker-compose -f docker-compose.yml up -d db
	sleep 60
	docker-compose -f docker-compose.yml up -d api_monitoria

down:
	docker-compose -f docker-compose.yml down

run-tests:
	docker-compose exec api_monitoria coverage run manage.py test

cov-tests:
	docker-compose exec api_monitoria coverage report -m
	