# main.py
from src.services import TaskService, EmailService
from src.repositories import SQLiteTaskRepository
from src.rpa.email_robot import TaskReminderRobot
from datetime import datetime
import os
from dotenv import load_dotenv

def print_menu():
    print("\n1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Send Reminders")
    print("6. Exit")

def main():
    load_dotenv()
    
    repo = SQLiteTaskRepository()
    task_service = TaskService(repo)
    email_service = EmailService(
        os.getenv('SMTP_SERVER'),
        int(os.getenv('SMTP_PORT')),
        os.getenv('EMAIL_USER'),
        os.getenv('EMAIL_PASSWORD')
    )
    
    robot = TaskReminderRobot(repo, email_service, os.getenv('EMAIL_USER'))
    
    while True:
        print_menu()
        choice = input("Select option: ")
        
        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            date_str = input("Due date (YYYY-MM-DD): ")
            due_date = datetime.strptime(date_str, "%Y-%m-%d")
            task_service.create_task(title, desc, due_date)
            
        elif choice == "2":
            tasks = task_service.get_tasks()
            for task in tasks:
                print(f"\n{task.id}: {task.title} - {task.status}")
                print(f"Due: {task.due_date}")
                
        elif choice == "3":
            task_id = int(input("Task ID to complete: "))
            task_service.complete_task(task_id)
            
        elif choice == "4":
            task_id = int(input("Task ID to delete: "))
            task_service.delete_task(task_id)
            
        elif choice == "5":
            robot.check_and_send_reminders()
            print("Reminders sent")
            
        elif choice == "6":
            break

if __name__ == "__main__":
    main()