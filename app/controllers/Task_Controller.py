from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services import task_service
from app.models.task_schema import Task, TaskCreate, TaskUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/tasks/", response_model=list[Task])
def pegar_tasks(db: Session = Depends(get_db)):
    return task_service.get_all_tasks(db=db)
@router.put("/tasks/{task_id}", response_model=Task)
def atualizar_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return task_service.atualizar_task(db=db, task_id=task_id, title=task.title, description=task.description, status=task.status)

@router.delete("/tasks/{task_id}", response_model=Task)
def apagar_task(task_id: int, db: Session = Depends(get_db)):
    return task_service.apagar_task(db=db, task_id=task_id)

@router.get("/tasks/{task_id}", response_model=Task)
def pegar_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.pegar_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="ID inexistente")
    return db_task

@router.post("/tasks/", response_model=Task)
def criar_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.criar_task(db=db, title=task.title, description=task.description, status=task.status)

