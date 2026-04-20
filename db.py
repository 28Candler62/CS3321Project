import sqlite3

# BASED ON - https://codereview.stackexchange.com/q/182700
# https://codereview.stackexchange.com/questions/182700/python-class-to-manage-a-table-in-sqlite
# Posted by Yu Zhang, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-20, License - CC BY-SA 3.0

class AppDataBase:
    __DB_LOCATION = ':memory:'
    __DB_CREATE_TABLES_SCRIPT = 'project_tables.sql'
    __DB_POPULATE_DB_DATA_SCRIPT = 'project_data_insert.sql'

    def __init__(self):
        """Initialize and populate the database"""
        self.__db_connection = sqlite3.connect(AppDataBase.__DB_LOCATION)
        
        try:
            self.__db_cur = self.__db_connection.cursor()
        except Exception:
            raise
            
        # Create Database Tables
        self.__execute_sql_file(AppDataBase.__DB_CREATE_TABLES_SCRIPT)
        
        # Execute a SQL script file
        self.__execute_sql_file(AppDataBase.__DB_POPULATE_DB_DATA_SCRIPT)
        
    def __execute_sql_file(self, script_file):
        try:
            # Read the SQL script from the file
            with open(script_file, 'r') as f:
                sql_script = f.read()
            
            # Execute the script
            self.__db_connection.executescript(sql_script)
            
            # Note: executescript issues a COMMIT automatically, 
            # but explicit commit is often good practice for clarity
            self.__db_connection.commit()            
            #print(f"Script executed successfully")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            raise
        except FileNotFoundError:
            print(f"Script file not found: {script_file}")
            raise

    def execute(self, statement_param):
        """
        Executes a single SQL statement. Use placeholders (? or :name) to safely bind parameters and prevent SQL injection
        """
        return self.__db_connection.execute(statement_param)

    def executemany(self, statement_param, iterable_param):
        """
        Executes a parameterized SQL command against all parameter sequences in an iterable
        EXAMPLE: "INSERT INTO users (name, age) VALUES (?, ?)", [('Alice', 30), ('Bob', 25)]
        """
        return self.__db_connection.executemany(statement_param, iterable_param)

    #def commit(self):
        #"""commit changes to database"""
        #self.connection.commit()
        
    def __del__(self):
        """
        Close database connection on class exit.
        """
        self.__db_connection.close()
        print('db connection closed')
        
        
"""
EXAMPLE

db = AppDataBase()

db.execute("CREATE TABLE lang(name, first_appeared)")

data = [
    ("C++", 1985),
    ("Objective-C", 1984),
]
db.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

# Print the table contents
for row in db.execute("SELECT name, first_appeared FROM lang"):
    print(row)

print("I just deleted", db.execute("DELETE FROM lang").rowcount, "rows")
"""