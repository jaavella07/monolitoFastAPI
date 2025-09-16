from sqlmodel import SQLModel, Field
from datetime import datetime


class MemoryBase(SQLModel):
    type: str | None = None
    date: datetime | None = None
    source: str | None = None
    message: str | None = None
    


class MemoryCreate(MemoryBase):
    pass

class MemoryUpdate(MemoryBase):
    pass


class Memory(MemoryBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
