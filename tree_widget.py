from PySide6.QtWidgets import QTreeWidgetItem, QComboBox, QCheckBox
from PySide6.QtCore import Qt
from models import Task, ToDoList

class TreeWidget():
    def __init__(self, tree_widget, todo_model):
        self.tree = tree_widget
        self.todo_manager = todo_model
        self.item_to_task = {} #Stores all tasks with item as a key
        self.prio_dic = {} #Stores all priority with item as a key
        self.tree.itemChanged.connect(self.handle_item_changed)
    
    def add_task(self, title, desc):
        # Add a task to the tree if newly created by user
        item = QTreeWidgetItem([title, desc, ""])
        item.setFlags(item.flags() | Qt.ItemIsEditable) #editable item
        self.tree.addTopLevelItem(item)
        task_obj = Task(title, desc, False, 0)

        # Create Widgets
        self.create_prio(item, task_obj.priority)
        self.create_status(item, task_obj.status)

        # Store task in backend
        self.todo_manager.add_task(task_obj)
        self.item_to_task[item] = task_obj

    def create_prio(self, item, priority=0):
        # Create a dropdown menu and set priority
        prio_dropdown = QComboBox()
        prio_dropdown.addItems(["Low", "Medium", "High"])
        prio_dropdown.setCurrentIndex(priority)
        self.tree.setItemWidget(item, 3, prio_dropdown)

        # Store dropdown widget object
        self.prio_dic[item] = prio_dropdown

        # Connect signal
        prio_dropdown.currentTextChanged.connect(lambda choice, i=item: self.update_prio_backend(choice, i))
    
    def update_prio_backend(self, choice, item):
        # Takes an item (i.e. a line in TreeWidget) and a choice from the prio dropdown menu
        # to update task_prio in backend
        curr_task = self.item_to_task.get(item)
        self.todo_manager.set_prio(curr_task, choice)
        
    def create_status(self, item, status=False):
        # Create a checkbox and set status
        stat = QCheckBox()
        stat.setChecked(status)
        self.tree.setItemWidget(item, 2, stat)

        # Connect signal
        stat.stateChanged.connect(lambda state, i=item: self.update_stat_backend(state, i))

    def update_stat_backend(self, state, item):
        # Takes a state and an item to change backend task status
        curr_task = self.item_to_task.get(item)
        if curr_task:
            curr_task.status = bool(state)

    def delete_task(self):
        # Delete the selected task from the tree
        selected = self.tree.currentItem()
        if selected:
            curr_task = self.item_to_task.get(selected)
            self.tree.takeTopLevelItem(self.tree.indexOfTopLevelItem(selected))
            self.todo_manager.delete_task(curr_task)
            del self.item_to_task[selected]

    def handle_item_changed(self, item, column):
        # Change backend when an item is changed
        curr_task = self.item_to_task.get(item)
        if curr_task:
            curr_task.title = item.text(0)
            curr_task.description = item.text(1)
    
    def display_task(self, task_obj):
        # Display the task in UI, not updating the backend
        item = QTreeWidgetItem([task_obj.title, task_obj.description, ""])
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.tree.addTopLevelItem(item)

        self.create_prio(item, task_obj.priority)
        self.create_status(item, task_obj.status)
        self.item_to_task[item] = task_obj