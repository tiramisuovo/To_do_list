from PySide6.QtWidgets import QApplication
from mainwindow import ToDoApp
from models import ToDoList

app = QApplication([])

todo_model = ToDoList()
window = ToDoApp(todo_model)
window.show()
app.exec()