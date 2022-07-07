import sqlite3


conexion = sqlite3.connect("Agenda.db")

with conexion:
   cur = conexion.cursor()

   cur.execute("""CREATE TABLE IF NOT EXISTS contactos (
                                    id integer primary key autoincrement,
                                    nombre text,
                                    tel integer,
                                    mail text)
                                 """)
   conexion.commit()
   print("Connection exist")                             
      