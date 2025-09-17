from sqlmodel import SQLModel, Field,Relationship
from datetime import datetime
from typing import List

from tenant.app.models.whatsapp import WhatsApp



class CustomersBase(SQLModel):
    name: str = Field(default=None)
    phone: str = Field(default=None)
    whatsapp: str = Field(default=None)
    email: str | None = None
    calls_counter: int | None = 0
    reminders_counter: int | None = 0
    status: str = Field(default=None)
    allow_whatsapp: str = Field(default=None)
    summary: str = Field(default=None)
    created_at: datetime | None = None
    scheduled_call: bool
    call_schedule: datetime | None = None
    country: str = Field(default=None)
    is_interested: str = Field(default=None)
    company: str = Field(default=None)
  


class CustomersCreate(CustomersBase):
    pass

class CustomersUpdate(CustomersBase):
    pass


class Customers(CustomersBase, table=True):
    __tablename__ = "customers"
    customer_id: int | None = Field(default=None, primary_key=True)

    whatsapps: List[WhatsApp] = Relationship(back_populates="customer")