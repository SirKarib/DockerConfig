
```sh
docker build -t python-env .
```

```sh
docker-compose build
```

```sh
docker-compose up -d
```

Display Web-server logs

```sh
docker-compose start log-collector && docker logs --tails 20 log-collector
```
