from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import Calls


router = APIRouter()


router.post("/calls")
async def create_calls(calls_data: Calls):
    return calls_data