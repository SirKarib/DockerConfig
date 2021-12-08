Build Docker image with Python 3 Environment

```sh
docker build -t python-env .
```

Build Docker images

```sh
docker-compose build
```

Run Docker containers

```sh
docker-compose up -d
```

Print Web-server logs

```sh
docker-compose start log-collector && docker logs --tails 20 log-collector
```
