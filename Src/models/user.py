import hashlib
from src.utils import db
from src.system import System
from src.dbutils import DbConfig
import sys


class User:
    def __init__(self, username="", password="", role=None):
        self.user_id = 0
        self.username = username.strip()
        self.password = password
        self.role = role

    

    @staticmethod
    def hash_password(password):
        """ This to hash password """
        return hashlib.sha512(password.encode("utf-8")).hexdigest()

    """
    This is login
    """

    def login(self):
        hashed_password = self.hash_password(self.password)
        # with db.OpenDb(DbConfig.LOGIN_INSERT,(self.username,),'fetchone') as data:
        #     result = data
        with db.OpenDb() as cursor:
            cursor.execute(
                DbConfig.LOGIN_INSERT,(self.username,),
                )
            result = cursor.fetchone()

        if result and result[2] == hashed_password:
            print("Login successful!")
            return result
        else:
            print("Invalid username or password.")
            return None

    """
    This to logout but not using anywhere right now
    """

    def logout(self):
        pass

    """
    This is to add new user
    """

    def add_user(self):
        while True:
            print(System.ADD_USER)

            try:
                option = int(input("Enter (1/2): "))
                if option == 2:
                    return
                elif option != 1:
                    print(System.INVALID_OPTION)
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            except KeyboardInterrupt:
                print(System.EXITING)
                sys.exit(0)

            # Getting user details
            self.get_user_details()

            # Checking if user is in db or not
            if self.check_existing_user():
                print("User already exists. Please choose a different username.")
                continue

            # Adding user to db
            self.add_user_to_db()
            print("User added successfully!")

    """
    THis to get user details
    """

    def get_user_details(self):
        self.username = input(System.ENTER_NAME).strip()
        self.password = input(System.ENTER_PASSWORD)
        self.role = input("Enter the role (default: user): ").strip().lower()
        self.role = "user" if not self.role else self.role

    """
    This will check for existing user
    """

    def check_existing_user(self):
        # with db.OpenDb(DbConfig.CHECK_EXISTING_USER,(self.username,),'fetchone') as data:
        #     return data is not None
        with db.OpenDb() as cursor:
            cursor.execute(
                DbConfig.CHECK_EXISTING_USER, (self.username,)
            )
            return cursor.fetchone() is not None

    """
    This is to add new user to db
    """

    def add_user_to_db(self):
        role_id = 1 if self.role == "admin" else 2
        hashed_password = self.hash_password(self.password)

        # with db.OpenDb(DbConfig.ADD_USER_TO_DB,(self.username, hashed_password, role_id)):
        #     pass
        with db.OpenDb() as cursor:
            cursor.execute(
                DbConfig.ADD_USER_TO_DB,(self.username, hashed_password, role_id),
            )
