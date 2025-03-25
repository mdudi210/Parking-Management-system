from Src.utils.db import OpenDb


class Pricing:
    def __init__(self):
        pass

    def set_price_menu(self):
        print(
            """Set Pricing for Parking:
            1. 4-Wheeler - $? per hour
            2. 2-Wheeler - $? per hour
            3. Exit"""
        )
        try:
            option = int(input("Enter(1/2/3):- "))
            if option > 3 or option < 1:
                print("Wrong Input")
                self.set_price()
        except ValueError:
            print("Wrong Input")
            self.set_price()
        return option

    def set_price(self):
        option = self.set_price_menu()
        if option == 1:
            price = input("Enter the price you want to set:- ")
            with OpenDb() as cursor:

                """
                            ON DUPLICATE KEY UPDATE
                column1 = value1, column2 = value2, ...;
                """
                cursor.execute(
                    """INSERT INTO Pricing(vehicle_type,rate_per_hour) VALUES(%s,%s) ON DUPLICATE KEY UPDATE rate_per_hour=%s""",
                    ("4-wheeler", price, price),
                )
                print("Price updated...!")
            self.set_price()
        elif option == 2:
            price = input("Enter the price you want to set:- ")
            with OpenDb() as cursor:
                cursor.execute(
                    """INSERT INTO Pricing(vehicle_type,rate_per_hour) VALUES(%s,%s) ON DUPLICATE KEY UPDATE rate_per_hour=%s""",
                    ("2-wheeler", price, price),
                )
                print("Price updated...!")
            self.set_price()
        else:
            return

    def get_price():
        pass


# Pricing().set_price()
