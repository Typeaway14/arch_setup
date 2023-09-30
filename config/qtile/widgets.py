import os
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.config import Screen

from functions import PWA
# widget_defaults = dict(
#     font="Ubuntu Mono",
#     fontsize = 12,
#     padding = 2,
#     background=colors[2]
# )

# extension_defaults = widget_defaults.copy()


class MyWidgets:
    def __init__(self):
        self.colors = [["#292d3e", "#292d3e"],  # panel background
                       # background for current screen tab
                       ["#434758", "#434758"],
                       ["#ffffff", "#ffffff"],  # font color for group names
                       # border line color for current tab
                       ["#bc13fe", "#bc13fe"],  # Group down color
                       # border line color for other tab and odd widgets
                       ["#8d62a9", "#8d62a9"],
                       ["#668bd7", "#668bd7"],  # color for the even widgets
                       ["#e1acff", "#e1acff"],  # window name

                       ["#000000", "#000000"],
                       ["#AD343E", "#AD343E"],
                       ["#f76e5c", "#f76e5c"],
                       ["#F39C12", "#F39C12"],
                       ["#F7DC6F", "#F7DC6F"],
                       ["#f1ffff", "#f1ffff"],
                       ["#4c566a", "#4c566a"], ]

        self.sunset_colors = [["#FFCAA6", "#FFCAA6"],    
                       ["#FEB9A3", "#FEB9A3"],
                       ["#FDA8A0", "#FDA8A0"],  
                       ["#FC989D", "#FC989D"],                          
                       ["#FA879A", "#FA879A"],
                       ["#F97697", "#F97697"],               
                       ["#F86594", "#F86594"], ]

        self.oceanblue_colors = [["#CCEEDE", "#CCEEDE"],    
                       ["#B3E8DC", "#B3E8DC"],
                       ["#99E1D9", "#99E1D9"],  
                       ["#5ABEC2", "#5ABEC2"],                          
                       ["#3BACB6", "#3BACB6"],
                       ["#1B9AAA", "#1B9AAA"],               
                       ["#2F8F9D", "#2F8F9D"], ]

        self.orgblue_colors = [["#F6CFBE", "#F6CFBE"],    
                       ["#ECD1C7", "#ECD1C7"],
                       ["#E2D3CF", "#E2D3CF"],  
                       ["#D8D6D8", "#D8D6D8"],                          
                       ["#CDD8E1", "#CDD8E1"],
                       ["#C3DAE9", "#C3DAE9"],               
                       ["#B9DCF2", "#B9DCF2"], ]

        self.pinblue_colors = [["#F7C0EC", "#F7C0EC"],    
                       ["#EAC0EC", "#EAC0EC"],
                       ["#DCBFEB", "#DCBFEB"],  
                       ["#CFBFEB", "#CFBFEB"],                          
                       ["#C2BEEB", "#C2BEEB"],
                       ["#B4BEEA", "#B4BEEA"],               
                       ["#A7BDEA", "#A7BDEA"], ]

        self.termite = "termite"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.Image(
                filename="~/.config/qtile/icons/halo.png",
                background=self.colors[0],
                mouse_callbacks={
                    'Button1': lambda qtile: qtile.cmd_spawn('dmenu_run -p "Run: "')}
            ),
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font="Noto Nerd",
                fontsize=20,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[-2],
                inactive=self.colors[-1],
                rounded=True,
                # rounded=False,
                # highlight_color=self.colors[9],
                highlight_method="line",
                # highlight_method='block',
                # urgent_alert_method='block',
                urgent_alert_method='line',
                # urgent_border=self.colors[9],
                this_current_screen_border=self.colors[9],
                this_screen_border=self.colors[4],
                other_current_screen_border=self.colors[0],
                other_screen_border=self.colors[0],
                foreground=self.colors[2],
                background=self.colors[0],
                disable_drag=True
            ),
            widget.Prompt(
                prompt=lazy.spawncmd(),
                font="Noto Nerd",
                padding=10,
                foreground=self.colors[3],
                background=self.colors[1]
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.colors[2],
                background=self.colors[0]
            ),
            widget.WindowName(
                fontsize=20,
                foreground=self.colors[6],
                background=self.colors[0],
                padding=0
            ),
            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
            widget.TextBox(
                text='',
                foreground=self.sunset_colors[1],
                background=self.colors[0],
                padding=0,
                fontsize=45
            ),
            widget.TextBox(
                text=" 󰍛 ",
                foreground=self.colors[7],
                padding=0,
                background=self.sunset_colors[1],
                fontsize=25
            ),
            widget.Memory(
                fontsize=20,
                foreground=self.colors[7],
                mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
                    self.termite + ' -e htop')},
                background=self.sunset_colors[1],
                padding=5
            ),
            widget.TextBox(
                text='',
                foreground=self.sunset_colors[2],
                background=self.sunset_colors[1],
                padding=0,
                fontsize=45
            ),
            widget.TextBox(
                fontsize=20,
                text="  ",
                foreground=self.colors[7],
                background=self.sunset_colors[2],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                fontsize=20,
                foreground=self.colors[7],
                background=self.sunset_colors[2],
                padding=5
            ),
            widget.TextBox(
                text='',
                background=self.sunset_colors[2],
                foreground=self.sunset_colors[3],
                padding=0,
                fontsize=45
            ),
            widget.CurrentLayoutIcon(
                fontsize=20,
                custom_icon_paths=[os.path.expanduser(
                    "~/.config/qtile/icons")],
                foreground=self.sunset_colors[1],
                background=self.sunset_colors[2],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                fontsize=20,
                foreground=self.colors[7],
                background=self.sunset_colors[3],
                padding=5
            ),
            widget.TextBox(
                text='',
                foreground=self.sunset_colors[4],
                background=self.sunset_colors[3],
                padding=0,
                fontsize=45
            ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[7],
                padding=0,
                background=self.sunset_colors[4],
                fontsize=25
            ),
            widget.Clock(
                fontsize=20,
                foreground=self.colors[7],
                background=self.sunset_colors[4],
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn(PWA.calendar())},
                format=" %a, %B %d  [ %I:%M %p ]"
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[0],
                background=self.colors[8]
            ),
        ]
        return widgets_list

    def init_widgets_screen(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen = self.init_widgets_list()
        return widgets_screen

    def init_widgets_screen2(self):
        '''
        Function that returns the widgets in a list.
        It can be modified so it is useful if you  have a multimonitor system
        '''
        widgets_screen2 = self.init_widgets_screen()
        return widgets_screen2

    def init_screen(self):
        '''
        Init the widgets in the screen
        '''
        return [Screen(top=bar.Bar(widgets=self.init_widgets_screen(), opacity=1.0, size=30)),
                Screen(top=bar.Bar(
                    widgets=self.init_widgets_screen2(), opacity=1.0, size=20))
                ]
