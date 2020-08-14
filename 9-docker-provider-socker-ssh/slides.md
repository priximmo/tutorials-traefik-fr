%title: TRAEFIK
%author: xavki


# TRAEFIK : Docker Provider - socket distante


<br>
* avec la socket unix local :

```
[providers.docker]
  endpoint = "unix:///var/run/docker.sock"
```

<br>
* via la socket ssh

* création clef ssh et copie de la clef publique

```
[providers.docker]
  endpoint = "ssh://vagrant@192.168.13.11:22"
```

Rq :

```
  useBindPortIP = true
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
    - 192.168.13.11:80:80
    labels:
      - traefik.http.routers.my-container.rule=Host(`example.com`) || Path(`/example/`)
```

sticky session
