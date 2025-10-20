import sqlite3
import time

class Storage():
    """A class to manage sqlite3 database"""

    def __init__(self):
        self.con = sqlite3.connect("todo.db")
        self.cursor = self.con.cursor()

        # Create to-do table if not present on initialization
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS To_do (
                id INTEGER PRIMARY KEY,
                todo VARCHAR(100) NOT NULL,
                description VARCHAR(255) DEFAULT NULL,
                status TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at DATE DEFAULT NULL
        )"""
        )
    
    def adding_todo(self, todo, status, description):
        """Stores all data into sqlite3"""

        try:
            self.cursor.execute(
                """INSERT OR FAIL INTO To_do (todo, description, status) 
                    VALUES (?, ?, ?)""",
                (
                    todo,
                    description,
                    status,
                ),
            )
            self.con.commit()
            print("|| Task Add successful ||")
        except sqlite3.Error as e:
            print(e)
            return
    
    def updating_todos(self, id, set_clause, field):
        """Update password using useid/username."""

        try:
            # Make current time
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            # Structure main sql query here
            sql = f"UPDATE To_do SET {set_clause} = ?, updated_at = ? WHERE id = ?"
            # execute sql here
            self.cursor.execute(sql, (field, current_time, id,),)
            self.con.commit()
        except sqlite3.IntegrityError:
            # throw error if value is not present
            print("Can't update non-existent entity")

    def delete_todos(self, id):
        """Delete to-do from the database using todo ID."""

        try:
            self.cursor.execute("DELETE FROM TO_do WHERE id = ?", (id,),)
            self.con.commit()
            print("\n|| Task deleted Successfully ||")
        except sqlite3.IntegrityError:
            print("Can't delete non-existent entity")

    def list_todo_item(self, status=None):
        """Show all task and also show task as per its progress."""

        select_clause = f"SELECT * FROM To_do"
        if status:
            # Filter todos list based on status
            select_clause += " Where status = ?"
            self.cursor.execute(select_clause, (status,))
        else:
            # Shows all todos
            self.cursor.execute(select_clause)
        items = self.cursor.fetchall()

        if not items:
            # Print error message if there's no todos
            print("To-do is empty please create some")
        else:
            # Print available todos based on filter
            for index, item in enumerate(items, start=1):
                self._print_db_item(index, item)

    def _print_db_item(self, index, item):
        """Print all fetch data."""

        # Show all the data here
        if item[5]:
            # show Update_at date if its there
            date = item[5]
            created_updated = "Updated"
        else:
            # otherwise show created_at date
            date = item[4]
            created_updated = "Created"
        created = date.split(" ")

        # Some styling for better visualization
        print("*" * 70)
        print()
        # Show todo name and id
        print(f"{index}. {item[1]} - ID: {item[0]}")
        # Show date created/modified one
        print(f"{created_updated} on {created[0]} at {created[1]}")
        # Show description
        print(f"Description:- {item[2]}")
        # Show task progress status
        print(f"Status:- {item[3]}")
        print()
        print("*" * 70)