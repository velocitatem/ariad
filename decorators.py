from functools import wraps
import sqlite3

"""
one database
tables:
code - associates name with code
components - associates name with component
parts - associates name with part
code 

decorators:
component - adds component to database
part - adds part to database
adding a part or component also means adding to the code table
"""

# component decorator
# Ex:component("DataLake")

class DB:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS code (
            name text primary key,
            code text
        )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS components (
            name text foreign key,
            component text
        )""")
        self.c.execute("""CREATE TABLE IF NOT EXISTS parts (
            name text foreign key,
            part text,
        )""")
        self.conn.commit()
        self.conn.close()

    def add_code(self, name, code):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO code VALUES (?, ?)", (name, code))
        self.conn.commit()
        self.conn.close()

    def add_component(self, name, component, code):
        self.add_code(name, code)
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO components VALUES (?, ?)", (name, component))
        self.conn.commit()
        self.conn.close()

    def add_part(self, name, part, code):
        self.add_code(name, code)
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("INSERT INTO parts VALUES (?, ?)", (name, part))
        self.conn.commit()
        self.conn.close()

    def get_code(self, name):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT code FROM code WHERE name=?", (name,))
        code = self.c.fetchone()
        self.conn.close()
        return code

    def get_component(self, name):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT component FROM components WHERE name=?", (name,))
        component = self.c.fetchone()
        self.conn.close()
        return component

    def get_part(self, name):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT part FROM parts WHERE name=?", (name,))
        part = self.c.fetchone()
        self.conn.close()
        return part


def component(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db = DB()
            db.add_component(name, func.__name__, func.__code__)
            return func(*args, **kwargs)
        return wrapper

    return decorator

# part decorator
# Ex:part("Insert")
def part(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db = DB()
            db.add_part(name, func.__name__, func.__code__)
            return func(*args, **kwargs)
        return wrapper

    return decorator

