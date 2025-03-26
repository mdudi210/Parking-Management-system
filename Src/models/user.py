from Src.utils import db
import hashlib


class User:
    def __init__(self, username="", password="", role=None):
        self.user_id = 0
        self.username = username.strip()
        self.password = password
        self.role = role

    """
    This to hash password
    """

    @staticmethod
    def hash_password(password):
        return hashlib.sha512(password.encode("utf-8")).hexdigest()

    """
    This is login
    """

    def login(self):
        hashed_password = self.hash_password(self.password)
        with db.OpenDb() as cursor:
            cursor.execute(
                "SELECT user_id,username, password,role FROM users WHERE username=%s",
                (self.username,),
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
            print(
                """ADD USER
                1. Add User
                2. Exit"""
            )

            try:
                option = int(input("Enter (1/2): "))
                if option == 2:
                    return
                elif option != 1:
                    print("Invalid input! Please enter 1 or 2.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

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
        self.username = input("Enter your username: ").strip()
        self.password = input("Enter your password: ")
        self.role = input("Enter the role (default: user): ").strip().lower()
        self.role = "user" if not self.role else self.role

    """
    This will check for existing user
    """

    def check_existing_user(self):
        with db.OpenDb() as cursor:
            cursor.execute(
                "SELECT username FROM users WHERE username=%s", (self.username,)
            )
            return cursor.fetchone() is not None

    """
    This is to add new user to db
    """

    def add_user_to_db(self):
        role_id = 1 if self.role == "admin" else 2
        hashed_password = self.hash_password(self.password)

        with db.OpenDb() as cursor:
            cursor.execute(
                "INSERT INTO Users(username, password, role) VALUES (%s, %s, %s)",
                (self.username, hashed_password, role_id),
            )
