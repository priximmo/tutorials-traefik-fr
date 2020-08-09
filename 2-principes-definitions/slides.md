%title: TRAEFIK
%author: xavki


# TRAEFIK : Principes & Définitions


<br>
* évolution de 1.7 à version 2.0

https://docs.traefik.io/
https://docs.traefik.io/v1.7/basics/

<br>
* traefik = edge router
		* capacité à analyser les requêtes pour les fournir aux bons services

<br>
* configuration via :
		* cli
		* config file
		* environment variables

<br>
* auto discovery
		* auto découvrir les services qu'il doit servir (sans intervention)
				* très utile pour docker (variation des ip)

------------------------------------------------------------------------------

# TRAEFIK : Principes & Définitions

<br>
STATIC CONFIGURATION : (démarrage > peu modifiée)

<br>
* Entrypoints :
		* points d'entrées
		* ports et adresses : [host]:port[/tcp|/udp]
		* redirection
		* forwarding ip
		* lets encrypt

<br>
* Providers : fournisseurs d'informations (registre de services)
		* doc :https://docs.traefik.io/providers/overview/
		* docker, kubernetes, consul...

------------------------------------------------------------------------------

# TRAEFIK : Principes & Définitions

<br>
DYNAMIC CONFIGURATION : (pendant le process > partie dynamique)

<br>
* Routers
		* règles de routages :
			* udp / tcp / http
			* /path > service-path
			* host
			* ou les deux
			* path/host > http/https
			* SNI (serveur name indication / TLS)

<br>
* Services
		* 1 service = 1 à multiples instances
		* load balancing
		* règles : sticky session, health check, round robin (weighted)
		* mirroring

<br>
* Middlewares
		* avant envoi de la requête aux services
		* modification : ex - ajout de path, réécriture, basic auth, compress, retry
		* doc : https://docs.traefik.io/middlewares/overview/

