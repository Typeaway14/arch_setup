"""
MODIFY THIS FILE TO CREATE CUSTOM KEYBINDINGS

Keybindings are configured with tuples, inside Predifined lists Variables

Modifier -> list() -> Ex: [MOD, CONTROL]

Key -> str() -> Ex: 'j'

Command -> str() -> Ex: vscode

(Modifier, Key, Command)
"""

from libqtile.confreader import ConfigError

# Import default mod keys
from keys.default import *

from os.path import expanduser

HOME = expanduser("~")

# Define constants here
# TERMINAL = "kitty"
TERMINAL = "xfce4-terminal"


# Basic window manager movements


# Qtile shutdown/restart keys
SHUTDOWN_MODIFIER = [MOD, CONTROL]
RESTART           = "r"
SHUTDOWN          = "q"


# Group movement keys:
GROUPS_KEY     = CONTROL
SWAP_GROUP_KEY = SHIFT

NEXT_GROUP = "period"
PREV_GROUP = "comma"


# ------------ Hardware Configs ------------
HARDWARE_KEYS = [
    # (Modifier, Key, Command)

    # Volume
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # Brightness
    ([], "XF86MonBrightnessUp", "brightnessctl set +2.5%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 2.5%-"),

    # Music 
    ([], "XF86AudioPrev", "playerctl previous -p spotify"),
    ([CONTROL], "XF86AudioPrev", "playerctl position 5- -p spotify"),
    ([], "XF86AudioPlay", "playerctl play-pause -p spotify"),
    ([CONTROL], "XF86AudioPlay", "playerctl play-pause -a"),
    # ([CONTROL], "space", "playerctl play-pause -a"),
    ([], "XF86AudioNext", "playerctl next"),
    ([CONTROL], "XF86AudioNext", "playerctl position 5+ -p spotify"),
]


APPS = [
    # (Modifier, Key, Command)

    #Applications
    ([MOD], "Return", TERMINAL),
    ([MOD],      "e", "thunar"),
    ([MOD], "a", "pavucontrol"),
    ([MOD],      "b", "qutebrowser"),
    ([MOD],      "v", "whatsdesk"),
    ([MOD],      "t", "telegram-desktop"),
    ([MOD], "s", "spotify-launcher"),


    # Run "rofi-theme-selector" in terminal to select a theme
        # ([MOD], "space", 'rofi -modi "drun,power-menu:rofi-power-menu,run,window,ssh" -show drun -show-icons'),
    ([MOD], "space", 'rofi -no-config -no-lazy-grab -show drun -theme ~/.config/polybar/scripts/rofi/launcher.rasi'),
        # ([MOD,CONTROL], "space", "rofi -no-config -no-lazy-grab -show run -theme ~/.config/polybar/scripts/rofi/launcher.rasi -disable-history -run-shell-command 'kitty --hold {cmd}'"),
    ([MOD,CONTROL], "space", "rofi -show calc -modi calc -no-sort -theme  ~/.config/polybar/scripts/rofi/launcher.rasi"),

    # Screenshots
    ([MOD, SHIFT], "s", "flameshot gui"),

    # Terminal apps
    ([MOD, ALT], "n", TERMINAL + " -e nvim"),
    ([MOD, ALT], "Return", TERMINAL+" --working-directory=/home/harsh117/documents/PES_Notes/SEM5/"),
    ([MOD, ALT],      "x", "bash -c xkill"),
    ([MOD, ALT],      "m", "kitty -e nmtui"),
    ([MOD, ALT],      "t", '''xfce4-terminal -e "bash -c 'cd ~/documents/Coding/TYRBO-on-terminal ; ./tyrbo b e'"'''),
    #### USE IF TERMINAL IS SET TO KITTY ####
    # ([MOD, ALT],      "c", TERMINAL+" --directory ~/.config/ -e nvim"),
    # ([MOD, ALT],      "b", TERMINAL+" --directory ~/.config/qutebrowser/ -e nvim ./config.py"),
    # ([MOD, ALT],      "q", TERMINAL+" --directory ~/.config/qtile/ -e nvim ./config.py"),
    # ([MOD, ALT],      "p", TERMINAL+" --directory ~/.config/polybar/ -e nvim ./config.ini"),
    #### USE IF TERMINAL IS SET TO XFCE4-TERMINAL ####
    ([MOD, ALT],      "c", '''xfce4-terminal -e "bash -c 'cd ~/.config/ ; nvim'"'''),
    ([MOD, ALT],      "b", '''xfce4-terminal -e "bash -c 'cd ~/.config/qutebrowser ; nvim config.py'"'''),
    ([MOD, ALT],      "q", '''xfce4-terminal -e "bash -c 'cd ~/.config/qtile ; nvim config.py'"'''),
    ([MOD, ALT],      "p", '''xfce4-terminal -e "bash -c 'cd ~/.config/polybar ; nvim config.ini'"'''),

    # Webpages
    ([MOD,CONTROL], "m", "firefox --new-window monkeytype.com"),
    ([MOD,CONTROL], "s", "qutebrowser --target window fast.com"),

    
]

SPAWN_KEYS = HARDWARE_KEYS + APPS 
