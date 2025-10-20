from argparse import ArgumentParser, Namespace
import sys
from to_do_list import to_do as td

class to_do_cli():
    def __init__(self):
        self.to_do_manager = td()
        self.parser = ArgumentParser(
            prog='To-Do Manager', description='Use to managing and tracking tasks',)


    def main(self):
        """Main area for managing CLI for to-do list"""

        # Add command line arguments:
        self.parser.add_argument(
            '--task_cli',
            help="To-Do Manager - provide add, update, show or delete for adding, updating, showing and removing tasks repectively",
            type = str)
        self.parser.add_argument(
            '--todo_id',
            help="Need to give id from your available todos for deleting and updating todos ",
            type = int)
        self.parser.add_argument(
            '--field',
            help="Update the provided field i.e 'todo', 'description' or 'status'",
            type = str)
        self.parser.add_argument(
            '--filter',
            help="If provided shows task based on its progress i.e To-Do, In-Progress or Finished",
            type = str)

        # Parse the arguments:
        args: Namespace = self.parser.parse_args()

        if args.task_cli == 'add':
            # For adding task in todos
            self.to_do_manager.adding_task()
        elif args.task_cli == 'delete':
            if args.todo_id:
                # For deleting todo if id is given      
                self.to_do_manager.remove_task(int(args.todo_id))
            else:
                print("Please provide ID for finding your task")
        elif args.task_cli == 'update':
            # For updating todo if id and update field is given
            if args.todo_id and args.field in ['todo', 'description', 'status']:
                self.to_do_manager.update_task(int(args.todo_id), args.field)
            else:
                print("Something went wrong. Try again")
        elif args.task_cli == 'show' and args.filter:
            # Show task based on its progress
            if args.filter in ["To-Do", "In-Progress", "Finished"]:
                print(f"All To-do list that are '{args.filter}'")
                print()
                self.to_do_manager.show_tasks(args.filter)
            else:
                # Print all if provided filter is not available
                print(f"Provided status is not available, showing all entries")
                print()
                self.to_do_manager.show_tasks()
        elif args.task_cli == 'show':
            self.to_do_manager.show_tasks()
        else:
            print("Provided option is not available right now or there error in your input")
        # if args.task_cli.lower == 'add':
        #     self.to_do_manager.adding_task()

if __name__ == "__main__":
    to_do_main = to_do_cli()
    to_do_main.main()

