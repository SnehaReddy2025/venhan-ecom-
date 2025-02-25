from fastapi import FastAPI
from app.api.v1_router import api_router
from app.db.conn import init_db
import uvicorn

app = FastAPI(title="FastAPI Backend", version="1.0")

@app.on_event("startup")
async def startup_db_client():
    await init_db()

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8020)

