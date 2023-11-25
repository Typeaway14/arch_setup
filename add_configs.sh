#!/bin/bash


#Creating .xinitrc and .Xresources in  ~
rm ~/.xinitrc
ln -s $HOME/documents/arch_setup/config/xinitrc ~/.xinitrc
rm ~/.Xresources
ln -s $HOME/documents/arch_setup/config/Xresources ~/.Xresources

#Adding picom config
rm -rf ~/.config/picom.conf
rm -rf ~/.config/compfy
# cp -r ./config/picom.conf ~/.config/
# ln -s $HOME/documents/arch_setup/config/picom.conf ~/.config/picom.conf
ln -s $HOME/documents/arch_setup/config/compfy/ ~/.config/

#Adding startship.toml to .config
rm ~/.config/starship.toml
# cp ./config/starship.toml ~/.config/
ln -s ./config/starship.toml ~/.config/starship.toml

#Adding nvim config
rm -rf ~/.config/nvim/
# cp -r ./config/nvim/ ~/.config/
ln -s $HOME/documents/arch_setup/config/nvim/ ~/.config/

#Adding kitty config
rm -rf ~/.config/kitty/
# cp -r ./config/kitty/ ~/.config/
ln -s $HOME/documents/arch_setup/config/kitty/ ~/.config/

#Adding qutebrowser config
rm -rf ~/.config/qutebrowser/
# cp -r ./config/qutebrowser/ ~/.config/
ln -s $HOME/documents/arch_setup/config/qutebrowser/ ~/.config/

#Adding qtile config
rm -rf ~/.config/qtile/
# cp -r ./config/qtile/ ~/.config/
ln -s $HOME/documents/arch_setup/config/qtile/ ~/.config/

#Adding polybar config
rm -rf ~/.config/polybar/
# cp -r ./config/polybar/ ~/.config/
ln -s $HOME/documents/arch_setup/config/polybar/ ~/.config/

#Adding dunst config
rm -rf ~/.config/dunst/
# cp -r ./config/dunst/ ~/.config/
ln -s $HOME/documents/arch_setup/config/dunst/ ~/.config/


mkdir $HOME/burner_files
