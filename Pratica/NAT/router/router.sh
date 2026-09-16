#!/bin/bash

set -e

echo "Interfaces:"
ip -br addr

echo
echo "Habilitando IPv4 forwarding..."

sysctl -w net.ipv4.ip_forward=1

echo
echo "Configurando NAT/PAT..."

iptables -t nat -A POSTROUTING \
    -s 192.168.10.0/24 \
    -o eth1 \
    -j MASQUERADE

echo
echo "Tabela NAT:"
iptables -t nat -L -n -v

echo
echo "Iniciando..."

sleep infinity