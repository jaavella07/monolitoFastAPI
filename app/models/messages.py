from sqlmodel import SQLModel, Field


class MessagesBase(SQLModel):
    phone: int | None = None


class MessagesCreate(MessagesBase):
    pass

class MessagesUpdate(MessagesBase):
    pass


class Messages(MessagesBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
