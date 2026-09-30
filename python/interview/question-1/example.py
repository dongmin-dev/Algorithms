from enum import Enum
from typing import Callable


class Status(Enum):
    OPEN = "open"
    DONE = "done"


class Task:
    def __init__(self, task_id: str, project_id: str, status: Status):
        self.task_id = task_id
        self.project_id = project_id
        self.status = status

    def complete(self) -> None:
        self.status = Status.DONE


class InMemoryDB:
    def __init__(self, tasks: list[Task]):
        self._tasks = list(tasks)

    def query_tasks(
        self,
        predicate: Callable[[Task], bool],
    ) -> list[Task]:
        return [task for task in self._tasks if predicate(task)]


class TaskService:
    def __init__(self, database: InMemoryDB):
        self._database = database

    def open_tasks(self, project_id: str) -> list[Task]:
        pass

    def completion_rate(self, project_id: str) -> float:
        pass

    def complete_task(self, task_id: str) -> Task:
        pass
