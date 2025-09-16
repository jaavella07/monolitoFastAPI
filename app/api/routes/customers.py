from fastapi import APIRouter, HTTPException as HTTTPException

from tenant.app.models import Customers


router = APIRouter()


router.post("/customers")
async def create_customers(customers_data: Customers):
    return customers_data