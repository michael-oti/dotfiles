#!/bin/sh
ibus-daemon -drxR &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
key-mapper-control --command autoload
