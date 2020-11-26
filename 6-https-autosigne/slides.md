%title: TRAEFIK
%author: xavki


# TRAEFIK : HTTPS autosigné


<br>


* redirection simple

```
  [entryPoints.xavki]
    address=":80"
    [entryPoints.xavki.http.redirections]
      [entryPoints.xavki.http.redirections.entryPoint]
        to = "xavki_secure"
        scheme = "http"
  [entryPoints.xavki_secure]
    address=":443"
```

<br>


* redirection https

```
  [entryPoints.xavki]
    address=":80"
    [entryPoints.xavki.http.redirections]
      [entryPoints.xavki.http.redirections.entryPoint]
        to = "xavki_secure"
        scheme = "https"
  [entryPoints.xavki_secure]
    address=":443"
```

-------------------------------------------------------------------------------

# TRAEFIK : HTTPS autosigné

<br>


* mise en place du certificat autosigné

```
openssl req -x509 -newkey rsa:2048 -keyout xavki.key -out xavki.crt -days 365 -nodes
```

<br>


* configuration du certificat

```
    [http.routers.xavki_route]
      entryPoints = ["xavki","xavki_secure"]
      service = "xavki"
      rule = "Path(`/`)"
      middlewares = ["xavki_https"]
      [http.routers.xavki_route.tls]
        [[tls.certificates]]
        certFile = "certs/xavki.cert"
        keyFile = "certs/xavki.key"
  [http.middlewares]
    [http.middlewares.xavki_https.redirectScheme]
      scheme = "https"
      permanent = true
```
