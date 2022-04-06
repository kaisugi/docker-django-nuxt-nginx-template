# docker-django-nuxt-nginx-template

based on https://github.com/naritotakizawa/docker-drf-and-nuxt-template

## development

```
docker-compose -f docker-compose.yml -f dev.yml build
docker-compose -f docker-compose.yml -f dev.yml up
```

open `http://127.0.0.1`

## production

change `ALLOWED_HOSTS` in `prod.yml` to your IP or host name

```
docker-compose -f docker-compose.yml -f prod.yml build
docker-compose -f docker-compose.yml -f prod.yml up
```

open `http://[your IP or host name]`