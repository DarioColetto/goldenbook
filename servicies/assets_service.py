# from tkinter import Label, Tk
from PIL.ImageTk import PhotoImage
from PIL import Image


class Imagen(object):

    """Returns a PhotoImage object when self is called.
    It can be used iside tk scope for any widget that requires an image.
    Ej: my_icon(),"""
      
    def __init__(self, path, size):
        self. path = path
        self.size = size

    def __call__(self):
        img = Image.open(self.path).resize(self.size) 
        return PhotoImage(img)  
        


main_icon = Imagen("assets/MainIcon.png", (35,35)) 
search_icon =  Imagen("assets/busqueda.png" , (15,15))
add_icon = Imagen("assets/agregarusuarios.png",(15,15))
update_icon = Imagen("assets/editar.png", (15,15))
save_icon = Imagen("assets/disco.png" , (15,15)) 
delete_icon = Imagen("assets/basura.png" , (15,15)) 
contact_icon= Imagen("assets/usuario.png" , (15,15))
telephone_icon= Imagen("assets/telefono.png" , (15,15)) 
mail_icon= Imagen("assets/sobre.png" , (15,15)) 
close_icon = Imagen("assets/cruzar.png", (10,10))
minimaze_icon = Imagen("assets/minimize.png", (10,10))
cross_icon =Imagen("assets/cross.png" , (15,15)) 
warning_icon = Imagen("assets/exclamacion.png", (30,30))  
check_icon = Imagen("assets/controlar.png" , (15,15))


  


