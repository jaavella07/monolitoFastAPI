from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import WhatsApp

router = APIRouter()


router.post("/whatsapp")
async def create_whatsapp(whatsapp_data: WhatsApp):
    return whatsapp_data