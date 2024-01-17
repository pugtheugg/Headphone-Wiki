import sqlite3


class DatabaseHandler:
    def __init__(self, database):
        self.database = f"{database}.db"
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, values=None):
        if self.cursor:
            if values:
                self.cursor.execute(query, values,)
            else:
                self.cursor.execute(query)
            self.connection.commit()

    def get_data(self, query):
        if self.cursor:
            self.cursor.execute(query)
            return self.cursor.fetchall()
