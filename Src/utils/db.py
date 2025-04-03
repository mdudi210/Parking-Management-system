import mysql.connector
from assests.config import Config
from mysql.connector.errors import get_exception , get_mysql_exception , DatabaseError

"""

This is context manager to create connection with this bd,
then creating cursor and returning to perform sql queries,
then committing and closing the connection

"""


class OpenDb:
    # ,query,query_argument,fetch_type=''
    def __init__(self):
        self.host = Config.HOST
        self.user = Config.USER
        self.password = Config.PASSWORD
        self.database = Config.DATABASE
        self.connection = None
        self.cursor = None
        # self.query = query
        # self.query_argument = query_argument
        # self.fetch_type = fetch_type

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            self.cursor = self.connection.cursor()
            return self.cursor
            # self.cursor.execute(self.query,self.query_argument)

            # result = None
            
            # if self.fetch_type == "":
            #     return None
            # if self.fetch_type == 'fetchone':
            #     result = self.cursor.fetchone()
            # elif self.fetch_type == 'fetchall':
            #     result = self.cursor.fetchall()

            # if result is not None:
            #     return result
            # return None
        except DatabaseError as e:
            print("This is sql error : "+e.msg)
        except AttributeError:
            print("This is sql error : ")

        

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.connection.commit()
            self.connection.close()
        except DatabaseError as e:
            print("This is sql error : "+e.msg)
        except AttributeError as e:
            print("This is sql error : ")


