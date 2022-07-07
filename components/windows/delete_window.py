from tkinter import Label
from components.widgets.Button import Button_
from .new_window import NewWindow
from servicies.repository import Repository
from servicies.assets_service import warning_icon, check_icon, close_icon
from components.comm import common


class DeleteWindow(NewWindow): 
        
        def __init__(self, master):
                super().__init__(master, "Eliminar Contacto")
                
                
                self.id = common.id_ 
                datos = Repository().get_by_id(self.id )       
        
                self.delete_label_icon=warning_icon()
                self.delete_label=Label(self,image = self.delete_label_icon, background='DarkGoldenrod2' ,padx=5 ,compound="left", justify='center', text=f"    Desea ELIMINAR a\n {datos[1]} ") 
                self.delete_label.pack(anchor="center")
        
                self.okey_btn_icon = check_icon()
                self.okey_btn = Button_(self,width=35, height=20 ,image=self.okey_btn_icon, bg_color='DarkGoldenrod2',pady=5, padx=5 , command=self.delete_contact)
                self.okey_btn.pack(side='left', padx=30 )

                self.cancel_btn_icon = close_icon()
                self.cancel_btn=Button_(self,width=35 , height=20 , image = self.cancel_btn_icon, bg_color='DarkGoldenrod2',pady=5, padx=5 ,command=self.destroy)
                self.cancel_btn.pack(side='right', padx=30 )

        def delete_contact(self):
                
                Repository().delete_by_id(self.id)
                common.string_listener.set('')
                self.destroy()

               
 