FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        bind9 \
        bind9utils \
        dnsutils \
        iproute2 \
        iputils-ping && \
    rm -rf /var/lib/apt/lists/*

COPY named.conf /etc/bind/named.conf
COPY db.empresa.test /etc/bind/db.empresa.test
COPY db.172.20.0 /etc/bind/db.172.20.0

EXPOSE 53/udp
EXPOSE 53/tcp

CMD ["named", "-g", "-c", "/etc/bind/named.conf"]
