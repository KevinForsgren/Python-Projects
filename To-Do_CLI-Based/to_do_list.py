# To Do List
to_do_lists = []
from database import Storage

class to_do():
    def __init__(self):
        # Database for storing all to-dos
        self.db = Storage()

    def adding_task(self):
        """Create task and add to the database""" 

        while True:
            print("Enter your to-do work here or enter 'quit' for exit: ")
            todo = input()
            if todo.lower() == "quit":  # Breaks if 'quit' is entered by the user
                break
            else:
                status = self._task_progress()
                # Description for to-do
                description = input("Enter Description about your todo: ")
                
                if description:
                    self.db.adding_todo(todo.title(), status, description.capitalize())
                else:
                    print("Please enter description try again")
    
    def _task_progress(self):
        progress = ["To-Do", "In-Progress", "Finished"]
        # to-do status
        while True:
            try:
                task_progress = int(input(f"1. {progress[0]} \n2. {progress[1]}\n3. {progress[2]}\nChoose from the following: "))
            except ValueError:
                print("Enter integers only")
            else:
                if task_progress in [1, 2, 3]:
                    return progress[task_progress - 1]
                else:
                    print("Choose from the given option only")
                
    def remove_task(self, id):
        """Delete task after providing appropriate id."""

        self.db.delete_todos(id)

    def show_tasks(self, status=None):
        # print elements from the list according to filter
        if status:
            self.db.list_todo_item(status)
        else:
            self.db.list_todo_item()

    def update_task(self, id, set_clause):
        """Update given task"""

        if set_clause.lower() == 'todo':
            #Provide Set type and value for updating todo
            field = input("Enter updated todo here:")
        elif set_clause.lower() == 'description':
            #Provide Set type and value for updating description
            field = input("Enter updated description here: ")
        elif set_clause.lower() == 'status':
            #Provide Set type and value for updating status
            field = self._task_progress()
        else:
            print("Provide either 'todo', 'description', 'status'")
            return

        self.db.updating_todos(id, set_clause, field)
