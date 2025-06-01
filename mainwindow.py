from PySide6.QtWidgets import QMainWindow
from ui_todo import Ui_MainWindow
import resources_rc
from models import ToDoList
from tree_widget import TreeWidget

class ToDoApp(QMainWindow):
    def __init__(self, todo_model):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.List.clear()
        self.todo_manager = todo_model
        self.tree_manager = TreeWidget(self.ui.List, self.todo_manager)
        self.setWindowTitle("To-Do List")

        self.ui.Add.clicked.connect(self.add_task)
        self.ui.Delete.clicked.connect(self.delete_task)
        self.ui.actionSave.triggered.connect(self.todo_manager.save_to_file)
        self.ui.actionLoad.triggered.connect(self.load_and_display)

        self.load_and_display()

    def add_task(self):
        # Add a task when pushbutton pressed
        title = self.ui.Title_input.text()
        desc = self.ui.Desc_input.text()
        self.tree_manager.add_task(title, desc)
        self.ui.Title_input.clear()
        self.ui.Desc_input.clear()
    
    def delete_task(self):
        # Delete a task when selected
        self.tree_manager.delete_task()
    
    def load_and_display(self):
        # Load UI for task list
        task_list = self.todo_manager.load_from_file() #list of loaded tasks
        self.ui.List.clear()
        self.tree_manager.item_to_task.clear()
        for task_obj in task_list:
            self.tree_manager.display_task(task_obj) 