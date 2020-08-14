%title: TRAEFIK
%author: xavki


# TRAEFIK : WhiteListing & Compression



<br>
Documentation : https://docs.traefik.io/middlewares/ipwhitelist/

* white list

```
[http.middlewares]
  [http.middlewares.filter_by_ip.ipWhiteList]
    sourceRange = ["192.168.13.10/24"]
```

<br>
Documentation : https://docs.traefik.io/middlewares/compress/

* compression

```
      middlewares = ["gzip"]
[http.middlewares]
  [http.middlewares.gzip.compress]

```
