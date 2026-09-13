FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        iproute2 \
        iputils-ping \
        net-tools \
        tcpdump \
        && \
    rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
