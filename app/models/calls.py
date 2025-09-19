from sqlmodel import SQLModel, Field


class CallsBase(SQLModel):
    type: str
    date: str = Field(default=None)
    transcript: str = Field(default=None)
    recording: str = Field(default=None)
    call_status:str = Field(default=None)
    duration: int | None = None
    end_call_status: str = Field(default=None)
    summary: str = Field(default=None)
    age: int | None = None

class CallsCreate(CallsBase):
    pass

class CallsUpdate(CallsBase):
    pass


class Calls(CallsBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
