from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import Calls,CallsCreate
from tenant.app.db import SessionDep


router = APIRouter()


router.post("/calls")
async def create_calls(calls_data: Calls):
    return calls_data


#Crear calls
@router.post("/calls", response_model=Calls)
async def create_call(call_data: CallsCreate , session: SessionDep,tags=["calls"]):
    call = Calls.model_validate(call_data.model_dump())
    session.add(call)
    session.commit()
    session.refresh(custom(call))
    return custom(call)
