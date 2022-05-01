# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
import psutil
import random
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.log_utils import logger


mod = "mod4"
terminal = "alacritty"
launcher = "rofi -show run"
wallpaper_folder = "/home/michael/Pictures/backgrounds"

Color = {
    "base000": "#21252C",
    "base00": "#282c34",
    "base01": "#353b45",
    "base02": "#3e4451",
    "base03": "#545862",
    "base04": "#565c64",
    "base05": "#abb2bf",
    "base06": "#b6bdca",
    "base07": "#c8ccd4",
    "light_red": "#e06c75",
    "dark_yellow": "#d19a66",
    "yellow": "#e5c07b",
    "green": "#98c379",
    "cyan": "#56b6c2",
    "blue": "#61afef",
    "violet": "#c678dd",
    "red": "#be5046",
}


def debug_log(qtile):
    pass


def get_wallpaper():
    list_of_wallpapers = os.listdir(wallpaper_folder)
    wallpaper = random.choice(list_of_wallpapers)
    wallpaper = f"{wallpaper_folder}/{wallpaper}"
    return wallpaper


keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "p", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    # Move windows between left/right columns or move up/down in current stack.
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),
    # Switch window focus to other pane(s) of stack
    Key(
        [mod],
        "Tab",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack",
    ),
    # Toggle between different layouts as defined below
    Key([mod], "a", lazy.next_layout(), desc="Toggle between layouts"),
    # Kill window
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    # Restart/Shutdown qtile
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod, "control"], "t", lazy.function(debug_log), desc="Debug logging key"),
    # Key(
    #    [mod, "control"],
    #    "w",
    #    lazy.function(change_wallpaper),
    #    desc="Change Wallpaper"
    # ),
    # Spawn
    Key(
        [mod],
        "space",
        lazy.spawn(launcher),
        desc="Spawn a command using a prompt widget",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("alacritty -e tmux new"),
        # lazy.spawn("alacritty -e tmux new-window -t TMUX: & tmux attach -t TMUX"),
        desc="Launch terminal",
    ),
    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    # Sount Output change
    Key(
        [mod, "control"],
        "a",
        lazy.spawn(
            "/home/michael/scripts/sound-output.sh wireless_headphone",
        ),
        desc="Change sound to wireless headphone",
    ),
    Key(
        [mod, "control"],
        "s",
        lazy.spawn("/home/michael/scripts/sound-output.sh headphone"),
        desc="Change sound to headphone",
    ),
    Key(
        [mod, "control"],
        "d",
        lazy.spawn(
            "/home/michael/scripts/sound-output.sh loudspeaker",
        ),
        desc="Change sound to loudspeaker",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl -p spotify next")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl -p spotify play-pause")),
]

# Clamp groups to specified screen.
def go_to_group(qtile, group_name, screen):
    qtile.focus_screen(screen)
    qtile.groups_map[group_name].cmd_toscreen(toggle=False)


workspaces = [
    {"name": "1"},
    {"name": "2"},
    {"name": "3", "spawn": "spotify", "matches": [Match(wm_class="spotify")]},
    {"name": "4"},
    {"name": "5"},
    {"name": "6"},
    {"name": "7"},
    {"name": "8"},
    {"name": "9"},
    {"name": "0", "screen": 1},
]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    screen = workspace["screen"] if "screen" in workspace else 0
    spawn = workspace["spawn"] if "spawn" in workspace else None
    ws_name = workspace["name"]
    # screen_affinity sounds like specifying a screen but doesn't work
    groups.append(Group(ws_name, matches=matches, spawn=spawn, screen_affinity=screen))
    keys.append(Key([mod], ws_name, lazy.function(go_to_group, ws_name, screen)))
    # keys.append(Key([mod], ws_name, lazy.group[ws_name].toscreen()))
    keys.append(Key([mod, "shift"], ws_name, lazy.window.togroup(ws_name)))


layouts = [
    layout.Max(name=""),
    layout.MonadTall(
        name="",
        margin=15,
        border_width=3,
        border_focus=Color["blue"],
        border_normal=Color["base01"],
    ),
]

widget_defaults = dict(font="Inter", fontsize=14, padding=3, foreground=Color["base07"])
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    fmt="<big>{}</big>",
                    fontsize=24,
                    padding=10,
                ),
                widget.GroupBox(
                    font="Inter",
                    active=Color["base07"],
                    inactive=Color["base07"],
                    highlight_method="block",
                    block_highlight_text_color=Color["base00"],
                    rounded=False,
                    other_screen_border=Color["blue"],
                    other_current_screen_border=Color["blue"],
                    this_current_screen_border=Color["blue"],
                    urgent_alert_method="block",
                    urgent_text=Color["base07"],
                    urgent_border=Color["red"],
                    hide_unused=True,
                    disable_drag=True,
                ),
                widget.Spacer(),
                widget.StatusNotifier(),
                widget.Clock(
                    format="%Y-%m-%d %a %H:%M",
                ),
            ],
            28,
            background=Color["base000"],
        ),
        wallpaper=get_wallpaper(),
        wallpaper_mode="fill",
    ),
    Screen(wallpaper=get_wallpaper(), wallpaper_mode="fill"),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(
            title="Library", wm_class="firefox"
        ),  # Firefox Downloads, History, Bookmark manager window
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    margin=15,
    border_width=3,
    border_focus=Color["blue"],
    border_normal=Color["base01"],
)
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

# TODO: This gets ugly. There is probably a better way to do it.
@hook.subscribe.client_new
def new_client(new_window):
    current_group = qtile.current_group
    if current_group.name == "1" and current_group.windows:
        if (
            "firefox" in current_group.windows[0].get_wm_class()
            and "firefox" in new_window.get_wm_class()
            and new_window.name
            != "Library"  # firefox Downloads/Bookmarks/History manager window
            and new_window.get_wm_role() != "Dialog"
            and new_window.get_wm_role() != "GtkFileChooserDialog"
        ):
            new_window.togroup("0")


# If we don't focus group['0'] at the start, qtile will put group['2'] on the second monitor
# For some reason I can't call my already defined lazy_function above
# needs import:  from libqtile import qtile
@hook.subscribe.startup_complete
def start_finished():
    qtile.focus_screen(1)
    qtile.groups_map["0"].cmd_toscreen(toggle=False)
    qtile.focus_screen(0)
    qtile.groups_map["1"].cmd_toscreen(toggle=False)


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~")
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])
