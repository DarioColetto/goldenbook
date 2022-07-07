import sqlite3


class Repository:
    
    conexion = sqlite3.connect("Agenda.db")
    with conexion:
        cur = conexion.cursor()

    
    def add_contact(self, nombre, tel, mail):

        self.cur.execute(
            "INSERT INTO contactos(nombre, tel, mail) VALUES(?,?,?)", (nombre, tel, mail))
        self.conexion.commit() #Es necesario el commit para que funcione el INSERT
    
    def get_all(self):
 
        data =  self.cur.execute("SELECT id, nombre, tel, mail FROM contactos ORDER BY nombre ASC")
        return data.fetchall()
              
    def get_by_query(self, item):

        item = f"{item}%"
        rows = self.cur.execute(
            "SELECT * FROM contactos WHERE nombre LIKE ? OR tel LIKE ? OR mail LIKE ? ORDER BY nombre ASC", (item, item, item))

        return rows.fetchall()

    def get_by_id(self, id) :
        
        query = self.cur.execute("SELECT * FROM contactos WHERE id = ?", (id,))
        row = query.fetchone()
    
        return row

    def update(self, id:int, name:str, tel:int, mail:str):
        
        self.cur.execute("UPDATE contactos SET nombre=?,tel=?, mail=? WHERE id =?",(name, tel, mail, id,))
        self.conexion.commit() #Es necesario el commit para que funcione el UPDATE
            
    
    def delete_by_id(self, id):
        
        self.cur.execute("DELETE FROM contactos WHERE id =?",(id,))
        self.conexion.commit()








