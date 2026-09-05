# Laboratório de DNS

Neste laboratório, vamos investigar como um host converte endereço em formato texto (FQDN - Fully Qualified Domain Name) em endereço IP e vice-versa.

Faremos consultas do tipo:
- A
- MX
- Consulta direta
- Consulta reversa

Vamos usar o **named** como servidor DNS na nossa rede local.

## Bibliografia

- [DNS - Terminologia](https://datatracker.ietf.org/doc/html/rfc9499)
- [DNS - Implementação](https://datatracker.ietf.org/doc/html/rfc1035)
- [named - site](https://www.isc.org/bind/)
- [named - repositório](https://gitlab.isc.org/isc-projects/bind9)

## Procedimento

Suba os containers.

No host:

```bash
$ sudo docker compose up -d
```

Resultado esperado

```bash
$ sudo docker compose up -d
[+] Running 3/3
 ✔ Network dns_dns-net   Created                              0.1s 
 ✔ Container dns-server  Started                              0.4s 
 ✔ Container dns-client  Started                              0.4s 
```

Verifique se os containers estão no ar:

```bash
$ sudo docker ps -a
```

Resultado esperado:

```bash
$ sudo docker ps -a
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS            NAMES
4d7de0808d65   meslin/dns-client   "/bin/bash"              2 minutes ago   Up 2 minutes                    dns-client
ae78dd849be5   meslin/dns-server   "named -g -c /etc/bi…"   2 minutes ago   Up 2 minutes   53/tcp, 53/udp   dns-server
```

Verifique as redes existentes:

```bash
$ sudo docker network ls
```

Resultado esperado:

```bash
$ sudo docker network ls
NETWORK ID     NAME          DRIVER    SCOPE
626fb2ea3cb6   bridge        bridge    local
8034ff13b14f   dns_dns-net   bridge    local
1b5be87839cd   host          host      local
97f519bf0843   none          null      local
```

Verifique também a rede que foi criada:

```bash
$ sudo docker network inspect dns_dns-net
```

Resultado esperado:

```bash
 sudo docker network inspect dns_dns-net
[
    {
        "Name": "dns_dns-net",
        "Id": "8034ff13b14f52b08f52eab26c9cfa8224f71ef4f79db9749ca864dce6ff1331",
        "Created": "2026-09-05T09:26:54.423969666-03:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv4": true,
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.20.0.0/24",
                    "IPRange": "",
                    "Gateway": "172.20.0.1"
                }
            ]
        },
        "Internal": true,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Options": {},
        "Labels": {
            "com.docker.compose.config-hash": "9042241b33ba01349df1f33843f7332d254ee04d4ccd8704f695c6134c9012ed",
            "com.docker.compose.network": "dns-net",
            "com.docker.compose.project": "dns",
            "com.docker.compose.version": "2.40.3"
        },
        "Containers": {
            "4d7de0808d65a3437b4f03eba4412dd56abada4e5059afb6f76136ed001d7acb": {
                "Name": "dns-client",
                "EndpointID": "89e1c37070c286d9b5ba01f6a3ef8b3676b912261e74aad598b159d42f6786aa",
                "MacAddress": "8a:1f:09:00:09:96",
                "IPv4Address": "172.20.0.2/24",
                "IPv6Address": ""
            },
            "ae78dd849be53d4b6f165eadaa65f5f6fb59d1c3eca0798b1703c0064f8ad9e6": {
                "Name": "dns-server",
                "EndpointID": "ed3f8e2244190f778be1693d429038ad361f3ee3eb06d2b349fc337ea880ad1e",
                "MacAddress": "02:c7:a3:4b:8b:f5",
                "IPv4Address": "172.20.0.10/24",
                "IPv6Address": ""
            }
        },
        "Status": {
            "IPAM": {
                "Subnets": {
                    "172.20.0.0/24": {
                        "IPsInUse": 5,
                        "DynamicIPsAvailable": 251
                    }
                }
            }
        }
    }
]
```

Analise o log do servidor DNS.

No host:

```bash
$ sudo docker compose logs dns-server
```

Resultado esperado:

```bash
$ sudo docker compose logs dns-server
dns-server  | 05-Sep-2026 12:26:54.863 starting BIND 9.18.39-0ubuntu0.24.04.7-Ubuntu (Extended Support Version) <id:>
dns-server  | 05-Sep-2026 12:26:54.863 running on Linux x86_64 7.0.0-30-generic #30~24.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Aug  7 13:27:52 UTC 2
dns-server  | 05-Sep-2026 12:26:54.863 built with  '--build=x86_64-linux-gnu' '--prefix=/usr' '--includedir=${prefix}/include' '--mandir=${prefix}/share/man' '--infodir=${prefix}/share/info' '--sysconfdir=/etc' '--localstatedir=/var' '--disable-option-checking' '--disable-silent-rules' '--libdir=${prefix}/lib/x86_64-linux-gnu' '--runstatedir=/run' '--disable-maintainer-mode' '--disable-dependency-tracking' '--libdir=/usr/lib/x86_64-linux-gnu' '--sysconfdir=/etc/bind' '--with-python=python3' '--localstatedir=/' '--enable-threads' '--enable-largefile' '--with-libtool' '--enable-shared' '--disable-static' '--with-gost=no' '--with-openssl=/usr' '--with-gssapi=yes' '--with-libidn2' '--with-json-c' '--with-lmdb=/usr' '--with-gnu-ld' '--with-maxminddb' '--with-atf=no' '--enable-ipv6' '--enable-rrl' '--enable-filter-aaaa' '--disable-native-pkcs11' 'build_alias=x86_64-linux-gnu' 'CFLAGS=-g -O2 -fno-omit-frame-pointer -mno-omit-leaf-frame-pointer -ffile-prefix-map=/build/bind9-8LYxaJ/bind9-9.18.39=. -flto=auto -ffat-lto-objects -fstack-protector-strong -fstack-clash-protection -Wformat -Werror=format-security -fcf-protection -fdebug-prefix-map=/build/bind9-8LYxaJ/bind9-9.18.39=/usr/src/bind9-1:9.18.39-0ubuntu0.24.04.7 -fno-strict-aliasing -fno-delete-null-pointer-checks -DNO_VERSION_DATE -DDIG_SIGCHASE' 'LDFLAGS=-Wl,-Bsymbolic-functions -flto=auto -ffat-lto-objects -Wl,-z,relro -Wl,-z,now -ledit' 'CPPFLAGS=-Wdate-time -D_FORTIFY_SOURCE=3'
dns-server  | 05-Sep-2026 12:26:54.863 running as: named -g -c /etc/bind/named.conf
dns-server  | 05-Sep-2026 12:26:54.863 compiled by GCC 13.3.0
dns-server  | 05-Sep-2026 12:26:54.863 compiled with OpenSSL version: OpenSSL 3.0.13 30 Jan 2024
dns-server  | 05-Sep-2026 12:26:54.863 linked to OpenSSL version: OpenSSL 3.0.13 30 Jan 2024
dns-server  | 05-Sep-2026 12:26:54.863 compiled with libuv version: 1.48.0
dns-server  | 05-Sep-2026 12:26:54.863 linked to libuv version: 1.48.0
dns-server  | 05-Sep-2026 12:26:54.864 compiled with libxml2 version: 2.9.14
dns-server  | 05-Sep-2026 12:26:54.864 linked to libxml2 version: 20914
dns-server  | 05-Sep-2026 12:26:54.864 compiled with json-c version: 0.17
dns-server  | 05-Sep-2026 12:26:54.864 linked to json-c version: 0.17
dns-server  | 05-Sep-2026 12:26:54.864 compiled with zlib version: 1.3
dns-server  | 05-Sep-2026 12:26:54.864 linked to zlib version: 1.3
dns-server  | 05-Sep-2026 12:26:54.864 ----------------------------------------------------
dns-server  | 05-Sep-2026 12:26:54.864 BIND 9 is maintained by Internet Systems Consortium,
dns-server  | 05-Sep-2026 12:26:54.864 Inc. (ISC), a non-profit 501(c)(3) public-benefit 
dns-server  | 05-Sep-2026 12:26:54.864 corporation.  Support and training for BIND 9 are 
dns-server  | 05-Sep-2026 12:26:54.864 available at https://www.isc.org/support
dns-server  | 05-Sep-2026 12:26:54.864 ----------------------------------------------------
dns-server  | 05-Sep-2026 12:26:54.864 found 12 CPUs, using 12 worker threads
dns-server  | 05-Sep-2026 12:26:54.864 using 12 UDP listeners per interface
dns-server  | 05-Sep-2026 12:26:54.870 DNSSEC algorithms: RSASHA1 NSEC3RSASHA1 RSASHA256 RSASHA512 ECDSAP256SHA256 ECDSAP384SHA384 ED25519 ED448
dns-server  | 05-Sep-2026 12:26:54.870 DS algorithms: SHA-1 SHA-256 SHA-384
dns-server  | 05-Sep-2026 12:26:54.870 HMAC algorithms: HMAC-MD5 HMAC-SHA1 HMAC-SHA224 HMAC-SHA256 HMAC-SHA384 HMAC-SHA512
dns-server  | 05-Sep-2026 12:26:54.870 TKEY mode 2 support (Diffie-Hellman): yes
dns-server  | 05-Sep-2026 12:26:54.870 TKEY mode 3 support (GSS-API): yes
dns-server  | 05-Sep-2026 12:26:54.872 the initial working directory is '/'
dns-server  | 05-Sep-2026 12:26:54.872 loading configuration from '/etc/bind/named.conf'
dns-server  | 05-Sep-2026 12:26:54.872 the working directory is now '/var/cache/bind'
dns-server  | 05-Sep-2026 12:26:54.872 reading built-in trust anchors from file '/etc/bind/bind.keys'
dns-server  | 05-Sep-2026 12:26:54.872 looking for GeoIP2 databases in '/usr/share/GeoIP'
dns-server  | 05-Sep-2026 12:26:54.872 using default UDP/IPv4 port range: [32768, 60999]
dns-server  | 05-Sep-2026 12:26:54.872 using default UDP/IPv6 port range: [32768, 60999]
dns-server  | 05-Sep-2026 12:26:54.873 listening on IPv4 interface lo, 127.0.0.1#53
dns-server  | 05-Sep-2026 12:26:54.882 listening on IPv4 interface eth0, 172.20.0.10#53
dns-server  | 05-Sep-2026 12:26:54.882 generating session key for dynamic DNS
dns-server  | 05-Sep-2026 12:26:54.883 sizing zone task pool based on 2 zones
dns-server  | 05-Sep-2026 12:26:54.883 none:99: 'max-cache-size 90%' - setting to 28753MB (out of 31948MB)
dns-server  | 05-Sep-2026 12:26:54.893 set up managed keys zone for view _default, file 'managed-keys.bind'
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 10.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 16.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 17.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 18.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 19.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 21.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 22.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 23.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 24.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 25.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 26.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 27.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 28.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 29.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 30.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 31.172.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 168.192.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 64.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 65.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 66.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 67.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 68.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 69.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 70.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 71.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 72.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 73.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 74.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 75.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 76.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 77.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 78.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 79.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 80.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 81.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 82.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 83.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.893 automatic empty zone: 84.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 85.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 86.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 87.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 88.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 89.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 90.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 91.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 92.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 93.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 94.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 95.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 96.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 97.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 98.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 99.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 100.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 101.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 102.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 103.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 104.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 105.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 106.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 107.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 108.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 109.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 110.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 111.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 112.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 113.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 114.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 115.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 116.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 117.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 118.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 119.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 120.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 121.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 122.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 123.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 124.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 125.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 126.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 127.100.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.894 automatic empty zone: 0.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 127.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 254.169.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 2.0.192.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 100.51.198.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 113.0.203.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 255.255.255.255.IN-ADDR.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: D.F.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 8.E.F.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 9.E.F.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: A.E.F.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: B.E.F.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: 8.B.D.0.1.0.0.2.IP6.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: EMPTY.AS112.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: HOME.ARPA
dns-server  | 05-Sep-2026 12:26:54.895 automatic empty zone: RESOLVER.ARPA
dns-server  | 05-Sep-2026 12:26:54.904 configuring command channel from '/etc/bind/rndc.key'
dns-server  | 05-Sep-2026 12:26:54.904 open: /etc/bind/rndc.key: permission denied
dns-server  | 05-Sep-2026 12:26:54.904 command channel listening on 127.0.0.1#953
dns-server  | 05-Sep-2026 12:26:54.904 configuring command channel from '/etc/bind/rndc.key'
dns-server  | 05-Sep-2026 12:26:54.904 open: /etc/bind/rndc.key: permission denied
dns-server  | 05-Sep-2026 12:26:54.904 command channel listening on ::1#953
dns-server  | 05-Sep-2026 12:26:54.904 not using config file logging statement for logging due to -g option
dns-server  | 05-Sep-2026 12:26:54.905 managed-keys-zone: loaded serial 0
dns-server  | 05-Sep-2026 12:26:54.909 /etc/bind/db.172.20.0:17: file does not end with newline
dns-server  | 05-Sep-2026 12:26:54.909 zone 20.172.in-addr.arpa/IN: loaded serial 2026090501
dns-server  | 05-Sep-2026 12:26:54.913 /etc/bind/db.empresa.test:20: file does not end with newline
dns-server  | 05-Sep-2026 12:26:54.913 zone empresa.test/IN: loaded serial 2026090501
dns-server  | 05-Sep-2026 12:26:54.913 all zones loaded
dns-server  | 05-Sep-2026 12:26:54.913 running
```

### Entrar no cliente

No host:

```bash
 sudo docker exec -it dns-client bash
```

Resultado esperado:

```bash
$ sudo docker exec -it dns-client bash
root@client:/# 
```

Consulte um FQDN fictício.

No cliente:

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```

```bash

```
