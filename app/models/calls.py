from sqlmodel import SQLModel, Field




class CallsBase(SQLModel):
    type: str
    date: str | None = None
    transcript: str | None = None
    recording: str | None = None
    call_status:str | None = None
    duration: int | None = None
    end_call_status: str
    summary: str
    age: int | None = None

class CallsCreate(CallsBase):
    pass

class CallsUpdate(CallsBase):
    pass


class Calls(CallsBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
