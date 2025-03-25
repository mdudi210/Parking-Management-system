from Src.utils import db
import hashlib


class User:
    def __init__(self, username="", password="", role=None):
        self.user_id = 0
        self.username = username
        self.password = password
        self.role = role

    def login(self):

        # hashing the password
        hashed_password = hashed_string = hashlib.sha256(
            self.password.encode("utf-8")
        ).hexdigest()
        """
        

        """
        with db.OpenDb() as cursor:
            cursor.execute(
                "SELECT username,password,role FROM users WHERE username=%s",
                (self.username,),
            )
            result = cursor.fetchone()
            if not result:
                print(result)
                return result
            elif result[1] == hashed_password:
                print(result)
                return result
            else:
                return None

    def logout(self):
        pass

    """

    """

    def add_user_menu(self):
        print(
            """ADD USER
            1. Add User
            2. Exit"""
        )

        try:
            option = int(input("Enter(1/2):- "))
            if option > 2 or option < 1:
                print("Wrong Input")
                self.add_user_menu()
        except ValueError:
            print("Wrong Input")
            self.add_user_menu()
        return option

    """
    
    """

    def add_user(self):
        option = self.add_user_menu()
        if option == 1:
            self.username = input("Enter your User Name:- ").strip()
            self.password = input("Enter your Password:- ")
            self.role = input("Enter the role (Bydefault user):- ")
            role_id = 2
            """
            
            """
            if self.role == "admin":
                role_id = 1
            with db.OpenDb() as cursor:
                cursor.execute(
                    "SELECT username FROM users WHERE username=%s", (self.username,)
                )
                check_username = cursor.fetchone()
                if not check_username:
                    cursor.execute(
                        """
                        INSERT INTO Users(username,password,role) VALUES (%s,%s,%s)
                        """,
                        (
                            self.username,
                            hashlib.sha256(self.password.encode("utf-8")).hexdigest(),
                            role_id,
                        ),
                    )
                    print("user added...!")
                    self.add_user()
                else:
                    print("user already exists\nPlease change your user name")
                    self.add_user()
        elif option == 2:
            return
