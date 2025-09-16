from sqlmodel import SQLModel, Field
from datetime import datetime


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
    chat_id: int | None = Field(default=None, primary_key=True)
