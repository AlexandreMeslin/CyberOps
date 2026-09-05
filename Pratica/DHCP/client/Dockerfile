FROM ubuntu:24.04

# Evita perguntas interativas durante a instalação dos pacotes
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza a lista de pacotes, instala as ferramentas e limpa o cache
RUN apt-get update && apt-get install -y \
        iproute2 \
        net-tools \
        iputils-ping \
        isc-dhcp-client \
    && rm -rf /var/lib/apt/lists/*
    
CMD ["/bin/bash"]
