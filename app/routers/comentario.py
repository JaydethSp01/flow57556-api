from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

comentarios = []

class Comentario(BaseModel):
    id: int
    content: str

@router.get("/comentario", response_model=List[Comentario])
async def get_comentarios():
    return comentarios

@router.post("/comentario", response_model=Comentario)
async def create_comentario(comentario: Comentario):
    comentarios.append(comentario)
    return comentario

@router.get("/comentario/{comentario_id}", response_model=Comentario)
async def get_comentario(comentario_id: int):
    for comentario in comentarios:
        if comentario.id == comentario_id:
            return comentario
    raise HTTPException(status_code=404, detail="Comentario not found")

@router.put("/comentario/{comentario_id}", response_model=Comentario)
async def update_comentario(comentario_id: int, updated_comentario: Comentario):
    for i, comentario in enumerate(comentarios):
        if comentario.id == comentario_id:
            comentarios[i] = updated_comentario
            return updated_comentario
    raise HTTPException(status_code=404, detail="Comentario not found")

@router.delete("/comentario/{comentario_id}")
async def delete_comentario(comentario_id: int):
    for i, comentario in enumerate(comentarios):
        if comentario.id == comentario_id:
            del comentarios[i]
            return
    raise HTTPException(status_code=404, detail="Comentario not found")
