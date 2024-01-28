import sqlite3


class DatabaseHandler:
    def __init__(self):
        db_file = """backend/iems.db"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def get_all_iems(self):
        """
        Query all rows in the iems table
        """
        self.cursor.execute("SELECT * FROM iem")

        data = self.cursor.fetchall()

        return data


    def execute_query(self, query, values=None):
        if self.cursor:
            if values:
                self.cursor.execute(query, values,)
            else:
                self.cursor.execute(query)
            self.connection.commit()

    def return_data(self, query):
        if self.cursor:
            self.cursor.execute(query)
            return self.cursor.fetchall()
