
# sudo cp ./sddm/mountain /usr/share/sddm/themes/
sudo rm -rf /usr/share/sddm/themes/mountain
sudo ln -s $HOME/documents/arch_setup/config/sddm/mountain /usr/share/sddm/themes/
# sudo cp ./sddm/default.conf /usr/lib/sddm/sddm.conf.d/
sudo rm /usr/lib/sddm/sddm.conf.d/default.conf
sudo ln -s $HOME/documents/arch_setup/config/sddm/mountain/theme.conf /usr/lib/sddm/sddm.conf.d/default.conf
