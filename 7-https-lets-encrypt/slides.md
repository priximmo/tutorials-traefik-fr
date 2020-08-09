%title: TRAEFIK
%author: xavki


# TRAEFIK : HTTPS && Let's Encrypt


<br>
* redirection https avec cert Let's Encrypt

xavki.fr > dns > ip > box/pat > laptop > traefik > python/server

<br>
* créer un resolver : https://docs.traefik.io/https/acme/

* type de challenge : tls, http, dns

```
[certificatesResolvers]
  [certificatesResolvers.xavki_certs]
    [certificatesResolvers.xavki_certs.acme]
      email = "moi@gmail.com"
      caServer = "https://acme-v02.api.letsencrypt.org/directory"
      storage = "acme.json"
      keyType = "EC384"
        [certificatesResolvers.xavki_certs.acme.httpChallenge]
          entryPoint = "xavki"
```

Rq : http challenge

-----------------------------------------------------------------------------

# TRAEFIK : HTTPS && Let's Encrypt

<br>
* pour challenge http (pas de redirection du port 80

```
[entryPoints]
  [entryPoints.xavki]
    address=":80"
  [entryPoints.xavki_secure]
    address=":443"
```

<br>
* router > modification de la déclaration du certificat
		* rule
		* entrypoint
		* certResolver

```
    [http.routers.xavki_route]
      entryPoints = ["xavki_secure"]
      service = "xavki"
      rule = "Host(`xavki.fr`) && Path(`/`)"
      middlewares = ["xavki_https"]
      [http.routers.xavki_route.tls]
        certResolver = "xavki_certs"
```
