from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

tableros = []

class Tablero(BaseModel):
    id: int
    name: str

@router.get("/tablero", response_model=List[Tablero])
async def get_tableros():
    return tableros

@router.post("/tablero", response_model=Tablero)
async def create_tablero(tablero: Tablero):
    tableros.append(tablero)
    return tablero

@router.get("/tablero/{tablero_id}", response_model=Tablero)
async def get_tablero(tablero_id: int):
    for tablero in tableros:
        if tablero.id == tablero_id:
            return tablero
    raise HTTPException(status_code=404, detail="Tablero not found")

@router.put("/tablero/{tablero_id}", response_model=Tablero)
async def update_tablero(tablero_id: int, updated_tablero: Tablero):
    for i, tablero in enumerate(tableros):
        if tablero.id == tablero_id:
            tableros[i] = updated_tablero
            return updated_tablero
    raise HTTPException(status_code=404, detail="Tablero not found")

@router.delete("/tablero/{tablero_id}")
async def delete_tablero(tablero_id: int):
    for i, tablero in enumerate(tableros):
        if tablero.id == tablero_id:
            del tableros[i]
            return
    raise HTTPException(status_code=404, detail="Tablero not found")
