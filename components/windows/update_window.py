from tkinter import Entry, Frame, Label
from .new_window import NewWindow
from components.widgets.Button import Button_
from servicies.repository import Repository
from servicies.assets_service import contact_icon, telephone_icon, mail_icon, save_icon, close_icon
from components.comm import common


class UpdateWindow(NewWindow):


    def __init__(self, master):
        super().__init__(master, "Editar Contactos")
        

        #Datos
        
        datos = Repository().get_by_id(common.id_.get())
        self.id=datos[0]    
        self.current_name=datos[1]
        self.current_tel=str(datos[2])
        self.current_mail=datos[3]

        #Frame
        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=20 )
        

        #Nombre
        self.label_nombre_icon =  contact_icon()
        self.label_nombre=Label(self.frame ,text="Name",image = self.label_nombre_icon, background="darkgoldenrod2", compound='right', padx=5 )
        self.label_nombre.grid(column=0, row=0, pady=3, sticky='e')      
        
        self.entry_nombre=Entry(self.frame )
        self.entry_nombre.insert(0, self.current_name)
        self.entry_nombre.grid(column=1, row=0)
        self.entry_nombre.focus()
        
        
        #Tel
        self.label_tel_icon = telephone_icon()
        self.label_tel=Label(self.frame , image = self.label_tel_icon ,text="Tel", background="darkgoldenrod2",  compound='right' ,padx=5 )
        self.label_tel.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_tel=Entry(self.frame  )
        self.entry_tel.insert(0, self.current_tel)
        self.entry_tel.grid(column=1, row=1)
     
        #Mail
        self.label_mail_icon= mail_icon()
        self.label_mail=Label(self.frame , text="Mail", image = self.label_mail_icon ,background="darkgoldenrod2",compound='right',padx=5 )
        self.label_mail.grid(column=0, row=2, pady=3, sticky='e')
        
        self.entry_mail=Entry(self.frame  )
        self.entry_mail.insert(0, self.current_mail)
        self.entry_mail.grid(column=1, row=2)
       
        #Boton Save
        self.edit_btn_icon = save_icon()
        self.edit_btn=Button_(self.frame ,width=110 ,text="Save", image= self.edit_btn_icon ,compound='left', bg_color="darkgoldenrod2",padx=5 , command=self.save_data)
        self.edit_btn.grid(column=0, row=3,pady=5, sticky='w')

        #Boton Cerrar
        self.close_btn_icon = close_icon()
        self.close_btn=Button_(self.frame, text="Close",image= self.close_btn_icon, compound='left', bg_color='DarkGoldenrod2',padx=5,  command=self.destroy )
        self.close_btn.grid(column=1, row=3, pady=5) 


    def save_data(self):

        
        new_name = self.entry_nombre.get()
        new_tel = int(self.entry_tel.get())
        new_mail = self.entry_mail.get()

        Repository().update(self.id, new_name, new_tel, new_mail)
        
        common.id_.set('')

        self.destroy()


