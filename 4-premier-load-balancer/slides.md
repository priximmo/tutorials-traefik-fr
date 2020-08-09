%title: TRAEFIK
%author: xavki


# TRAEFIK : Premier Load Balancer


<br>
* exemple 2 service minimalistes :

```
python3 -m http.server 8081
python3 -m http.server 8082
```

<br>
* configuration réduite :

```
[accesslog]
[api]
  insecure=true
  dashboard=true
  debug=true

[log]
  level="INFO"

[entryPoints]
  [entryPoints.web]
    address=":80"

[providers.file]
  directory = "/home/vagrant/services/"
  watch = true
```

<br>
* traitement du service

```
[http]
  [http.routers]
    [http.routers.xavki_route]
      entryPoints = ["web"]
      service = "xavki"
      rule = "Path(`/`)"
  [http.services]
    [http.services.xavki]
      [http.services.xavki.loadBalancer]
        [[http.services.xavki.loadBalancer.servers]]
          url = "http://127.0.0.1:8081"
        [[http.services.xavki.loadBalancer.servers]]
          url = "http://127.0.0.1:8082"
```
