FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        openssh-server \
        telnetd \
        xinetd \
        apache2 \
        net-tools \
        iputils-ping \
        && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash aluno && \
    echo 'aluno:senha123' | chpasswd

COPY xinetd.conf /etc/xinetd.conf
COPY index.html /var/www/html/index.html

RUN mkdir -p /run/sshd

EXPOSE 22 23 80

CMD service xinetd start && \
    service apache2 start && \
    /usr/sbin/sshd -D
