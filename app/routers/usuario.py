from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

usuarios = []

class Usuario(BaseModel):
    id: int
    name: str
    email: str

@router.get("/usuario", response_model=List[Usuario])
async def get_usuarios():
    return usuarios

@router.post("/usuario", response_model=Usuario)
async def create_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return usuario

@router.get("/usuario/{usuario_id}", response_model=Usuario)
async def get_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.put("/usuario/{usuario_id}", response_model=Usuario)
async def update_usuario(usuario_id: int, updated_usuario: Usuario):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            usuarios[i] = updated_usuario
            return updated_usuario
    raise HTTPException(status_code=404, detail="Usuario not found")

@router.delete("/usuario/{usuario_id}")
async def delete_usuario(usuario_id: int):
    for i, usuario in enumerate(usuarios):
        if usuario.id == usuario_id:
            del usuarios[i]
            return
    raise HTTPException(status_code=404, detail="Usuario not found")
