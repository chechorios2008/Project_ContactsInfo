from pydantic import *

class ContactoRequestModel(BaseModel):
    nombre: str
    correo: str
    celular: int


class ContactoResponseModel(ContactoRequestModel):
    id: int
