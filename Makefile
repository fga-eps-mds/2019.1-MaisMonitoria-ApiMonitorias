run:
	docker-compose -f docker-compose.yml up

run-d:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

run-dc-tests:
	docker network create api-backend 
	docker-compose -f docker-compose.yml build

tests:
	docker exec api_monitoria bash -c "bash run-tests.sh"

unit-tests:
	echo "Running Unit Tests"
	docker exec api_monitoria bash -c "bash run-tests.sh"
	