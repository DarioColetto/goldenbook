from tkinter import Entry, Frame, Label
from servicies.assets_service import search_icon, add_icon, update_icon, delete_icon
from servicies.routing import Routing 
from .Button import Button_
from components.comm import common


class WidgetFrame(Frame,Routing ):
    
    
    def __init__(self, parent):
        bg_color="darkgoldenrod2"
        
        super().__init__(parent, background=bg_color )
        
        
        self.pack(side='top', fill="both",  pady=5) 


        self.search_label_icon = search_icon()
        self.search_label=Label(self,width=20,background="darkgoldenrod2", image = self.search_label_icon)
        self.search_label.pack(side='left')

        self.entry_search=Entry(self, textvariable = common.string_listener , fg='grey20' )
        self.entry_search.pack(side='left')
        self.entry_search.focus()
        
        self.add_btn_icon = add_icon()
        self.add_btn=Button_(self,image = self.add_btn_icon ,bg_color="darkgoldenrod2", padx=10, text="Add",compound="left", width=35 ,command = self.to_add_window) 
        self.add_btn.pack(side='left')

        self.update_btn_icon = update_icon()
        self.update_btn=Button_(self,text="Edit", bg_color="darkgoldenrod2", padx=10, image = self.update_btn_icon , compound="left" , width=35, command=self.to_update_window ,state="disable" )
        self.update_btn.pack(side='left')

        self.delete_btn_icon = delete_icon()
        self.delete_btn=Button_(self,text="Del",bg_color="darkgoldenrod2", padx=10, image = self.delete_btn_icon, compound="left" , width=35,command=self.to_delete_window, state="disable")
        self.delete_btn.pack(side='left') 

        #TRACERS

        common.string_listener.trace_add("write", self.text_changed)
        common.id_.trace_add("write" , self.change_btn_state)
    
    def text_changed(self, *args): 
        
        entry_string = self.entry_search.get()
        
        if entry_string:
            common.string_listener.set(entry_string)
            
            

    def change_btn_state(self, *arg):

        if common.id_ != 0:
            self.update_btn.config(state="normal")
            self.delete_btn.config(state="normal")
        # else:
        #     self.update_btn.config(state="disable")
        #     self.delete_btn.config(state="disable")                