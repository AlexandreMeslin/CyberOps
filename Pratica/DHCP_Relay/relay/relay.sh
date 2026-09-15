#!/bin/bash

set -e

echo "Interfaces:"
ip -br addr

echo
echo "Desativando Checksum Offloading..."
ethtool -K eth0 tx off rx off 2>/dev/null || true
ethtool -K eth1 tx off rx off 2>/dev/null || true
ethtool -K eth2 tx off rx off 2>/dev/null || true

echo
echo "Habilitando IPv4 forwarding..."

sysctl -w net.ipv4.ip_forward=1

echo
echo "Iniciando DHCP Relay..."

exec dhcrelay \
    -d \
    -4 \
    -i eth0 \
    -i eth1 \
    -i eth2 \
    192.168.50.2
