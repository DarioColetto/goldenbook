from tkinter import IntVar, LabelFrame, StringVar, Tk
from tkinter.ttk import Sizegrip
from ..widgets.tree_view import TreeView

from ..widgets.widgets_conteiner import WidgetFrame

from ..widgets.title_bar import TitleBar
from .config_geometry import config_geometry

from components.comm import common


class MainWindow(Tk):
    
    
    def __init__(self):
        super().__init__()
        
        self.overrideredirect(True) 
        
        self.geometry(config_geometry(self, 550, 500))
        
        self.config(background='DarkGoldenrod2', highlightthickness=4,
                    highlightbackground="grey15", highlightcolor="grey15"),
        self.resizable(True, True)
        self.minsize(550, 370)



        common.string_listener = StringVar()
        common.added = StringVar() 
        common.id_ = IntVar() 



        self.title_bar = TitleBar(self, "GoldenBook")
        
        self.widet_frame=WidgetFrame(self)

        self.tree_frame=LabelFrame(self, text="CONTACTOS", labelanchor="nw", padx=5, pady=5,background="darkgoldenrod2") 
        self.tree_frame.pack(anchor="w", fill="both", expand=True, padx=5, pady=5)

        self.sizegrip = Sizegrip(self.tree_frame)
        self.sizegrip.pack(side='bottom', anchor='se')

        self.tree=TreeView(self.tree_frame)
         


