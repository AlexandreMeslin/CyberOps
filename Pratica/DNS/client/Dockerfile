FROM ubuntu:24.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        dnsutils \
        iproute2 \
        iputils-ping \
        net-tools && \
    rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
