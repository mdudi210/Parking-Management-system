from Src.utils import db
from Src.models import user, pricing, parking_slot, parking_record


class ParkingSystem:
    def __init__(self):
        self.current_user = None

    def welcome_page(self):
        print("Welcome to WatchGuard Parking")

        while True:
            username = input("Enter your User Name: ").strip()
            password = input("Enter your Password: ")

            auth = user.User(username=username, password=password).login()
            if not auth:
                print("\n** Username or Password is incorrect. Please try again. **\n")
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
            print("Something went wrong.")

    def get_option(self, menu_options):
        while True:
            try:
                option = int(input("Enter Your Option: "))
                if option in menu_options:
                    return option
                print("Invalid option. Please try again.")
            except ValueError:
                print("Input must be an integer.")

    def admin_menu(self):
        """Admin menu options."""
        while True:
            print(
                """\nWelcome Admin, please select an option:
                1. Add User
                2. Manage Parking Slots
                3. Set Pricing Rates
                4. View Income (Daily/Monthly)
                5. View Total Income per Vehicle
                6. Log Out"""
            )
            option = self.get_option({1, 2, 3, 4, 5, 6})

            if option == 1:
                user.User().add_user()
            elif option == 2:
                parking_slot.ParkingSlot().manage_slot()
            elif option == 3:
                pricing.Pricing().set_price()
            elif option == 4:
                # Implement view income functionality
                pass
            elif option == 5:
                # Implement total income per vehicle
                pass
            elif option == 6:
                self.current_user = None
                self.welcome_page()
                break

    def customer_menu(self):
        """Customer menu options."""
        while True:
            print(
                """\nWelcome User, please select an option:
                1. View Available Parking Slots
                2. Park Vehicle
                3. Unpark Vehicle
                4. View Parking History
                5. Log Out"""
            )
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
