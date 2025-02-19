from fastapi import FastAPI
from app.database import Base, engine
from app.routes import tasks

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def root():
    return {"message": "Todo API is running"}
