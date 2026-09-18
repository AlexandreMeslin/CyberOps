FROM httpd:latest

RUN apt-get update \
    && apt-get install -y iproute2 \
    && rm -rf /var/lib/apt/lists/*