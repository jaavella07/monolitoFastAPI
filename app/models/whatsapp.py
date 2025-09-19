from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional

 


class WhatsAppBase(SQLModel):
    phone: int | None = None
    session_id: str | None = None
    message: str | None = None
    source: str | None = None
    date: datetime | None = None

class WhatsAppCreate(WhatsAppBase):
    pass

class WhatsAppUpdate(WhatsAppBase):
    pass


class WhatsApp(WhatsAppBase, table=True):
    __tablename__ = "whatsapp"
    chat_id: int | None = Field(default=None, primary_key=True)

    # customer_id: Optional[int] = Field(default=None, foreign_key="customers.customer_id")
    # customer: "Customers" = Relationship(back_populates="whatsapps")