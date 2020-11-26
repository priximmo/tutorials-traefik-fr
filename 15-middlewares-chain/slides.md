%title: TRAEFIK
%author: xavki


# TRAEFIK : Middlewares - Chain



<br>


Documentation : https://docs.traefik.io/middlewares/chain/

* chain = enchainement et ordre des middlewares

```
sudo apt install apache2-utils
htpasswd -nB xavki
```

<br>


* middleware d'authentification

```
[http.middlewares]
    [http.middlewares.login.basicAuth]
    users = [
    "xavki:$2y$05$L6tUGpt4aes2CVkWwoAOROx5ZIwUWO9bmdUPOAR5GqMszx4RcKAPy",
    "xavki2:$2y$05$L6tUGpt4aes2CVkWwoAOROx5ZIwUWO9bmdUPOAR5GqMszx4RcKAPy",
    ]
```

<br>


* middleware de compress

```
  [http.middlewares.gzip.compress]
```

<br>


* middleware de whitelisting

```
  [http.middlewares.filter_by_ip.ipWhiteList]
    sourceRange = ["192.168.13.1"]
```

<br>


* création de la chaine

```
  [http.middlewares.secured.chain]
    middlewares = ["filter_by_ip", "login", "compress"]
```
