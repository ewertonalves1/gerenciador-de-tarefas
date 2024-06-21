from fastapi import FastAPI
from app.controllers import Task_Controller
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(Task_Controller.router)
