FROM meslin/dhcp-relay:latest

RUN apt-get update \
    && apt-get install -y \
        iptables \
    && rm -rf /var/lib/apt/lists/*