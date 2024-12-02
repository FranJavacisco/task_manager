from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: str
    due_date: datetime
    status: str = "pending"