from sqlalchemy.orm import Session
from app.repositories import task_repository
from app.models.task_schema import Task

def criar_task(db: Session, title: str, description: str, status: str) -> Task:
    return task_repository.criar_task(db, title=title, description=description, status=status)

def pegar_task(db: Session, task_id: int) -> Task:
    return task_repository.pegar_task(db, task_id)

def atualizar_task(db: Session, task_id: int, title: str, description: str, status: str) -> Task:
    return task_repository.atualizar_task(db, task_id, title=title, description=description, status=status)

def apagar_task(db: Session, task_id: int) -> Task:
    return task_repository.apagar_task(db, task_id)

def get_all_tasks(db: Session) -> list[Task]:
    return task_repository.get_all_tasks(db)
