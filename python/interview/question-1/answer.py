class TaskService:
    def __init__(self, database: InMemoryDB):
        self._database = database

    def open_tasks(self, project_id: str) -> list[Task]:
        return self._database.query_tasks(
            lambda task: task.project_id == project_id and task.status is Status.OPEN
        )

    def completion_rate(self, project_id: str) -> float:
        tasks = self._database.query_tasks(lambda task: task.project_id == project_id)

        if not tasks:
            return 0.0

        completed_count = sum(task.status is Status.DONE for task in tasks)

        return completed_count / len(tasks)

    def complete_task(self, task_id: str) -> Task:
        tasks = self._database.query_tasks(lambda task: task.task_id == task_id)

        if not tasks:
            raise ValueError(f"Task not found: {task_id}")

        task = tasks[0]
        task.complete()
        return task
