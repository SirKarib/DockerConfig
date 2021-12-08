Build Docker image with Python 3 Environment

```sh
docker build -t python-env .
```

Build Docker images with Docker-Compose

```sh
docker-compose build
```

Run Docker containers with Docker-Compose

```sh
docker-compose up -d
```

Print the last 20 Web server logs

```sh
docker-compose start log-collector && docker logs --tails 20 log-collector
```
