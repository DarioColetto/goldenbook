from tkinter import Button

class Button_(Button):
    def __init__(self, master, bg_color , *args, **kwargs):
        self.bg_color = bg_color
        
        super().__init__(master, bg= bg_color, *args, **kwargs)
            
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)


    def on_enter(self,*arg):
        self['background'] = 'white'
    
    def on_leave(self, *arg):
        self['background'] = self.bg_color