#!/bin/bash

#Install all needed packages
./install.sh

#Clone necessary repos from Typeaway14 github
./clone_repos.sh

#Prepare bashrc
rm ~/.bashrc
# cp ./config/bashrc ~/.bashrc
ln -s $HOME/documents/arch_setup/config/bashrc ~/.bashrc

#Add configs for various programs
./add_configs.sh

#Start systemctl services
./systemctl_start.sh

#Setup wallpapers for grub and nitrogen
./set_wallpapers.sh

#Add SDDM theme
./set_sddm.sh

#Add fonts 


