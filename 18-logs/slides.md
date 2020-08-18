%title: TRAEFIK
%author: xavki


# TRAEFIK : Logs



<br>
Documentation : 
	https://docs.traefik.io/observability/logs/
	https://docs.traefik.io/observability/access-logs/

* 2 types de logs :
		* logs : logs de traefik lui-même
		* access logs	: log des requêtes

* default = stdout

* les fichiers sont relachés > logrotate possible

<br>
* logs :
		* level (ERROR) : DEBUG, PANIC, FATAL, ERROR, WARN, INFO
		* filePath : localisation
		* format (common) : common (Common Log Format ou CLF) / json

---------------------------------------------------------------------------------------

# TRAEFIK : Logs


<br>
* access logs :
		* filePath : localisation
		* format (common) : common (Common Log Format ou CLF) / json
		* bufferingSize : nombre de ligne conservée en mémoire avant de les écrire

* filtre

```
[accessLog]
  filePath = "/path/to/access.log"
  format = "json"
  [accessLog.filters]    
    statusCodes = ["200", "300-302"]
    retryAttempts = true
    minDuration = "10ms"
```

* et limitation et formats possibles

https://docs.traefik.io/observability/access-logs/#limiting-the-fieldsincluding-headers

```
[accessLog]
  filePath = "/path/to/access.log"
  format = "json"
  [accessLog.fields]
    defaultMode = "keep"
    [accessLog.fields.names]
      "ClientUsername" = "drop"
```
