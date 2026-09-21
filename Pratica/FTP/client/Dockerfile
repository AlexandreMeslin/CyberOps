FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
        ftp \
        iputils-ping \
        net-tools \
        && rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
