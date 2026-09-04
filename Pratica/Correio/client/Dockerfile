FROM ubuntu:24.04

# Install the necessary packages for the mail client
RUN apt-get update && apt-get install -y \
    telnet \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*
