%title: TRAEFIK
%author: xavki


# TRAEFIK : authentification BasicAuth


<br>


Doc : https://docs.traefik.io/middlewares/basicauth/

* générer un hash MD5, SHA1, or BCrypt

```
sudo apt install apache2-utils
```

```
htpasswd -nB xavki
```

Rq : -B > bcrypt

<br>


* configuration

```
[http]
  [http.routers]
    [http.routers.xavki_route]
      entryPoints = ["xavki"]
      service = "xavki"
      rule = "Path(`/`)"
      middlewares = ["xavki"]
  [http.middlewares]
    [http.middlewares.xavki.basicAuth]
    users = [
    "xavki:$2y$05$L6tUGpt4aes2CVkWwoAOROx5ZIwUWO9bmdUPOAR5GqMszx4RcKAPy",
    "xavki2:$2y$05$L6tUGpt4aes2CVkWwoAOROx5ZIwUWO9bmdUPOAR5GqMszx4RcKAPy",
    ]
```

-------------------------------------------------------

# TRAEFIK : authentification BasicAuth

<br>



<br>


* secure api

```
[accesslog]
[api]
  #insecure=true
  dashboard=true
  debug=true
[log]
  level="INFO"
[entryPoints]
  [entryPoints.xavki]
    address=":80"
  [entryPoints.api]
    address=":8080"
```

<br>


* settings du router

```
    [http.routers.api_route]
      entryPoints = ["api"]
      service = "api@internal"
      rule = "PathPrefix(`/api`)||PathPrefix(`/dashboard`)"
      middlewares = ["xavki"]
```

Rq : api@internal (service interne)
