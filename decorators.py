from functools import wraps
import inspect
import sqlite3

"""
one database
tables:
code - associates name with code
components - associates name with component
parts - associates name with part
--- all makes use of primary and foreign keys connecting by name

decorators:
component - adds component to database
part - adds part to database
adding a part or component also means adding to the code table
"""

# component decorator
# Ex:component("DataLake")

from src.db import DB


def component(name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db = DB()
            # code_str:
            code_str = inspect.getsource(func)
            db.add_component(name, func.__name__, code_str)
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
            code_str = inspect.getsource(func)
            db.add_part(name, func.__name__, code_str)
            return func(*args, **kwargs)
        return wrapper

    return decorator

