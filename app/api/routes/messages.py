from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import Messages


router = APIRouter()


router.post("/messages")
async def create_messages(messages_data: Messages):
    return messages_data