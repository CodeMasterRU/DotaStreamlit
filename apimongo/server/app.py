from fastapi import FastAPI

from server.routes.dota import router as DotaRouter

app = FastAPI()

app.include_router(DotaRouter, tags=["dota"], prefix="/dota")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this app!"}



