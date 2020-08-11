%title: TRAEFIK
%author: xavki


# TRAEFIK : Docker Provider


<br>
* multi providers

<br>
* avec la socket unix local :

```
[providers.docker]
  endpoint = "unix:///var/run/docker.sock"
```

<br>
* utilisation via docker-compose (partie dynamique) :

```
version: '3.3'
services:
  my-container:
    image: nginx:latest
    container_name: mynginx
    ports:
    - 8082:80
    labels:
      - traefik.http.routers.my-container.rule=Host(`example.com`)
```

<br>
* via la socket ssh

* création clef ssh et copie de la clef publique

```
[providers.docker]
  endpoint = "ssh://vagrant@127.0.0.1:22"
```
