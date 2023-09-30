
#Move wallpapers
sudo rm -rf /usr/share/wallpapers
rm -rf ~/wallpapers
sudo ln -s -r $HOME/documents/arch_setup/wallpapers/ /usr/share/
ln -s $HOME/documents/arch_setup/wallpapers ~/
nitrogen --set-auto ~/wallpapers/main_desktop_wall.jpg
