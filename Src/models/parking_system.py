import getpass
from src.models import user, pricing, parking_slot, parking_record , income_record
from src.system import System
import sys

class ParkingSystem:
    def __init__(self):
        self.current_user = None

    def welcome_page(self):
        print(System.WELCOME)

        while True:
            try :
                username = input(System.ENTER_NAME).strip()
                password = getpass.getpass(System.ENTER_PASSWORD)
            except KeyboardInterrupt:
                print(System.EXITING)
                sys.exit(0)

            auth = user.User(username=username, password=password).login()
            if not auth:
                print(System.INVALID_USER_PASSWORD)
            else:
                self.current_user = {
                    "user_id": auth[0],
                    "username": auth[1],
                    "role": auth[3],
                }
                break

        if self.current_user["role"] == 1:
            self.admin_menu()
        elif self.current_user["role"] == 2:
            self.customer_menu()
        else:
            print(System.SOMETHING_WRONG)

    def get_option(self, menu_options):
        while True:
            try:
                option = int(input(f"{System.ENTER_OPTION}: "))
                if option in menu_options:
                    return option
                print(System.INVALID_OPTION)
            except ValueError:
                print(System.MUST_INTEGER)
            except KeyboardInterrupt:
                print(System.EXITING)
                sys.exit(0)

    def admin_menu(self):
        """Admin menu options."""
        while True:
            print(System.ADMIN_MENU)
            option = self.get_option({1, 2, 3, 4, 5, 6})

            if option == 1:
                user.User().add_user()
            elif option == 2:
                parking_slot.ParkingSlot().manage_slot()
            elif option == 3:
                pricing.Pricing().set_price()
            elif option == 4:
                # Implement view income functionality
                income_record.IncomeRecord.view_income()
            elif option == 5:
                # Implement total income per vehicle
                income_record.IncomeRecord.view_total_income_per_vehicle()
            elif option == 6:
                self.current_user = None
                self.welcome_page()
                break

    def customer_menu(self):
        """Customer menu options."""
        while True:
            print(System.CUSTOMER_MENU)
            option = self.get_option({1, 2, 3, 4, 5})

            if option == 1:
                parking_slot.ParkingSlot().is_available_slots()
            elif option == 2:
                parking_record.ParkingRecord(
                    user_id=self.current_user["user_id"],
                    username=self.current_user["username"],
                    role=self.current_user["role"],
                ).park_vehicle()
            elif option == 3:
                parking_record.ParkingRecord(
                    user_id=self.current_user["user_id"],
                    username=self.current_user["username"],
                    role=self.current_user["role"],
                ).unpark_vehicle()
            elif option == 4:
                parking_record.ParkingRecord(
                    user_id=self.current_user["user_id"],
                    username=self.current_user["username"],
                    role=self.current_user["role"],
                ).parking_history()
            elif option == 5:
                self.current_user = None
                self.welcome_page()
                break
