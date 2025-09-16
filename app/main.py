from fastapi import FastAPI

from tenant.app.db.db import create_all_tables

from tenant.app.api.routes import customers,messages,calls,memory,whatsapp


app = FastAPI(title="Tenant App", version="1.0.0",lifespan=create_all_tables)

app.include_router(calls.router,prefix="/api/calls")
app.include_router(customers.router,prefix="/api/customers")
app.include_router(memory.router,prefix="/api/memory")
app.include_router(messages.router,prefix="/api/messages")
app.include_router(whatsapp.router,prefix="/api/whatsapp")



@app.get("/")
async def root():
    return {
        "message": "app is running",
        "status": "ok"
        }

