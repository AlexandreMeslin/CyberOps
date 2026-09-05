FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        isc-dhcp-server \
        iproute2 \
        iputils-ping && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lib/dhcp && \
    touch /var/lib/dhcp/dhcpd.leases

COPY dhcpd.conf /etc/dhcp/dhcpd.conf

CMD ["dhcpd", "-f", "-d", "--no-pid", "eth0"]
