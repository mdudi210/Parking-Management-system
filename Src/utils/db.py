import mysql.connector


class OpenDb:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "Watchguard@01"
        self.database = "ParkingSystem"
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
