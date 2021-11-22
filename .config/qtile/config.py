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
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.log_utils import logger

mod = "mod4"
terminal = "alacritty"
rofi = "rofi -show run"

Color = {
    "grey": "#293241",
    "red": "#EE6C4D",
    "light_blue": "#E0FBFC",
    "blue": "#98C1D9",
    "dark_blue": "#3D5A80",
}

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
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    # Spawn
    Key([mod], "space", lazy.spawn(rofi), desc="Spawn a command using a prompt widget"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.spawn("alacritty -e tmux new"),
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
]

# Clamp groups to specified screen. qtile.warp_to_screen() gets called manually so the mouse cursor follows the focus even when a window is present.
# One could set the global option "cursor_warp" to true, but Steam doesn't like that. Every menu press will set the cursor back to the center.
def go_to_group(qtile, group_name, screen):
    qtile.focus_screen(screen)
    qtile.groups_map[group_name].cmd_toscreen(toggle=False)
    qtile.warp_to_screen()

workspaces = [
    {'name': '1'},
    {'name': '2'},
    {'name': '3', 'spawn': 'spotify', 'matches': [Match(wm_class='spotify')]},
    {'name': '4'},
    {'name': '5'},
    {'name': '6'},
    {'name': '7'},
    {'name': '8'},
    {'name': '9'},
    {'name': '0', 'screen': 1}
]

groups = []
for workspace in workspaces:
    matches = workspace['matches'] if 'matches' in workspace else None
    screen = workspace['screen'] if 'screen' in workspace else 0
    spawn = workspace['spawn'] if 'spawn' in workspace else None
    key = workspace['name']
    # screen_affinity sounds like specifying a screen but doesn't work
    groups.append(Group(workspace['name'], matches=matches, spawn=spawn, screen_affinity=screen))
    keys.append(Key([mod], key, lazy.function(go_to_group, workspace['name'], screen)))
    keys.append(Key([mod, 'shift'], key, lazy.window.togroup(workspace['name'])))

layouts = [
    layout.Max(),
    layout.MonadTall(
        margin=15, border_width=0, border_focus="#bc7cf7", border_normal="#4c566a"
    ),
]

widget_defaults = dict(
    font="Lato-Regular", fontsize=12, padding=3, foreground=Color["light_blue"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(
                    active=Color["light_blue"],
                    highlight_method="text",
                    this_current_screen_border=Color["red"],
                    font="Lato-Regular",
                    hide_unused=True,
                    disable_drag=True,
                ),
                widget.Spacer(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %H:%M"),
            ],
            24,
            background=Color["grey"],
        ),
    ),
    Screen(),
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
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

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
