from pydantic import BaseModel


class Task(BaseModel):
    skill: str
    input: dict


class Plan(BaseModel):
    tasks: list[Task]
