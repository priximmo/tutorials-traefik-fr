%title: TRAEFIK
%author: xavki


# TRAEFIK : Introduction


<br>


* reverse proxy

* Doc et site : https://docs.traefik.io/

<br>


* RP permet :
		* filtrage
		* enrichissement
		* chiffrement (tls)
		* compression
		* load-balancing
		* authentification

<br>


* traefik > langage GO

* édité par containous (Fr > Emile Vauge)

<br>


* traefik, sa force ?
		* discovery > providers (consul, docker, fichiers...)
		* échange direct avec let's encrypt (tls)

--------------------------------------------------------------------------

# TRAEFIK : Introduction

<br>


* différentes couches
		* http > osi 7 (applicative)
		* tcp > osi 4 (transport)
		* udp > osi 4 (transport)

<br>


* traefik :
		* interface graphique
		* exposition de métriques (prometheus routes...)
		* enregistrement du tracing (opentracing > jaeger)
		* discovery et mise à jour à chaud (ex : swarm...)

<br>


* installation :
		* via container (docker) : la plus répandu
		* via binaire

<br>


* configurations : toml ou yaml
		* Tom's Obvious, Minimal Language
