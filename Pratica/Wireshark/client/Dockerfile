FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        telnet \
        openssh-client \
        curl \
        iputils-ping \
        net-tools \
        dnsutils \
        && \
    rm -rf /var/lib/apt/lists/*

CMD ["bash"]
