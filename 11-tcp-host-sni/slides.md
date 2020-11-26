%title: TRAEFIK
%author: xavki


# TRAEFIK : TCP HostSNI


<br>


* documentation : https://docs.traefik.io/routing/routers/#configuring-tcp-routers

<br>


* 3 modes : HTTP / TCP / UDP

<br>


* TCP > sans manipuler les entêtes etc (TCP vs HTTP)

<br>


* TCP > load balancing transparent (ex : bases de données)

<br>


* possiblité de faire du passthrough (cf playlist haproxy) :
		* client > traefik transparent > serveur tls
		* à la différence de la vidéo https
			* client > traefik tls > server sans tls

<br>


* pb TCP filtering > host header (HTTP)
		* SNI > TLS permet d'utiliser le Host SNI > plusieurs services load balancés


---------------------------------------------------------------------------------------

# TRAEFIK : Docker Provider - Routers Rules

<br>


* entrypoint (static configuration)

```
  [entryPoints.mysql]
    address=":3306"
```

* utilisation via docker-compose (partie dynamique) et sans TLS (HostSNI = \*)

```
version: '3'
services:
  db:
    image: mysql:5.7
    ports:
    - 192.168.13.11:3306:3306
    environment:
      - MYSQL_ROOT_PASSWORD=root
    labels:
      - traefik.tcp.routers.mysql.rule=HostSNI(`*`)
      - traefik.tcp.routers.mysql.entrypoints=mysql
```

<br>


* test

```
mysql -h 192.168.13.10 -u root -p
```
