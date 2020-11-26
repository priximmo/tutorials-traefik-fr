%title: TRAEFIK
%author: xavki


# TRAEFIK : TLS Options


<br>


Documentation :
Blog utile : https://tferdinand.net/traefik-2-configuration-du-tls/
Mozilla : https://ssl-config.mozilla.org/#server=traefik&version=2.3&config=intermediate&guideline=5.6

<br>


Checks : https://www.ssllabs.com/ssltest/analyze.html
CLI :

```
openssl s_client -showcerts -connect xavki.fr:443 -tls1_2
openssl s_client -showcerts -connect xavki.fr:443 2>/dev/null | openssl x509 -text -noout | grep "Public-Key"
```

<br>


* type et taille:

```
[certificatesResolvers]
  [certificatesResolvers.xavki_certs]
    [certificatesResolvers.xavki_certs.acme]
      email = "moi@gmail.com"
      caServer = "https://acme-v02.api.letsencrypt.org/directory"
      storage = "acme.json"
      keyType = "RSA4096"
      [certificatesResolvers.xavki_certs.acme.httpChallenge]   
        entryPoint = "xavki"
```

--------------------------------------------------------------------------------

# TRAEFIK : TLS Options


<br>


* ajout d'options

```
[http]
  [http.routers]
    [http.routers.xavki_route]
      entryPoints = ["xavki_secure"]
      service = "xavki"
      rule = "Host(`xavki.fr`) && Path(`/`)"
      middlewares = ["xavki_https"]
      [http.routers.xavki_route.tls]
        certResolver = "xavki_certs"
        options = "intermediate"
```

<br>


* version minimale de tls

```
[tls.options]
  [tls.options.default]
    minVersion = "VersionTLS12"
```

* version maximale

```
[tls.options]
  [tls.options.default]
    maxVersion = "VersionTLS12"
```

--------------------------------------------------------------------------------

# TRAEFIK : TLS Options


<br>


* avec les ciphers

```
[tls.options]
  [tls.options.intermediate]
    minVersion = "VersionTLS12"
    cipherSuites = [
      "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
      "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
      "TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305",
      "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305"
    ]
```

<br>


* en plus CAA : entrée DNS sépcifiant le fourniseur de certificat (CAA)



