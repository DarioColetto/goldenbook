from tkinter import Frame, Label
from .Button import Button_
from servicies.assets_service import main_icon, cross_icon, minimaze_icon 


class TitleBar:
    
    def __init__(self, parent, win_title:str):
        self.parent= parent
        self.title=win_title
            
        self.frame = Frame(self.parent, bg="grey15", relief="raised", bd=0, height=25) 
        self.frame.pack(fill="x", side='top')
        
        # Bind the titlebar
        self.frame.bind("<Button-1>", self.startMove)
        self.frame.bind("<ButtonRelease-1>", self.stopMove)
        self.frame.bind("<B1-Motion>", self.moving)
        
        
        # Create title text and ICon
        
        self.title_label_icon = main_icon()
        self.title_label = Label(self.frame, image = self.title_label_icon , bg="grey15", fg="white" ,compound='left')
        self.title_label.pack(side='left')

        self.title_label = Label(self.frame, text=self.title, bg="grey15", fg="white")
        self.title_label.pack(side='left', padx=10)

        # Create close button on titlebar

        self.close_button_icon = cross_icon()
        self.close_button=Button_(self.frame, image= self.close_button_icon , bg_color="grey15", width=20, height=25 ,relief="raised", bd=0,command=self.frame.quit)
        self.close_button.pack(side='right', pady=4)

        self.minimize_button_icon = minimaze_icon()
        self.minimize_button=Button_(self.frame, image= self.minimize_button_icon , bg_color="grey15", width=20, height=25 ,relief="raised", bd=0 , command= self.minimize)
        self.minimize_button.pack(side='right', pady=4)
    
    def startMove(self,event):
        self.x = event.x
        self.y = event.y

    def stopMove(self,event):
        self.x = None
        self.y = None

    def moving(self,event): 
        x = (event.x_root - self.x)
        y = (event.y_root - self.y)
        self.parent.geometry("+%s+%s" % (x, y))

    def quitter(self,e):
        self.parent.quit()


    def minimize(self, *arg):
        pass
    
 

