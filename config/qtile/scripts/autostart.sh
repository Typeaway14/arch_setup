#!/usr/bin/env bash
# ---
# Use "run program" to run it only if it is not already running
# Use "program &" to run it regardless
# ---
# NOTE: This script runs with every restart of AwesomeWM
# TODO: run_once


function run {
    if ! pgrep $1 > /dev/null ;
    then
        $@&
    fi
}

picom &
nitrogen --restore & 
~/.config/polybar/launch.sh &
# xrandr --output eDP --brightness 0.4
xinput set-prop "ASUE140D:00 04F3:31BC Touchpad" "libinput Tapping Enabled" 1
xinput --set-prop "ASUE140D:00 04F3:31BC Touchpad"  'libinput Accel Speed' 0.5
