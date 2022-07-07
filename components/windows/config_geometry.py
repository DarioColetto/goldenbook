def config_geometry(self,window_width,window_height ) -> str:
    """Obtiene las dimenciones de la pantalla y devuelve las coordenadas del centro de la pantalla"""
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
        
    return f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}"