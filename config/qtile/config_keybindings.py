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

from functions import PWA

from os.path import expanduser

HOME = expanduser("~")

# Define constants here
TERMINAL = "kitty"


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
    ([CONTROL], "space", "playerctl play-pause -a"),
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
    ([MOD],      "m", "whatsdesk"),
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
    ([MOD, ALT],      "x", "bash -c xkill"),
    ([MOD, ALT],      "m", TERMINAL+" -e nmtui"),
    ([MOD, ALT],      "c", TERMINAL+" --directory ~/.config/ -e nvim"),
    ([MOD, ALT],      "b", TERMINAL+" --directory ~/.config/qutebrowser/ -e nvim ./config.py"),
    ([MOD, ALT],      "q", TERMINAL+" --directory ~/.config/qtile/ -e nvim ./config.py"),
    ([MOD, ALT],      "p", TERMINAL+" --directory ~/.config/polybar/ -e nvim ./config.ini"),

    # Webpages
    ([MOD,CONTROL], "m", "firefox --new-window monkeytype.com"),

    
]

##########################
# Your custom keys here  #
##########################

CUSTOM_SPAWN_KEYS = [
    # PWA keys
    ([MOD, ALT], "s", PWA.spotify()),
    # ([MOD, ALT], "m", PWA.music()),
    ([MOD, ALT], "t", PWA.calendar()),
    ([MOD, ALT], "y", PWA.youtube()),
    ([MOD, ALT], "l", PWA.notion()),
    ([MOD, ALT], "h", PWA.habitica()),
]


SPAWN_KEYS = HARDWARE_KEYS + APPS + CUSTOM_SPAWN_KEYS 

SPAWN_CMD_KEYS = [
    # Takes full screenshot and creates a file on the screenshot folder
    ([SHIFT],    "Print", f"xfce4-screenshooter -f -s {HOME}/Pictures/Screenshots/"),
]
