from sqlmodel import SQLModel, Field
from datetime import datetime


class CustomersBase(SQLModel):
    name: str
    phone: str
    whatsapp: str | None = None
    email: str | None = None
    calls_counter: int | None = 0
    reminders_counter: int | None = 0
    status: str
    allow_whatsapp: str
    summary: str
    created_at: datetime | None = None
    scheduled_call: bool
    call_schedule: datetime | None = None
    country: str
    is_interested: str
    company: str
  



class CustomersCreate(CustomersBase):
    pass

class CustomersUpdate(CustomersBase):
    pass


class Customers(CustomersBase, table=True):
    customer_id: int | None = Field(default=None, primary_key=True)
