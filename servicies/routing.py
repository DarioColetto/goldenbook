from components.windows.update_window import UpdateWindow
from components.windows.delete_window import DeleteWindow
from components.windows.add_window import AddWindow


class Routing:

    def to_add_window(master):
        return AddWindow(master)

    def to_update_window(master):
        return UpdateWindow(master)    

    def to_delete_window(master):
        return DeleteWindow(master) 