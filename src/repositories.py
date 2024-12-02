from abc import ABC, abstractmethod
from typing import List
import sqlite3
from .models import Task
from datetime import datetime

class TaskRepository(ABC):
    @abstractmethod
    def create(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def get_all(self) -> List[Task]:
        pass
    
    @abstractmethod
    def update(self, task: Task) -> Task:
        pass
    
    @abstractmethod
    def delete(self, task_id: int) -> None:
        pass

class SQLiteTaskRepository(TaskRepository):
    # Copiar implementación del código original