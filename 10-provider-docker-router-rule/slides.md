%title: TRAEFIK
%author: xavki


# TRAEFIK : Docker Provider - Routers Rules


<br>
* documentation : https://docs.traefik.io/routing/routers/

<br>
Types de rule :

<br>
* clef du header

```
Headers(`key`, `value`)
```

<br>
* regex dans une clef du header

```
HeadersRegexp(`key`, `regexp`)
```

<br>
* le host header

```
Host(`example.com`, ...)
HostHeader(`example.com`, ...)
```

---------------------------------------------------------------------------------------

# TRAEFIK : Docker Provider - Routers Rules



<br>
* regex sur le host header

```
HostRegexp(`example.com`, `{subdomain:[a-z]+}.example.com`, ...)
```

<br>
* sélection par les méthodes

```
Method(`GET`, ...)
````

<br>
* sélection via le path (exact)

```
Path(`/path`, `/articles/{cat:[a-z]+}/{id:[0-9]+}`, ...)
```

<br>
* sélection via le pathprefix (partie du path)

```
PathPrefix(`/products/`, `/articles/{cat:[a-z]+}/{id:[0-9]+}`)
```

<br>
* requête via les paramètres

```
Query(`foo=bar`, `bar=baz`)
```

---------------------------------------------------------------------------------------

# TRAEFIK : Docker Provider - Routers Rules


* utilisation via docker-compose (partie dynamique) :

```
version: '3.3'
services:
  my-container:
    image: nginx:latest
    container_name: mynginx
    ports:
    - 192.168.13.11:8082:80
    labels:
      - traefik.http.routers.my-container.rule=HostRegexp(`example.com`,`www.example.com`,`{subdomain:[ikvxa]+}.example.com`) || Path(`/example/{.*}`,`/example/`) 
      - traefik.http.routers.my-container.middlewares=rewrite
      - "traefik.http.middlewares.rewrite.replacepathregex.regex=^/example/(.*)"
      - "traefik.http.middlewares.rewrite.replacepathregex.replacement=/tata/$$1"
```

