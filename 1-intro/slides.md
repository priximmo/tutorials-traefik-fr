%title: TRAEFIK
%author: xavki


# TRAEFIK : Introduction


<br>
* reverse proxy

* permet :
		* filtrage
		* enrichissement
		* chiffrement (tls)
		* compression
		* load-balancing
		* authentification

<br>
* traefik > langage GO

<br>
* traefik, sa force ?
		* discovery
		* échange direct avec let's encrypt (tls)

<br>
* différentes couches
		* http > osi 7 (appicative)
		* tcp > osi 4 (transport)
		* udp > osi 4 (transport)

<br>
* traefik :
		* interface graphique
		* exposition de métriques (prometheus routes...)
		* discovery et mise à jour à chaud (ex : swarm)

<br>
* installation :
		* via docker : la plus répandu
		* via binaire

<br>
* configurations : toml ou yaml
