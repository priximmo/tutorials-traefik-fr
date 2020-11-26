%title: TRAEFIK
%author: xavki


# TRAEFIK : Metrics



<br>


Documentation : 
	https://docs.traefik.io/observability/metrics/overview/

<br>


* différents types :
		* prometheus
		* influxdb
		* statsd
		* datadog

<br>


* influxdb

```
[metrics]
  [metrics.influxDB]
    address = "localhost:8089"
```

<br>


* prometheus

```
[metrics]
  [metrics.prometheus]
```

Rq : sur le port 8080 > route /metrics
Sinon :   address = ":8082"

---------------------------------------------------------------------

# TRAEFIK : Metrics



<br>


Options

* addEntryPointsLabels = true

* addServicesLabels = true

* redéfinition du bucket

```
    buckets = [0.1,0.3,1.2,5.0]
```
