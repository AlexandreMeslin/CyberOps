FROM httpd:latest

RUN apt-get update \
    && apt-get install -y \
        iproute2 \
        isc-dhcp-client \
        curl \
    && rm -rf /var/lib/apt/lists/*