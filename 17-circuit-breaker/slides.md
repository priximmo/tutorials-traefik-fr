%title: TRAEFIK
%author: xavki


# TRAEFIK : Middlewares - CircuitBreaker



<br>
Documentation : https://docs.traefik.io/middlewares/circuitbreaker/

* circuitbreaker

	Client > Traefik > Service A > Trigger > 503 ? 

<br>
* 3 triggers
		* NetworkErrorRatio : 
				NetworkErrorRatio() > 0.30
		* ResponseCodeRatio
				ResponseCodeRatio(500, 600, 0, 600) > 0.25
		* LatencyAtQuantileMS
				LatencyAtQuantileMS(50.0) > 100 

<br>
* combinaison avec des opérateurs : && ||
		* et bien sûr : < > != == ...

<br>
* différents états
    * Close : fonctionne normalement
    * Open : sortie du service
    * Recovering : situation en cours de rétablissement

<br>
* complément
		* un circuit breaker est évalué en sortie de chain
		* un circuit breaker peut être utiliser par différents router
		* retourne seulement des 503


