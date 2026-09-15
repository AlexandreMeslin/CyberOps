FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        isc-dhcp-server \
        iproute2 \
        tcpdump \
        iputils-ping && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/lib/dhcp && \
    touch /var/lib/dhcp/dhcpd.leases

COPY dhcpd.conf /etc/dhcp/dhcpd.conf

CMD ["sh", "-c", \
     "ip route add 10.10.0.0/24 via 192.168.50.3 2>/dev/null || true; \
      ip route add 10.20.0.0/24 via 192.168.50.3 2>/dev/null || true; \
      exec dhcpd -f -d --no-pid eth0"]
