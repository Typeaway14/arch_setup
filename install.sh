#!/bin/bash

ARCH_PACKAGES="\
networkmanager \
acpi \
amd-ucode \
base \
base-devel \
bluez \
bluez-utils \
bash-completion \
cheese \
brightnessctl \
code \
cowsay \
dbus-python \
dosfstools \
dunst \
efibootmgr \
eza \
feh \
firefox \
flameshot \
fortune-mod \
fzf \
git \
gparted \
htop \
iptables-nft \
kitty \
lolcat \
mtools \
mkinitcpio \
nano \
neofetch \
neovim \
nitrogen \
npm \
ntfs-3g \
ntp \
os-prober \
pavucontrol \
picom \
polybar \
pulseaudio \
pulseaudio-bluetooth \
python-dbus-next \
python-pip \
python-psutil \
qbittorrent \
qt5-graphicaleffects \
qt5-quickcontrols \
qt5-quickcontrols2 \
qtile \
qutebrowser \
ripgrep \
rofi \
sddm \
spotify-launcher \
sl \
starship \
sudo \
sshfs \
sxhkd \
thunar \
unzip \
vi \
telegram-desktop \
vim \
arandr \
vlc \
playerctl \
nnn \
yt-dlp \
xorg \
zip "

AUR_PACKAGES="\
pulseaudio-ctl \
qtile-extras-git \
rofi-power-menu \
whatsdesk-bin \
ruby-mdless \
zscroll-git"


#System update
sudo pacman -Syu

# Install all needed packages
sudo pacman -S $ARCH_PACKAGES

#Setup AUR-helper Yay
# ./aur_setup.sh

# Install all needed aur packages
yay -S $AUR_PACKAGES



