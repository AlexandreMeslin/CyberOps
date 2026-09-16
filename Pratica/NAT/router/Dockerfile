FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        iproute2 \
        iptables \
        iputils-ping \
        tcpdump \
        && \
    rm -rf /var/lib/apt/lists/*

COPY router.sh /usr/local/bin/router.sh

RUN chmod +x /usr/local/bin/router.sh

CMD ["/bin/bash"]
