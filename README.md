# README


Build -
`docker build -t backend-test:latest .`

Run with docker swarm -
- `docker swarm init`
- `docker stack deploy -c docker-compose.yml backend-stack`
- `docker service ls`