from typing import Optional
import fastapi
from fastapi import Path, Query
from pydantic import BaseModel

router = fastapi.APIRouter()

@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses")
async def read_courses():
    return {"courses": []}

@router.get("/courses/:id")
async def read_course():
    return {"courses": []}

@router.get("/courses/:id")
async def update_course():
    return {"courses": []}

@router.get("/courses/:id")
async def delete_course():
    return {"courses": []}

@router.get("/courses/:sections")
async def read_course_sections():
    return {"courses": []}