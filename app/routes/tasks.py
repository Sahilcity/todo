from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud, database, models

router = APIRouter()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db), user_id: int = 1):
    return crud.create_task(db, task, owner_id=user_id)

@router.get("/", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(database.get_db), user_id: int = 1):
    return crud.get_tasks(db, owner_id=user_id)
