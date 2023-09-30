#!/bin/bash
#Execute this from any directory inside the home directory. The setup repo should already satisfy this condition
mkdir ../yay && git clone https://aur.archlinux.org/yay.git ../yay && cd ../yay && makepkg -si
