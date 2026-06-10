from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: str

tasks: List[Task] = []
next_id = 1

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_create: TaskCreate):
    global next_id
    task = Task(id=next_id, title=task_create.title, description=task_create.description)
    tasks.append(task)
    next_id += 1
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = Task(id=task.id, title=task_update.title, description=task_update.description, completed=task.completed)
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            del tasks[index]
            return
    raise HTTPException(status_code=404, detail="Task not found")
