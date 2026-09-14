# CyberOps

[![License: MIT](https://img.shields.io/badge/license-MIT-orange.svg)](https://opensource.org/licenses/MIT)
![Contributors](https://img.shields.io/github/contributors/AlexandreMeslin/CyberOps)
![Open Issues](https://img.shields.io/github/issues/AlexandreMeslin/CyberOps)
![Open PRs](https://img.shields.io/github/issues-pr/AlexandreMeslin/CyberOps)
![GitHub Created At](https://img.shields.io/github/created-at/AlexandreMeslin/CyberOps)

![PRs Welcome](https://img.shields.io/badge/PRs-welcome-magenta.svg)
![Pull Requests](https://img.shields.io/github/issues-pr/AlexandreMeslin/CyberOps)
![Students](https://img.shields.io/badge/Students-Contributions%20Welcome-yellow)

![HTML](https://img.shields.io/badge/language-HTML-brown.svg)
![Python](https://img.shields.io/badge/language-Python-yellow.svg)
![CSS](https://img.shields.io/badge/language-CSS-red.svg)
![Top Language](https://img.shields.io/github/languages/top/AlexandreMeslin/CyberOps)
![Languages Count](https://img.shields.io/github/languages/count/AlexandreMeslin/CyberOps)

![Last Commit](https://img.shields.io/github/last-commit/AlexandreMeslin/CyberOps)
![Repo Size](https://img.shields.io/github/repo-size/AlexandreMeslin/CyberOps)
![Code Size](https://img.shields.io/github/languages/code-size/AlexandreMeslin/CyberOps)
![GitHub commits since tagged version](https://img.shields.io/github/commits-since/AlexandreMeslin/CyberOps/v2026.2)


![GitHub stars](https://img.shields.io/github/stars/AlexandreMeslin/CyberOps?style=social)
![GitHub forks](https://img.shields.io/github/forks/AlexandreMeslin/CyberOps?style=social)
![GitHub followers](https://img.shields.io/github/followers/AlexandreMeslin)
![GitHub User's stars](https://img.shields.io/github/stars/AlexandreMeslin)
![GitHub watchers](https://img.shields.io/github/watchers/AlexandreMeslin/CyberOps)

**Frameworks & Ferramentas:**

![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)

**Community Profile**

![License](https://img.shields.io/github/license/AlexandreMeslin/CyberOps)
![Contributing](https://img.shields.io/badge/Contributing-Yes-brightgreen)
![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-Yes-blue)
![Security Policy](https://img.shields.io/badge/Security-Policy-red)
![Support](https://img.shields.io/badge/Support-Available-orange)

![Community Profile](https://img.shields.io/badge/Community%20Profile-100%25-success)

![CITATION.cff](https://img.shields.io/badge/Citation-CFF-blueviolet)
![Open Science](https://img.shields.io/badge/Open%20Science-Ready-success)
![PUC-Rio](https://img.shields.io/badge/PUC--Rio-Department%20of%20Informatics-003366)

![Governance](https://img.shields.io/badge/Governance-Defined-blue)
![Code Owners](https://img.shields.io/badge/CODEOWNERS-Enabled-lightgrey)
![Roadmap](https://img.shields.io/badge/Roadmap-Published-informational)

![Course](https://img.shields.io/badge/Course-CyberOps-blue)
![PUC-Rio](https://img.shields.io/badge/Institution-PUC--Rio-003366)
![Semester](https://img.shields.io/badge/Semester-2026.1-lightgrey)
![Educational](https://img.shields.io/badge/Educational-Repository-brightgreen)


## Contribuindo

Interessado em contribuir? Confira nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para encontrar recursos sobre como contribuir, além de um guia sobre como configurar um ambiente de desenvolvimento.

### Junte-se à nossa incrível comunidade como colaborador de código

![Imagem com os contribuidores](https://contrib.rocks/image?repo=AlexandreMeslin/CyberOps&anon=0&columns=25&max=100&r=true)

Repositório para o curso de extensão de CyberOps da PUC-Rio, cobrindo a teoria e a prática dos principais conceitos de redes e protocolos.

## Ementa

- Conceitos de Redes de Comunicação de Dados: PAN, LAN, MAN e WAN
- Topologias: física e lógica
- Modelo de Referência OSI: funcionalidades das 7 camadas
- Arquitetura TCP/IP
  - Operação básica dos protocolos de rede (ARP, IP)
  - Transporte (TCP, UDP)
  - Aplicação (DHCP, HTTP, FTP, SMTP, POP3, IMAP)
- Domain Name System (DNS)

## Objetivo do curso

O objetivo do curso é consolidar os fundamentos de redes e protocolos por meio de aulas teóricas e atividades práticas aplicadas ao contexto de CyberOps.

## Erros e suas "soluções"

### Permissão negada

#### Descrição

Não tem permissão para se conectar ao daemon.

#### Sintoma

```bash
$ docker compose up -d
unable to get image 'meslin/arp-client:latest': permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/images/meslin/arp-client:latest/json": dial unix /var/run/docker.sock: connect: permission denied
```

#### Solução

Esqueceu de usar `sudo`?

Tente de novo:

```bash
$ sudo docker compose up -d
```

---

### Sem permissão de executar algum comando de rede

#### Descrição

Não consegue executar algum comando relativo a rede do container porque a operação não é permitida.

#### Sintoma

```
oot@af453b5aab70:/# ip neigh flush all
Failed to send flush request: Operation not permitted
```

#### Solução

Acrescente as permissões no arquivo `docker-compose.yaml` na descrição do serviço:

```yaml
    cap_add:
      - NET_ADMIN
      - NET_RAW
```

---

### Endereço do Lab já em uso

#### Descrição

Não consegue subir o lab porque o Docker informa que o endereço do lab já está em uso.

#### Sintoma:

```
$ sudo docker compose up -d
[+] Running 5/6
 ✔ Network arp_arp-net    Created                                                                                                                                                  0.0s 
 ✔ Network arp_net2       Created                                                                                                                                                  0.1s 
 ⠦ Container arp-router   Starting                                                                                                                                                 0.6s 
 ✔ Container arp-client2  Started                                                                                                                                                  0.5s 
 ✔ Container arp-client3  Started                                                                                                                                                  0.5s 
 ✔ Container arp-client1  Started                                                                                                                                                  0.6s 
Error response from daemon: failed to set up container networking: Address already in use
```

#### Solução

Inspecione as redes do lab com o comando (troque o nome da rede pelo nome adequado - veja o seu `docker-compose.yaml`):

```bash
$ sudo docker network inspect arp_arp-net
```

Procure por algum container que ainda esteja agarrado a essa rede, por exemplo, o container `arp-client1` como mostrado a seguir:

```bash
 sudo docker network inspect arp_arp-net
[
    {
        "Name": "arp_arp-net",
        "Id": "134525f489339bb83f8e4e38b8665598c2ac10d64352ad43a184ca87be5b61a0",
        "Created": "2026-09-13T19:55:07.471505202-03:00",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv4": true,
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "192.168.1.0/24",
                    "IPRange": "",
                    "Gateway": "192.168.1.1"
                }
            ]
        },
        "Internal": false,
        "Attachable": false,
        "Ingress": false,
        "ConfigFrom": {
            "Network": ""
        },
        "ConfigOnly": false,
        "Options": {},
        "Labels": {
            "com.docker.compose.config-hash": "bff2868b5f812404c30c03af39506520c2b49cdbb7d154a2ec03101e31d952bb",
            "com.docker.compose.network": "arp-net",
            "com.docker.compose.project": "arp",
            "com.docker.compose.version": "2.40.3"
        },
        "Containers": {
            "4e5b3fc2c3751aaed106c23850ebfd431717930f23ffb83d90e5c8f5b134267f": {
                "Name": "arp-client1",
                "EndpointID": "a9b3b2925569d633ebb2e7cf10bbd4b60c8d6596830dc9cdf192b561d5a5676b",
                "MacAddress": "92:be:42:e3:bf:20",
                "IPv4Address": "192.168.1.10/24",
                "IPv6Address": ""
            }
        },
        "Status": {
            "IPAM": {
                "Subnets": {
                    "192.168.1.0/24": {
                        "IPsInUse": 4,
                        "DynamicIPsAvailable": 252
                    }
                }
            }
        }
    }
]
```

Pare e remova todos os containers que aparecerem conectados às redes que vamos usar:

```bash
$ sudo docker stop arp-client1
arp-client1
$ sudo docker rm arp-client1
arp-client1
```

---