from tkinter.ttk import Style 
 
        #Configura el estilo de los widgets ttk...
class TreeViewStyle(Style):

    def __init__(self, master):
        super().__init__(master)
        

        self.theme_use('alt')
        
        self.configure("Vertical.TScrollbar",troughcolor="grey15",background='darkgoldenrod2',  bordercolor="grey", arrowcolor="grey15", foreground="darkgoldenrod2")
        self.configure("arrowless.Vertical.TScrollbar", troughcolor="darkgoldenrod2")
        self.map('Vertical.TScrollbar',background=[( 'disabled', 'darkgoldenrod2'), ('active', 'darkgoldenrod2')])
        
        self.configure("Treeview.Heading", background="darkgoldenrod1", foreground="black")
        self.map("Treeview.Heading", background=[('!disabled','darkgoldenrod2'), ('active','#darkgoldenrod2')] )
        self.map('Treeview', background=[( 'selected', 'goldenrod1')],  foreground=[('!disabled','black')])

        self.configure("TSizegrip", relief="flat",background="darkgoldenrod2")