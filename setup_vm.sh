#!/bin/bash

yay -S qemu virt-manager iptables-nft
sudo systemctl enable libvirtd
sudo systemctl start libvirtd
sudo usermod -G libvirt -a harsh117
sudo rm /etc/firewalld/firewalld.conf
sudo cp ./vm/firewalld.conf/ /etc/firewalld/firewalld.conf
