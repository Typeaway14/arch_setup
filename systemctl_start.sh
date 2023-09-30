#start bluetooth
sudo systemctl enable bluetooth
sudo systemctl start bluetooth

#stop lightdm and start sddm
sudo systemctl stop lightdm
sudo systemctl disable lightdm
sudo systemctl enable sddm
sudo systemctl start sddm
