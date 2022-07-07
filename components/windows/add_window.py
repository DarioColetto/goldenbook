from tkinter import Entry, Frame, Label

from servicies.repository import Repository
from .new_window import NewWindow
from components.widgets.Button import Button_
from servicies.assets_service import contact_icon, telephone_icon, mail_icon, add_icon, close_icon
from components.comm import common

class AddWindow(NewWindow):

    def __init__(self, master):

        
        super().__init__(master, "Agregar Contacto")

        self.frame=Frame(self, background="darkgoldenrod2")
        self.frame.pack(fill="both", padx=5, pady=20 )

        #Nombre
        self.label_nombre_icon=contact_icon()
        self.label_nombre=Label(self.frame, text="Nombre",image= self.label_nombre_icon, compound='right', padx=5,background='DarkGoldenrod2' )
        self.label_nombre.grid(column=0, row=0, sticky='e', pady=3 )      
        
        self.entry_nombre=Entry(self.frame)
        self.entry_nombre.insert(0, "")
        self.entry_nombre.grid(column=1, row=0)
        self.entry_nombre.focus()
            #Tel

        self.label_tel_icon = telephone_icon()
        self.label_tel=Label(self.frame, text="Tel",image= self.label_tel_icon, background="darkgoldenrod2",  compound='right' ,padx=5)
        self.label_tel.grid(column=0, row=1,pady=3, sticky='e')
        
        self.entry_tel=Entry(self.frame)
        self.entry_tel.insert(0, "")
        self.entry_tel.grid(column=1, row=1,  )
            #Mail
        self.label_mail_icon= mail_icon()   
        self.label_mail=Label(self.frame,text="Mail",image=self.label_mail_icon ,background="darkgoldenrod2",compound='right',padx=5)
        self.label_mail.grid(column=0, row=2, pady=3, sticky='e')
        
        self.entry_mail=Entry(self.frame )
        self.entry_mail.insert(0, "")
        self.entry_mail.grid(column=1, row=2,  )
           
            #Boton Agregar
        self.add_btn_icon = add_icon()
        self.add_btn=Button_(self.frame, width=110 , text="Add",image = self.add_btn_icon , bg_color="darkgoldenrod2", compound='right',padx=5, command=self.add_)
        self.add_btn.grid(column=0, row=3, pady=5)

            #Boton Cerrar
        self.close_btn_icon = close_icon()
        self.close_btn=Button_(self.frame, width=110, text="Close", image = self.close_btn_icon, compound='left',bg_color='DarkGoldenrod2',padx=5, command=self.destroy)
        self.close_btn.grid(column=1, row=3, pady=5)
  

    def add_(self):
        try: #verifica si los widgets ya existen. En caso de que si, los destruye. 
            self.validation_msj.destroy()
            self.added_msj.destroy()
        except AttributeError:   # Ignora el error en caso que no existan.       
            pass
        
        finally:    #Ejecuta el codigo...
            
            nombre=self.entry_nombre.get()
            tel=self.entry_tel.get() #  el campo tel esta saliendo como string..
            mail=self.entry_mail.get()    

            if len(nombre)>0 and len(tel)>0 and len(mail)>0:  # Verifica que los campos no esten vacios
                
                Repository().add_contact(nombre, tel, mail)
                
                
                self.added_msj=Label(self, text=f"{nombre} agregado", background='DarkGoldenrod2' )
                self.added_msj.pack(anchor="center")
                
                common.added.set(nombre) 

                #Clean Entries
                self.entry_nombre.delete(0, "end")
                self.entry_tel.delete(0, "end")
                self.entry_mail.delete(0, "end")

                self.entry_nombre.focus()

                
           
           
            else:  # Si los campos estan vacios, levanta la notificacion 'msjError'
                try:
                    self.added_msj.destroy()
                except AttributeError: 
                       
                    self.msjError() 
                else:
                    
                    self.msjError()    

            
    def msjError(self):             
        self.validation_msj=Label(self, text=f"Se deben rellenar los campos", pady=5,background="darkgoldenrod2",font=("Times New Roman", 10), justify='center' )
        self.validation_msj.pack(side='bottom',  padx=5, pady=5)