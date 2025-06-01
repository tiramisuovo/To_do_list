import json
import os

class Task:
    # Task with a title, description, status, priority level
    def __init__(self, title, description, status, priority):
        self.title = title
        self.description = description
        self.status = status #False = incomplete; True = complete
        self.priority = priority #priority from 0-2; 0 = low, 1 = medium, 2 = high

    def __repr__(self):
        status_str = "Complete" if self.status else "Incomplete"
        return f"{self.title} [Description: {self.description}, Status: {status_str}, Priority: {self.priority}]"

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["description"], data["status"], data["priority"])
    

class ToDoList:
    # To do list with tasks
    def __init__(self):
        self.all_tasks = []

        self.file_path = os.path.join(os.path.expanduser("~"),"my_tasks.json")

    def save_to_file(self):
        tasks_data = [task.to_dict() for task in self.all_tasks]
        with open(self.file_path,"w") as f:
            json.dump(tasks_data, f, indent = 4)

    def load_from_file(self):
        with open(self.file_path,"r") as f:
            loaded_data = json.load(f)
            self.all_tasks = [Task.from_dict(data) for data in loaded_data]
        return self.all_tasks

    def view_all_tasks(self):
        # Give a list of all tasks
        print (self.all_tasks)

    def add_task(self, new_task):
        # Add a task to all_tasks
        self.all_tasks.append(new_task)

    def delete_task(self, task_to_delete):
        # Delete a task when a task is passed in
        new_all_tasks = []
        for task in self.all_tasks:
            if task.title != task_to_delete.title or task.description != task_to_delete.description:
                new_all_tasks.append(task)
        self.all_tasks = new_all_tasks
    
    def set_prio(self, task_to_set, choice):
        # Set priority of the task, 0 = low, 1 = medium, 2 = high
        # Title, desc, choice are strings
        for task in self.all_tasks:
            if task.title == task_to_set.title and task.description == task_to_set.description:
                if choice == "Low":
                    task.priority = 0
                elif choice == "Medium":
                    task.priority = 1
                elif choice == "High":
                    task.priority = 2