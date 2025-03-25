from Src.utils.db import OpenDb


class ParkingSlot:
    def slot_type(self):
        print(
            """Slot type:
                1. 4-wheeler
                2. 2-wheeler
                3. Exit"""
        )
        try:
            slot_type = int(input())
            if slot_type < 1 or slot_type > 3:
                print("Wrong Input!")
        except ValueError:
            print("Wrong input!")
            self.slot_type()
        if slot_type == 1:
            return "4-wheeler"
        elif slot_type == 2:
            return "2-wheeler"
        else:
            self.manage_slot()

    def manage_slot_menu(self):
        print(
            """Managing Parking Slots:
            1. Add new slot
            2. remove slot
            3. Exit"""
        )

        try:
            option = int(input("Enter(1/2/3):- "))
            if option > 3 or option < 1:
                print("Wrong Input")
                self.manage_slot_menu()
        except ValueError:
            print("Wrong Input")
            self.manage_slot_menu()
        return option

    """
    
    """

    def manage_slot(self):
        option = self.manage_slot_menu()
        if option == 1:
            finall_slot_type = self.slot_type()
            if not finall_slot_type:
                self.manage_slot()
            else:
                finall_slot_type = self.slot_type()
            with OpenDb() as cursor:
                cursor.execute(
                    "INSERT INTO ParkingSlots(slot_type) VALUES (%s)", ("4-wheeler",)
                )
            print("4-wheeler slot added!")
            self.manage_slot()
        elif option == 2:
            self.manage_slot()
        else:
            return
