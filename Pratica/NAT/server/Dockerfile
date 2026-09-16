FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        apache2 \
        iproute2 \
        iputils-ping \
        tcpdump \
        && \
    rm -rf /var/lib/apt/lists/*

COPY index.html /var/www/html/index.html

CMD ["/bin/bash"]
