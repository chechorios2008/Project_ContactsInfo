from fastapi import FastAPI
from fastapi.requests import HTTPConnection
from database import dbLite as connection
from database import *
from schemas import *
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Api Contactos", 
              description="Aplicativo web para administración de contactos", 
              version='1.0')

# Solución Cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([Contacto])


@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()


#Función agregar
@app.post('/api/v1/contacto/agregar', tags=["Admin Contactos"])
async def agregar_contacto(contacto_request: ContactoRequestModel):
    cont = Contacto.create(
        nombre = contacto_request.nombre,
        correo = contacto_request.correo,
        celular = contacto_request.celular
    )
    return (contacto_request)


# Función eliminar.
@app.delete('/api/v1/eliminar/{contacto_id}', tags=["Admin Contactos"])
async def eliminar_contacto(contacto_id):
    cont = Contacto.select().where(Contacto.id == contacto_id).first()

    if cont:
        cont.delete_instance()
        return True, 'Contacto eliminado exitosamente.'
    else:
        return HTTPConnection(404, 'El contacto no se encuentra registrado')


# Función lista.
@app.get('/api/v1/contactos', tags=["Admin Contactos"])
def lista_contactos():
    tmp = cargarContactos()
    return tmp