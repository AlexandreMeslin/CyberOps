# Laboratório de Wireshark

## Requisitos

- Docker
- Wireshark

## Bibliografia

- [Docker](https://www.docker.com/)
- [Wireshark](https://www.wireshark.org/)

## Instalação

- Abra o terminal do Linux

### Wireshack

- Atualize a lista de pacotes do sistema:

```bash
$ sudo apt update
```

- Instale o Wireshark

```bash
$ sudo apt install -y wireshark
```

> [!NOTE]
> Se perguntado, durante a instalação, se non-superusers devem ter a capacidade de captura pacotes, selecione `Yes`

### Docker e Docker Compose

[Instalação do Docker](https://docs.docker.com/engine/install/ubuntu/)

> [!NOTE]
> A documentação oficial recomenda remover os pacotes antigos, se houver

- Remova os pacotes antigos:

```bash
$ sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc docker-buildx podman-docker containerd runc | cut -f1)
```

- Atualize a lista de pacotes do sistema:

```bash
$ sudo apt update
```

- Instale os pré-requisitos:

```bash
$ sudo apt install -y ca-certificates curl
```

- Adicione a chave GPG do Docker

```bash
$ sudo install -m 0755 -d /etc/apt/keyrings
$ sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
$ sudo chmod a+r /etc/apt/keyrings/docker.asc
```

- Adicione o repositório do docker no APT

```bash
$ sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF
$ sudo apt update
```

- Instale o Docker:

```bash
$ sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

- Verifique a instalação

```bash
$ sudo docker run hello-world
```

## Procedimento

### Containers

Execute os containers.

No host (no seu laptop):

```bash
$ sudo docker compose up -d
```

Resultado esperado:

```bash
$ sudo docker compose up -d
[+] Running 3/3
 ✔ Network wireshark_wireshark-net  Created                     0.0s 
 ✔ Container wireshark-server       Started                     1.1s 
 ✔ Container wireshark-client       Started                     1.0s 
```

Verifique se os containers `wireshark-server` e `wireshark-client` estão rodando.

No host:

```bash
$ sudo docker ps -a
```

Resultado esperado:

```bash
$ sudo docker ps -a
CONTAINER ID   IMAGE                            COMMAND                  CREATED         STATUS         PORTS                                                                                  NAMES
8aaf8e5f79c1   meslin/wireshark-server:latest   "/bin/sh -c 'service…"   9 seconds ago   Up 8 seconds   0.0.0.0:22-23->22-23/tcp, [::]:22-23->22-23/tcp, 0.0.0.0:80->80/tcp, [::]:80->80/tcp   wireshark-server
c8e95e464e99   meslin/wireshark-client:latest   "bash"                   9 seconds ago   Up 8 seconds                                                                                          wireshark-client
```

Entre no container do cliente.

No host:


```bash
$ sudo docker exec -it wireshark-client bash
```

Resultado esperado:

```
$ sudo docker exec -it wireshark-client bash
root@client:/# 
```

### Captura de uma sessão Telnet

Abra o Wireshark.
Selecione a interface iniciada com `br-`.
Inicie a captura clicando na barbatana azul.

Abra uma sessão telnet do cliente no servidor.

![Wireshark - seleção de interface](img/Wireshak-interface.png)

No cliente:

```
root@client:/# telnet wireshark-server
```

Resultado esperado

```
oot@client:/# telnet wireshark-server
Trying 172.18.0.3...
Connected to wireshark-server.
Escape character is '^]'.

Linux 7.0.0-30-generic (server) (pts/0)

server login:
```

Use as seguintes credenciais

- Username: aluno
- Password: senha123

> [!NOTE]
> Observe que nada aparece quando você digita a senha - seja JEDI!!!

```
server login: aluno
Password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 7.0.0-30-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
aluno@server:~$
```

Entre com alguns comandos, por exemplo:

```bash
ls -l
pwd
```

E depois termine a sessão com o comando `exit`

Resultado esperado:

```
aluno@server:~$ ls -l
total 0
aluno@server:~$ pwd
/home/aluno
aluno@server:~$ exit
logout
Connection closed by foreign host.
root@client:/# 
```

Pare a captura clicando no botão quadrado vermelho do Wireshark.

Veja que muitos datagramas foram capturados, mas poucos deles nos importam agora.
Use `telnet` como filtro.
Depois de filtrado, verifique os datagramas.
Alguns datagramas importantes devem estar faltando, então vamos filtrar pelo fluxo TCP.

Selecione um datagrama `Telnet` e use `Follow` > `TCP Stream`.

![Wireshark - TCP Stream](img/Wireshark-tcp_stream.png)

Veja que o Wireshark agora mostra toda a captura da sessão, colocando as mensagens do servidor em azul e as do cliente em vermelho.

Agora percorra cada um dos pacotes já filtrados e verifique o campo `Telnet` da camada de aplicação.

### Captura HTTP

Remova o filtro clicando no X no final da linha do filtro.
Inicie uma nova captura no Wireshark clicando na barbatana azul.
Opcionalmente salve essa captura.

Acesse uma página HTML no servidor.

No cliente:

```
root@client:/# curl http://wireshark-server
```

Resultado esperado:

```
root@client:/# curl http://wireshark-server
<!DOCTYPE html>
<html>
<head>
    <title>Wireshark Lab</title>
</head>
<body>

<h1>Laboratório de Wireshark</h1>

<p>Esta página está sendo servida pelo container server.</p>

<p>Protocolo: HTTP</p>

</body>
</html>
```

Pare a captura no Wireshark clicando no botão quadrado vermelho.

Novamente observe que muitos datagramas foram capturados.
Você poderia novamente filtrar pela aplicação (`http`), mas, desta vez, vamos filtrar pela porta.
Use o filtro `tcp.port == 80`.
Veja que somente a sessão HTTP está sendo exibida.

![Wireshark - Captura HTTP](img/Wireshark-captura-HTTP.png)

Clique com o botão da direita do mouse em qualquer um dos pacotes HTTP e selecione `Follow` > `HTTP Stream`.

![Wireshark - HTTP Stream](img/Wireshark-HTTP_Stream.png)

> [!TIP]
> Selecione `UTF-8` na opção `Show data as`

Analise o resultado.
Veja que toda a sessão HTTP é mostrada na janela.
Dados do servidor em azul e do cliente em vermelho.

Agora, realize o mesmo procedimento acessando uma página via https, como, por exemplo, a home-page da PUC-Rio:

No cliente:

```
root@client:/# curl https://www.puc-rio.br
```

Pare a captura no Wireshark.

Filtre pela porta HTTPS 443.

Clique com o botão da direita do mouse em qualquer um dos pacotes e selecione `Follow` > `TCP Stream`.
Veja que você consegue ler os dados que vieram no seu cliente, mas não consegue ler os dados capturados.

### Captura SSH

Refaça os passos da captura Telnet, mas agora usando SSH.

Inicie a captura no Wireshark clicando na barbatana azul.

Abra uma sessão ssh a partir do cliente.

No cliente:

```
root@client:/# ssh aluno@wireshark-server
```

> Responda `yes` quando perguntado se deseja continuar.

Resultado esperado:

```
root@client:/# ssh aluno@wireshark-server
The authenticity of host 'wireshark-server (172.18.0.3)' can't be established.
ED25519 key fingerprint is SHA256:lSwxx1/tUUfYvY8FlaFo49eyDIGM7If3DQmT6UNKGQk.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'wireshark-server' (ED25519) to the list of known hosts.
aluno@wireshark-server's password: 
Welcome to Ubuntu 24.04.4 LTS (GNU/Linux 7.0.0-30-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
```

Entre com alguns comandos, por exemplo:

```bash
ls -l
pwd
```

E depois termine a sessão com o comando `exit`

Resultado esperado:

```
aluno@server:~$ ls
aluno@server:~$ pwd
/home/aluno
aluno@server:~$ exit
logout
Connection to wireshark-server closed.
root@client:/# 
```

Pare a captura no Wireshark clicando no quadradro vermelho.

![Wireshark - Captura SSH](img/Wireshark-captura-ssh.png)

Filtre pela porta 22 (`tcp.port == 22`).
Siga o fluxo TCP e veja se consegue obter alguma informação sobre conta, senha ou o que o usuário digitou como você conseguiu facilmente ao usar telnet.

![Wireshark - Stream SSH](img/Wireshark-Stream-SSH.png)

## Dados

### Telnet

1. Explique porque o login ficou parecido com `aalluunnoo` e a senha apenas ficou `senha123`.
1. Verifique o IP de origem.
1. Verifique o IP de destino.
1. Verifique o porta de origem.
1. Verifique o porta de destino.
1. Verifique o protocolo de transporte.
1. Verifique o handshake TCP.
1. Liste os dados da sessão capturados pelo Wireshark.

### HTTP

1. Verifique o IP de origem.
1. Verifique o IP de destino.
1. Verifique o porta de origem.
1. Verifique o porta de destino.
1. Verifique o protocolo de transporte.
1. Verifique o handshake TCP.
1. Liste os dados da sessção quer foram exibidos no Wireshark.
1. Compara conexão HTTP com uma HTTPS

### SSH

1. Verifique o IP de origem.
1. Verifique o IP de destino.
1. Verifique o porta de origem.
1. Verifique o porta de destino.
1. Verifique o protocolo de transporte.
1. Verifique o handshake TCP.
1. Verifique o dados da aplicação.
1. Informe o que aconteceu com os dados da sessão capturados pelo Wireshark
1. Compare a conexão SSH com a conexão Telnet.
