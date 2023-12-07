import sqlite3
from typing import Callable, Any, Dict

class Ariad:
    _instances = {}



    def __init__(self, project_id: str):
        self.project_id = project_id
        self.conn = sqlite3.connect(f'{project_id}.sqlite')
        self.modules = {}
        self._create_tables()

    def _create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS modules (
                name TEXT PRIMARY KEY,
                code TEXT NOT NULL
            )
        ''')
        self.conn.commit()
        # load modules
        cursor.execute('SELECT name, code FROM modules')
        for name, code in cursor.fetchall():
            self.modules[name] = code



    def store_function_to_cache(self, module_func: Callable):
        # save as a file in the .ariad folder
        import uuid
        import inspect
        id = uuid.uuid4()
        # make .ariad folder if it doesn't exist
        import os
        if not os.path.exists(".ariad"):
            os.makedirs(".ariad")
        with open(f".ariad/{id}.py", "w") as f:
            f.write(inspect.getsource(module_func))

        return f".ariad/{id}.py"

    def load_function_from_cache(self, module_name: str):
        # load from .ariad folder
        import importlib.util
        import os

        # Convert the file path to a module name

        # Load the module
        spec = importlib.util.spec_from_file_location(module_name, os.path.join(os.getcwd(), module_name))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module
    def register_module(self, module_name: str, module_func: Callable):
        cursor = self.conn.cursor()
        print(f"Registering module '{module_name}'")
        module_func = self.store_function_to_cache(module_func)
        cursor.execute('INSERT OR REPLACE INTO modules (name, code) VALUES (?, ?)',
                       (module_name, module_func))
        print(f"Registered module '{module_name}' with SQL: {cursor.lastrowid}")
        self.conn.commit()
        self.modules[module_name] = module_func

    def list_modules(self) -> Dict[str, str]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT name, description FROM modules')
        return {name: description for name, description in cursor.fetchall()}


    @classmethod
    def register(cls, project_id: str):
        if project_id not in cls._instances:
            cls._instances[project_id] = cls(project_id)
        return cls._instances[project_id]

    # ...

    def execute_module(self, module_name: str, *args, **kwargs) -> Any:
        module = self.modules.get(module_name)
        module = self.load_function_from_cache(module)
        print(f"Executing module '{module}'")
        if module is not None:
            func = getattr(module, module_name)
            return func(*args, **kwargs)
        else:
            raise Exception(f"Module '{module_name}' not found")