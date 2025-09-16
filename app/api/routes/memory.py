from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import Memory


router = APIRouter()


router.post("/memory")
async def create_memory(memory_data: Memory):
    return memory_data