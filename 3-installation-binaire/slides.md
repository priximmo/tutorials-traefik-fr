%title: TRAEFIK
%author: xavki


# TRAEFIK : Installation via binaire


<br>


* installation en binaire

Doc : https://docs.traefik.io/providers/overview/


https://github.com/containous/Traefik/releases/

https://docs.traefik.io/getting-started/install-traefik/


```
wget https://github.com/containous/traefik/releases/download/v2.3.0-rc3/traefik_v2.3.0-rc3_linux_amd64.tar.gz
tar xzvf traefik_v2.3.0-rc3_linux_amd64.tar.gz
mv traefik /usr/local/bin
chmod 755 /usr/local/bin/traefik
```

------------------------------------------------------------------------

# TRAEFIK : Installation via binaire

<br>


* configuration (juste dashboard)

<br>


* ex : cli

```
traefik --accesslog=true \
        --api=true \
        --api.insecure=true \
        --api.dashboard=true \
        --api.debug=true \
        --log.level=INFO \
```

<br>


* ex : fichier toml

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
```

```
traefik --configFile=config.toml
```

<br>


* test

```
http://192.168.13.10:8080/
```
