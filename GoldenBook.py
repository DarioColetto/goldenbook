from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image   # Modulo para abrir y editar imagenes. "pip install Pillow"
import sqlite3


conexion=sqlite3.connect("Agenda.db")
cursor=conexion.cursor()
query=cursor.execute("""CREATE TABLE IF NOT EXISTS contactos (
                                id integer primary key autoincrement,
                                nombre text,
                                tel integer,
                                mail text)
                             """)
conexion.commit()                             
conexion.close()  

class Agenda:
    def __init__(self):
        
        self.win=Tk() #------SE Resetean los atributos del Tk y hay que volverlos a crear para poder cambiar la barra de menu----###
        self.win.overrideredirect(True)
        #Window Geometry (x,y)
        self.window_width, window_height = 550, 500
        #Saca el valor las dimensiones y las divide para obtener las coordenadas del centro de la pantalla
        self.screen_width,screen_height = self.win.winfo_screenwidth(), self.win.winfo_screenheight()
        x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.win.geometry(f"{self.window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # remove title bar
        self.win.config(background='DarkGoldenrod2' , highlightthickness=4, highlightbackground="grey15", highlightcolor="grey15"), 
        self.win.resizable(True, True)
        self.win.minsize(550,370)
        
 
        # Create Fake Title Bar
        self.title_bar = Frame(self.win, bg="grey15", relief="raised", bd=0, height=25)  #grey15, DarkGoldenrod2  blanco perla #EFEFEF
        self.title_bar.pack(fill=X, side='top')
        
        # Bind the titlebar
        self.title_bar.bind("<Button-1>", self.startMove)
        self.title_bar.bind("<ButtonRelease-1>", self.stopMove)
        self.title_bar.bind("<B1-Motion>", self.moving)
        
        
        # Create title text and ICon
        self.mainIcon = ImageTk.PhotoImage(Image.open("icons/MainIcon.png").resize((35,35)))
        self.title_label = Label(self.title_bar, image=self.mainIcon, bg="grey15", fg="white" ,compound='left')
        self.title_label.pack(side=LEFT)

        self.title_label = Label(self.title_bar, text="GoldenBook", bg="grey15", fg="white")
        self.title_label.pack(side=LEFT, padx=10)

        # Create close button on titlebar
        self.closeBtnImage =ImageTk.PhotoImage(Image.open("icons/cross.png").resize((15,15)))
        self.close_Button=Button(self.title_bar, image=self.closeBtnImage, bg="grey15", width=20, height=25 ,relief="raised", bd=0,command=self.win.quit)
        self.close_Button.pack(side=RIGHT, pady=4)
        self.close_Button.bind("<Enter>", self.on_enter)    #Cambia el color del boton de cerrar cuando el mouse pasa por encima
        self.close_Button.bind("<Leave>", self.on_leave)
        #----------
        self.contTop=Frame(self.win, background="darkgoldenrod2")
        self.contTop.pack(side=TOP, fill="both",  pady=5)   #anchor must be n, ne, e, se, s, sw, w, nw, or center
        
        self.searchIcon = ImageTk.PhotoImage(Image.open("icons/busqueda.png").resize((15,15))) #Abre la imagen y la redimensiona
        self.buscarLabelImg=Label(self.contTop,width=20,background="darkgoldenrod2",image=self.searchIcon ) #"Guarda la imagen dentro de una Label"
        self.buscarLabelImg.pack(side='left')

        self.string_listener = StringVar()  #Cree los botones y una funcion para validar si hay texto een la entrada y cambie de estado.
        
        self.string_listener.trace("w", self.text_changed)  #esta funcion no lleva (), sino tira el error 'TypeError: 'NoneType' object is not callable'
                                                            #el "trace", es quien hace el seguimiento..
        self.txtBuscar=Entry(self.contTop, textvariable = self.string_listener , fg='grey20' )
        self.txtBuscar.pack(side='left')
        self.txtBuscar.focus()
        
        self.addIcon = ImageTk.PhotoImage(Image.open("icons/agregarusuarios.png").resize((15,15)))
        self.btnAgregar=Button(self.contTop,image= self.addIcon,background="darkgoldenrod2", padx=10, text="Add",compound="left", width=35 ,command= self.addContactWindow)
        self.btnAgregar.pack(side='left')
        self.btnAgregar.bind("<Enter>", self.on_enter1)
        self.btnAgregar.bind("<Leave>", self.on_leave1)

        self.editIcon = ImageTk.PhotoImage(Image.open("icons/editar.png").resize((15,15)))
        self.btnEditar=Button(self.contTop,text="Edit",background="darkgoldenrod2", padx=10, image=self.editIcon, compound="left" , width=35,state="disable", command=self.editBtn)
        self.btnEditar.pack(side='left')
        self.btnEditar.bind("<Enter>", self.on_enter2)
        self.btnEditar.bind("<Leave>", self.on_leave2)
        
        self.deleteIcon = ImageTk.PhotoImage(Image.open("icons/basura.png").resize((15,15)))
        self.btndelete=Button(self.contTop,text="Del",background="darkgoldenrod2", padx=10, image=self.deleteIcon, compound="left" , width=35,state="disable", command=self.deleteWin)
        self.btndelete.pack(side='left')
        self.btndelete.bind("<Enter>", self.on_enter3)
        self.btndelete.bind("<Leave>", self.on_leave3)
        
        
        #------------
        self.frame1=LabelFrame(self.win, text="CONTACTOS", labelanchor="nw", padx=5, pady=5,background="darkgoldenrod2") 
        self.frame1.pack(anchor="w", fill="both", expand=True, padx=5, pady=5)
        
        idcol=['#1','#2','#3', '#4']
        namecol=["ID","Nombre","Teléfono","Email"]
        self.view=ttk.Treeview(self.frame1,columns=idcol ,show="headings", selectmode='browse' )
        self.view.pack(side='left', fill='both', expand=True)

        #Configura el estilo de los widgets ttk..un quilombo!
        style=ttk.Style()
        style.theme_use('alt')
        style.configure("Vertical.TScrollbar",troughcolor="grey15",background='darkgoldenrod2',  bordercolor="grey", arrowcolor="grey15", foreground="darkgoldenrod2")
        style.configure("arrowless.Vertical.TScrollbar", troughcolor="darkgoldenrod2")
        style.map('Vertical.TScrollbar',background=[( 'disabled', 'darkgoldenrod2'), ('active', 'darkgoldenrod2')])
        
        style.configure("Treeview.Heading", background="darkgoldenrod1", foreground="black")
        style.map("Treeview.Heading", background=[('!disabled','darkgoldenrod2'), ('active','#darkgoldenrod2')] )
        style.map('Treeview', background=[( 'selected', 'goldenrod1')],  foreground=[('!disabled','black')])

        self.tv1eScrollBar =ttk.Scrollbar(self.frame1,orient="vertical",command=self.view.yview)
        self.tv1eScrollBar.pack(side='left', fill='y')
        self.view.configure(yscrollcommand=self.tv1eScrollBar.set)  
        
        self.view.bind('<ButtonRelease-1>', self.cambiaEditar) #Cambia el estado de los botones Edit y Delet
       
        for i in range(len(idcol)):
            self.view.heading(idcol[i], text=namecol[i])
            self.view.column(idcol[i] ,width=160, stretch=True)
        
        self.loadData()

        self.view.config(displaycolumns=['#2','#3', '#4']) #Para que solo muestre las columnas indicadas
        

        self.style=ttk.Style().configure("TSizegrip", relief="flat",background="darkgoldenrod2")
        self.sg = ttk.Sizegrip(self.win, style=self.style)
        
        
        self.sg.pack(side="right" ,anchor='se')

    def startMove(self,event):
        self.x = event.x
        self.y = event.y

    def stopMove(self,event):
        self.x = None
        self.y = None

    def moving(self,event): #Mueve la ventana
        x = (event.x_root - self.x)
        y = (event.y_root - self.y)
        self.win.geometry("+%s+%s" % (x, y))

    def quitter(self,e): #root.destroy()
        self.win.quit()

    def on_enter(self,*arg):
        self.close_Button['background'] = 'white'
    def on_leave(self, *arg):
        self.close_Button['background'] = 'grey15'   
    def on_enter1(self,*arg):
        self.btnAgregar['background'] = 'white'
    def on_leave1(self, *arg):
        self.btnAgregar['background'] = 'darkgoldenrod2'   
    def on_enter2(self,*arg):
        self.btnEditar['background'] = 'white'
    def on_leave2(self, *arg):
        self.btnEditar['background'] = 'darkgoldenrod2'   
    def on_enter3(self,*arg):
        self.btndelete['background'] = 'white'
    def on_leave3(self, *arg):
        self.btndelete['background'] = 'darkgoldenrod2'   
	        
    def cambiaEditar(self, *arg):
        self.btnEditar.config(state="normal")
        self.btndelete.config(state="normal")
        
    def selectItem(self, *arg):
        datos=self.view.item(self.view.focus()) # VERR, puede servir para indicar la seleccion
        return  datos

    def text_changed(self,*args): #Lee si la longitud del Entry es 0
        long=len(self.txtBuscar.get())
        
        if long>0:
            self.buscar()
            self.txtBuscar.config(fg="black")
        else:
            self.txtBuscar.config(fg="grey")
            self.refreshView()

    
    def loadData(self):
        conexion=sqlite3.connect("Agenda.db")
        cursor=conexion.cursor()
        query=cursor.execute("SELECT id, nombre, tel, mail FROM contactos ORDER BY nombre ASC")
        rows= query.fetchall() #Devuelve Tuplas con los datos (id, nombre, tel, mail) 
        conexion.close()   
        for row in rows:
            self.view.insert("", "end", text=row[1], values= row)

        return rows             
    
    def refreshView(self):
        for e in self.view.get_children():
            self.view.delete(e)
        
        self.loadData()       

    def buscar(self):    
        
        for e in self.view.get_children():
            self.view.delete(e)

        cosa=f"{self.txtBuscar.get()}%"
        conexion=sqlite3.connect("Agenda.db")
        cur=conexion.cursor()
        query=cur.execute("SELECT * FROM contactos WHERE nombre LIKE ? OR tel LIKE ? OR mail LIKE ? ",(cosa,cosa,cosa)) #
        conexion.commit()
        rows= query.fetchall()
        conexion.close()   
        #print(nombre)
        
        for row in rows:
            self.view.insert("", "end", values=row)
        
    def addContactWindow(self):
        
        self.agregarWin=NewWindow(self.win, "Agregar Contacto") #No se pone pack|ni grid|ni place.
        
            #Nombre
        self.usuarioImg= ImageTk.PhotoImage(Image.open("icons/usuario.png").resize((15,15)))    
        self.agregarWindowlabelNombre=Label(self.agregarWin.Frame,text="Nombre",image=self.usuarioImg, compound='right', padx=5,background='DarkGoldenrod2' )
        self.agregarWindowlabelNombre.grid(column=0, row=0, sticky=E, pady=3 )      
        self.agregarWindowTxtNombre=Entry(self.agregarWin.Frame)
        self.agregarWindowTxtNombre.insert(0, "")
        self.agregarWindowTxtNombre.grid(column=1, row=0)
        self.agregarWindowTxtNombre.focus()
            #Tel
        self.teltImg= ImageTk.PhotoImage(Image.open("icons/telefono.png").resize((15,15)))     
        self.agregarWindowlabelTel=Label(self.agregarWin.Frame, text="Tel",image=self.teltImg, background="darkgoldenrod2",  compound='right' ,padx=5)
        self.agregarWindowlabelTel.grid(column=0, row=1,pady=3, sticky=E)
        self.agregarWindowTxtTel=Entry(self.agregarWin.Frame, )
        self.agregarWindowTxtTel.insert(0, "")
        self.agregarWindowTxtTel.grid(column=1, row=1,  )
            #Mail
        self.mailtImg= ImageTk.PhotoImage(Image.open("icons/sobre.png").resize((15,15)))     
        self.agregarWindowlabelMail=Label(self.agregarWin.Frame,text="Mail",image=self.mailtImg ,background="darkgoldenrod2",compound='right',padx=5)
        self.agregarWindowlabelMail.grid(column=0, row=2, pady=3, sticky=E)
        self.agregarWindowTxtMail=Entry(self.agregarWin.Frame )
        self.agregarWindowTxtMail.insert(0, "")
        self.agregarWindowTxtMail.grid(column=1, row=2,  )
            #Boton Agregar
        self.agregarIcon = ImageTk.PhotoImage(Image.open("icons/agregarusuario.png").resize((15,15)))    
        self.agregarWindowAgregarBtn=Button(self.agregarWin.Frame, width=110 ,text="Add",image=self.agregarIcon ,background="darkgoldenrod2",compound='right',padx=5, command=self.btnAddContacto)
        self.agregarWindowAgregarBtn.grid(column=1, row=3, pady=5 ,sticky=W)
        self.agregarWindowAgregarBtn.bind("<Enter>", self.on_enter8)
        self.agregarWindowAgregarBtn.bind("<Leave>", self.on_leave8)
            #Boton Cerrar
        self.closeIcon = ImageTk.PhotoImage(Image.open("icons/cruzar.png").resize((10,10)))
        self.agregarWindowBtnClose=Button(self.agregarWin, text="Close",image=self.closeIcon, compound='left',background='DarkGoldenrod2',padx=5,   command=self.agregarWin.destroy)
        self.agregarWindowBtnClose.pack(side=BOTTOM,anchor=SE, padx=5, pady=5)# LLamo directamente a la funcion destroy para cerrar ventana
        self.agregarWindowBtnClose.bind("<Enter>", self.on_enter9)
        self.agregarWindowBtnClose.bind("<Leave>", self.on_leave9)

    def on_enter8(self,*arg):
            self.agregarWindowAgregarBtn['background'] = 'white'
    def on_leave8(self, *arg):
            self.agregarWindowAgregarBtn['background'] = 'darkgoldenrod2'   

    def on_enter9(self,*arg):
            self.agregarWindowBtnClose['background'] = 'white'
    def on_leave9(self, *arg):
            self.agregarWindowBtnClose['background'] = 'darkgoldenrod2' 




    def btnAddContacto(self):
        try: #verifica si los widgets ya existen. En caso de que si, los destruye. 
            self.msjValidacion.destroy()
            self.msjAgregado.destroy()
        except AttributeError:   #Simplemente ignora el error en caso de que no existan.       
            pass
        finally:    #Ejecuta el codigo...
            nombre=self.agregarWindowTxtNombre.get()
            tel=self.agregarWindowTxtTel.get() #  el campo tel esta saliendo como string..
            mail=self.agregarWindowTxtMail.get()    

            if len(nombre)>0 and len(tel)>0 and len(mail)>0:  # Hace una verficacion para que los campos no esten vacios
                conexion=sqlite3.connect("Agenda.db")
                cur=conexion.cursor()

                cur.execute("INSERT INTO contactos(nombre, tel, mail) VALUES(?,?,?)",(nombre,tel,mail)) #
                conexion.commit()
                conexion.close()
                

                self.msjAgregado=Label(self.agregarWin, text=f"{nombre} agregado", background='DarkGoldenrod2' )
                self.msjAgregado.pack(anchor="center")

                self.agregarWindowTxtNombre.delete(0, "end")
                self.agregarWindowTxtTel.delete(0, "end")
                self.agregarWindowTxtMail.delete(0, "end")

                self.agregarWindowTxtNombre.focus()

                self.refreshView()
            else:  # Si los vampos estan vacios, levanta la notificacion 'msjError'
                try:
                    self.msjAgregado.destroy()
                except AttributeError:    
                    self.msjError() 
                else:
                    self.msjError()    

            
    def msjError(self):             
        self.msjValidacion=Label(self.agregarWin, text=f"Se deben rellenar los campos", pady=5,background="darkgoldenrod2",font=("Times New Roman", 10), justify='center' )
        self.msjValidacion.pack(side=BOTTOM,  padx=5, pady=5)
        
    def editBtn(self):
        
        self.editwin=NewWindow(self.win, "Editar Contacto")

        #     #Datos
        datos=self.view.item(self.view.selection())    
        self.idedit=datos["values"][0]    
        self.nombreedit=datos["values"][1]
        self.teledit=str(datos["values"][2])
        self.mailedit=datos["values"][3]

            #Nombre
        self.contactImg= ImageTk.PhotoImage(Image.open("icons/usuario.png").resize((15,15)))    
        self.editWindowlabelNombre=Label(self.editwin.Frame ,text="Name",image=self.contactImg,background="darkgoldenrod2", compound='right', padx=5 )
        self.editWindowlabelNombre.grid(column=0, row=0, pady=3, sticky=E)      
        self.editWindowTxtNombre=Entry(self.editwin.Frame )
        self.editWindowTxtNombre.insert(0, self.nombreedit)
        self.editWindowTxtNombre.grid(column=1, row=0)
        self.editWindowTxtNombre.focus()
        
        
            #Tel
        self.teltImg= ImageTk.PhotoImage(Image.open("icons/telefono.png").resize((15,15))) 
        self.editWindowlabelTel=Label(self.editwin.Frame , text="Tel",image=self.teltImg, background="darkgoldenrod2",  compound='right' ,padx=5 )
        self.editWindowlabelTel.grid(column=0, row=1,pady=3, sticky=E)
        self.editWindowTxtTel=Entry(self.editwin.Frame  )
        self.editWindowTxtTel.insert(0, self.teledit)
        self.editWindowTxtTel.grid(column=1, row=1)
     
            #Mail
        self.mailtImg= ImageTk.PhotoImage(Image.open("icons/sobre.png").resize((15,15))) 
        self.editWindowlabelMail=Label(self.editwin.Frame , text="Mail",image=self.mailtImg ,background="darkgoldenrod2",compound='right',padx=5 )
        self.editWindowlabelMail.grid(column=0, row=2, pady=3, sticky=E)
        self.editWindowTxtMail=Entry(self.editwin.Frame  )
        self.editWindowTxtMail.insert(0, self.mailedit)
        self.editWindowTxtMail.grid(column=1, row=2)
       
            #Boton Save
        self.saveIcon = ImageTk.PhotoImage(Image.open("icons/disco.png").resize((15,15)))
        self.editWindowEditBtn=Button(self.editwin.Frame ,width=110 ,text="Save", image= self.saveIcon,compound='left',background="darkgoldenrod2",padx=5 ,command=self.saveData)
        self.editWindowEditBtn.grid(column=1, row=3,pady=5, sticky=W)
        self.editWindowEditBtn.bind("<Enter>", self.on_enter6)
        self.editWindowEditBtn.bind("<Leave>", self.on_leave6)
            #Boton Cerrar
        
        self.closeIcon = ImageTk.PhotoImage(Image.open("icons/cruzar.png").resize((10,10)))
        self.editWindowBtnClose=Button(self.editwin, text="Close",image=self.closeIcon, compound='left',background='DarkGoldenrod2',padx=5,  command=self.editwin.destroy )
        self.editWindowBtnClose.pack(side=BOTTOM,anchor=SE, padx=5, pady=5) 
        self.editWindowBtnClose.bind("<Enter>", self.on_enter7)
        self.editWindowBtnClose.bind("<Leave>", self.on_leave7)



    def on_enter6(self,*arg):
            self.editWindowEditBtn['background'] = 'white'
    def on_leave6(self, *arg):
            self.editWindowEditBtn['background'] = 'darkgoldenrod2'   

    def on_enter7(self,*arg):
            self.editWindowBtnClose['background'] = 'white'
    def on_leave7(self, *arg):
            self.editWindowBtnClose['background'] = 'darkgoldenrod2' 
        
    def saveData(self):
        
        datos=self.view.item(self.view.selection())    
        self.idedit=datos["values"][0] 
        newName=self.editWindowTxtNombre.get()
        newTel=int(self.editWindowTxtTel.get())
        newMail=self.editWindowTxtMail.get()

        conexion=sqlite3.connect("Agenda.db")
        cursor=conexion.cursor()
        cursor.execute("UPDATE contactos SET nombre=?,tel=?, mail=? WHERE id =?",(newName, newTel, newMail, self.idedit))
        conexion.commit()
        conexion.close()
        
        self.refreshView()
        

        #algoritmo de REENFOCAR
        child_id=[x for x in self.view.get_children()] #Da todos los Id Ej.. ['I012', 'I013', 'I014', 'I015', 'I016', 'I017'...]
        items=[self.view.item(i) for i in child_id] #Da todos los items que tiene el child_ID
        
        for x in range(len(child_id)):
            if items[x]["values"][0]==self.idedit:
                self.view.focus(child_id[x])   
                self.view.selection_set(child_id[x])
                break
                

        self.editwin.destroy()
                
                    

    def deleteWin(self):
        
        self.deletewin=NewWindow(self.win, "Eliminar Contacto")
        #self.deletewin.geometry("250x150")
        
        nombre=self.view.item(self.view.selection())["values"][1]
        
        self.avisolIcon = ImageTk.PhotoImage(Image.open("icons/exclamacion.png").resize((30,30)))
        self.deleteLabel=Label(self.deletewin,image=self.avisolIcon, background='DarkGoldenrod2' ,padx=5 ,compound="left",  text=f"    Desea ELIMINAR a\n {nombre} ", justify='center')
        self.deleteLabel.pack(anchor="center")
       
        self.okeylIcon = ImageTk.PhotoImage(Image.open("icons/controlar.png").resize((15,15)))
        self.okeyBtn=Button(self.deletewin,width=35, height=20 ,image=self.okeylIcon,background='DarkGoldenrod2',pady=5, padx=5 , command=self.deletecontact)
        self.okeyBtn.pack(side=LEFT, padx=30 )
        self.okeyBtn.bind("<Enter>", self.on_enter4)
        self.okeyBtn.bind("<Leave>", self.on_leave4)
        
        self.cancelIcon = ImageTk.PhotoImage(Image.open("icons/cruzar.png").resize((15,15)))
        self.cancelButton=Button(self.deletewin,width=35 , height=20 , image=self.cancelIcon, background='DarkGoldenrod2',pady=5, padx=5 ,command=self.deletewin.destroy)
        self.cancelButton.pack(side=RIGHT, padx=30 )
        self.cancelButton.bind("<Enter>", self.on_enter5)
        self.cancelButton.bind("<Leave>", self.on_leave5)
        
    def on_enter4(self,*arg):
            self.okeyBtn['background'] = 'white'
    def on_leave4(self, *arg):
            self.okeyBtn['background'] = 'darkgoldenrod2'   

    def on_enter5(self,*arg):
            self.cancelButton['background'] = 'white'
    def on_leave5(self, *arg):
            self.cancelButton['background'] = 'darkgoldenrod2'        

    def deletecontact(self):
        self.idedit=self.selectItem()["values"][0]
        conexion=sqlite3.connect("Agenda.db")
        cursor=conexion.cursor()
        cursor.execute("DELETE FROM contactos WHERE id =?",(self.idedit,))
        conexion.commit()
        conexion.close()
        self.deletewin.destroy()
        self.refreshView() 

class NewWindow(Toplevel):
        def __init__(self, master,wintilte, *arg, **kwargs):
            super().__init__(master,*arg, **kwargs)
            #self.newwin=Toplevel(master)#No se pone pack|ni grid|ni place.
            
            #Window Geometry (x,y)
            window_width,window_height=  250,250
            #Saca el valor las dimensiones y las divide para obtener las coordenadas del centro de la pantalla
            screen_width,screen_height = master.winfo_screenwidth(), master.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            
            self.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")
            self.overrideredirect(True)# remove title bar
            self.config(background='DarkGoldenrod2', highlightthickness=4, highlightbackground="grey15", highlightcolor="grey15")
                    # Create Fake Title Bar
            self.title_bar = Frame(self, height=25,  background="grey15")  #grey15, DarkGoldenrod2  blanco perla #EFEFEF
            self.title_bar.pack(fill=BOTH )
                    
                    # Create title text and ICon
            self.mainIcon = ImageTk.PhotoImage(Image.open("icons/MainIcon.png").resize((30,30)))
            self.title_label = Label(self.title_bar, image=self.mainIcon, bg="grey15", fg="white" ,compound='left')
            self.title_label.pack(side=LEFT)

            self.title_label = Label(self.title_bar, text=wintilte, bg="grey15", fg="white")
            self.title_label.pack(side=LEFT, padx=10)

            self.Frame=Frame(self, background="darkgoldenrod2")
            self.Frame.pack(fill="both", padx=5, pady=20 )           

App=Agenda()
App.win.mainloop()

 