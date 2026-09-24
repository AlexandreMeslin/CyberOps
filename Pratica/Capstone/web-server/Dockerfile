FROM httpd:latest

RUN apt-get update \
    && apt-get install -y \
        iproute2 \
        isc-dhcp-client \
        iputils-ping \
        curl \
        iptables \
    && rm -rf /var/lib/apt/lists/*
