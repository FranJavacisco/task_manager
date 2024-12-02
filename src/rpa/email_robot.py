from datetime import datetime, timedelta
import logging
from ..models import Task
from ..repositories import TaskRepository
from ..services import EmailService

class TaskReminderRobot:
    # Copiar implementación del código original