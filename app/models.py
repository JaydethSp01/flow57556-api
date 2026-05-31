from pydantic import BaseModel

class Tarea(BaseModel):
    id: int
    titulo: str
    asignado_a: str
    estado: str

class Usuario(BaseModel):
    id: int
    nombre: str

class Tablero(BaseModel):
    id: int
    nombre: str

class Comentario(BaseModel):
    id: int
    contenido: str
    tarea_id: int