from fastapi import FastAPI

from app.internal import configurations, system

app = FastAPI()

app.include_router(configurations.router, prefix="/config")
app.include_router(system.router, prefix="/system")


@app.get("/")
async def root():
    return {"message": "Hello you"}
