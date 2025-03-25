from Src.utils import db
import hashlib
from Src.models import user, pricing, parking_slot


class ParkingSystem:
    def welcome_page(self):
        print("Welcome to watchguard Parking")
        username = input("Enter your User Name:- ").strip()
        password = input("Enter your Password:- ")

        auth = user.User(username=username, password=password).login()
        if not auth:
            print("\n\n**Username or Password is incorrect**\n\n")
            self.welcome_page()
        elif auth[2] == 1:
            self.admin_menu()
        elif auth[2] == 2:
            self.customer_menu()
        else:
            print("somthing went wrong")

    # Admin menu option
    def admin_menu(self):
        print(
            """Welcome Admin, please select an option:
            1. Add User
            2. Manage Parking Slots
            3. Set Pricing Rates
            4. View Income (Daily/Monthly)
            5. View Total Income per Vehicle
            6. Log Out"""
        )
        try:
            option = int(input("Enter Your Option:- "))
        except ValueError as e:
            print("Input must be an Integer")
            option = 0
        match option:
            case 1:
                if not user.User().add_user():
                    self.admin_menu()
            case 2:
                if not parking_slot.ParkingSlot().manage_slot():
                    self.admin_menu()
            case 3:
                if not pricing.Pricing().set_price():
                    self.admin_menu()
            case 4:
                pass
            case 5:
                pass
            case 6:
                self.welcome_page()
            case _:
                print("You have Entered Wrong Option")
                self.admin_menu()

    # Customer menu option
    def customer_menu(self):
        print(
            """Welcome User, please select an option:
              1. View Available Parking Slots
              2. Park Vehicle
              3. Unpark Vehicle
              4. View Parking History
              5. Log Out"""
        )
        try:
            option = int(input("Enter Your Option"))
        except ValueError as e:
            print("Input must be an Integer")
            option = 0
        match option:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                self.welcome_page()
            case _:
                print("You have Entered Wrong Option")
                self.customer_menu()
