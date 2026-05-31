from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

tareas = []

class Tarea(BaseModel):
    id: int
    title: str
    description: str

@router.get("/tarea", response_model=List[Tarea])
async def get_tareas():
    return tareas

@router.post("/tarea", response_model=Tarea)
async def create_tarea(tarea: Tarea):
    tareas.append(tarea)
    return tarea

@router.get("/tarea/{tarea_id}", response_model=Tarea)
async def get_tarea(tarea_id: int):
    for tarea in tareas:
        if tarea.id == tarea_id:
            return tarea
    raise HTTPException(status_code=404, detail="Tarea not found")

@router.put("/tarea/{tarea_id}", response_model=Tarea)
async def update_tarea(tarea_id: int, updated_tarea: Tarea):
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            tareas[i] = updated_tarea
            return updated_tarea
    raise HTTPException(status_code=404, detail="Tarea not found")

@router.delete("/tarea/{tarea_id}")
async def delete_tarea(tarea_id: int):
    for i, tarea in enumerate(tareas):
        if tarea.id == tarea_id:
            del tareas[i]
            return
    raise HTTPException(status_code=404, detail="Tarea not found")
