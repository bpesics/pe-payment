deploy:
	docker-compose -f docker-compose.yaml build
	docker-compose -f docker-compose.yaml down -v
	docker-compose -f docker-compose.yaml up -d --force-recreate