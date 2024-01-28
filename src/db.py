import sqlite3
class DB:
    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS code (name TEXT, version INTEGER, code TEXT, PRIMARY KEY (name, version))")
        self.c.execute("CREATE TABLE IF NOT EXISTS components (name TEXT, version INTEGER, component TEXT, PRIMARY KEY (name, version))")
        self.c.execute("CREATE TABLE IF NOT EXISTS parts (name TEXT, version INTEGER, part TEXT, PRIMARY KEY (name, version))")
        self.conn.commit()
        self.conn.close()

    def _add_versioned_item(self, table, name, item, code=None):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        # Get the highest version number for the existing item
        self.c.execute(f"SELECT MAX(version) FROM {table} WHERE name=?", (name,))
        result = self.c.fetchone()
        version = 1 if result[0] is None else result[0] + 1

        # If code is provided, add it to the code table with the new version
        if code is not None:
            self.c.execute("INSERT INTO code VALUES (?, ?, ?)", (name, version, code))

        # Insert the new version of the item
        self.c.execute(f"INSERT INTO {table} VALUES (?, ?, ?)", (name, version, item))
        self.conn.commit()
        self.conn.close()

    def add_code(self, name, code):
        self._add_versioned_item('code', name, code, code)

    def add_component(self, name, component, code):
        self._add_versioned_item('components', name, component, code)

    def add_part(self, name, part, code):
        self._add_versioned_item('parts', name, part, code)

    def get_latest_code(self, name):
        return self._get_latest_item('code', name)

    def get_latest_component(self, name):
        return self._get_latest_item('components', name)

    def get_latest_part(self, name):
        return self._get_latest_item('parts', name)

    def _get_latest_item(self, table, name):
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute(f"SELECT * FROM {table} WHERE name=? ORDER BY version DESC LIMIT 1", (name,))
        item = self.c.fetchone()
        self.conn.close()
        return item
