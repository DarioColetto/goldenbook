from tkinter import Toplevel
from .config_geometry import config_geometry
from ..widgets.title_bar import TitleBar


class NewWindow(Toplevel):
        def __init__(self, master,win_tilte, *arg, **kwargs):
            super().__init__(master,*arg, **kwargs)
            #Toplevel() No usa pack|grid|place.
            
            self.overrideredirect(True)
            self.geometry(config_geometry(self, 250,250))
            self.config(background='DarkGoldenrod2', highlightthickness=4, highlightbackground="grey15", highlightcolor="grey15")      
            
            self.new_title_bar= TitleBar(self,win_tilte)       


