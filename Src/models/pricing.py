from src.utils.db import OpenDb
from src.system import System
from src.dbutils import DbConfig
import sys

class Pricing:
    """
    This is menu for pricing
    """

    def display_menu(self):
        print(System.DISPLAY_MENU)
        while True:
            try:
                option = int(input("Enter (1/2/3): "))
                if option in [1, 2, 3]:
                    return option
                print(System.INVALID_OPTION)
            except ValueError:
                print("Invalid input! Please enter a number.")
            except KeyboardInterrupt:
                print(System.EXITING)
                sys.exit(0)

    """
    This will set the valid of price
    """

    def set_price(self):
        vehicle_types = {1: "4-wheeler", 2: "2-wheeler"}

        while True:
            option = self.display_menu()
            if option == 3:
                print("Returning to main menu.")
                return

            vehicle_type = vehicle_types[option]
            price = self.get_price_input(vehicle_type)

            self.update_price_in_db(vehicle_type, price)
            print(f"Price for {vehicle_type} updated successfully!")

    """
    THis to get price input
    """

    def get_price_input(self, vehicle_type):
        while True:
            price = input(f"Enter the price per hour for {vehicle_type}: ").strip()
            if price.replace(".", "", 1).isdigit():
                return float(price)
            print(System.INVALID_OPTION)

    """
    This will update date in db
    """

    def update_price_in_db(self, vehicle_type, price):
        with OpenDb() as cursor:
            cursor.execute(
                DbConfig.UPDATE_PRICE_IN_DB,(vehicle_type, price, price),
            )

    """
    this will help in getting price
    """

    def get_price(self, vehicle_type):
        with OpenDb() as cursor:
            cursor.execute(
                DbConfig.GET_PRICE,(vehicle_type,),
            )
            result = cursor.fetchone()
        if result:
            return result[0]  # Returning only the price value
        else:
            print(f"No pricing data found for {vehicle_type}.")
            return None
