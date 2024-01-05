from peewee import *


dbLite = SqliteDatabase('agenda.db')


class Contacto(Model):
    nombre = TextField()
    correo = TextField()
    celular = IntegerField()

    class Meta:
        database = dbLite
        Table_name = 'contactos'

dbLite.connect()


# Función para obtener toda la lista.
def cargarContactos():
    contactos = []
    for cont in Contacto.select().dicts():
        contactos.append(cont)
        
    return contactos    
