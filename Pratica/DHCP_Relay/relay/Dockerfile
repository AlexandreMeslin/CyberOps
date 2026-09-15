FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        isc-dhcp-relay \
        iproute2 \
        iputils-ping \
        ethtool \
        tcpdump \
        && \
    rm -rf /var/lib/apt/lists/*

COPY relay.sh /usr/local/bin/relay.sh

RUN chmod +x /usr/local/bin/relay.sh

CMD ["/usr/local/bin/relay.sh"]
