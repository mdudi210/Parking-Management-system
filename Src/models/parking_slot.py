from Src.utils.db import OpenDb


class ParkingSlot:
    """
    This to unassign slot to vehilce
    """

    def unassign_slot(self, slot_id):
        # Update in ParkingSlots table
        with OpenDb() as cursor:
            cursor.execute(
                "UPDATE ParkingSlots SET is_occupied = FALSE WHERE slot_id = %s",
                (slot_id,),
            )
            print(f"Slot {slot_id} is now available.")

    """
    This to assign slot to vehilce
    """

    def assign_slot(vehicle_type):
        # fetching slot_id to assign slot
        with OpenDb() as cursor:
            cursor.execute(
                "SELECT slot_id FROM ParkingSlots WHERE slot_type = %s AND is_occupied = 0 LIMIT 1",
                (vehicle_type,),
            )
            slot = cursor.fetchone()
            if slot:
                slot_id = slot[0]
                # Updating ParkingSlots table for occupied slot
                cursor.execute(
                    "UPDATE ParkingSlots SET is_occupied = 1 WHERE slot_id = %s",
                    (slot_id,),
                )
                return slot_id
            else:
                # No available slots
                return None

    """

    this shows available slots
    """

    @staticmethod
    def get_available_slots():
        # fetch from parkingslots to see available slots
        with OpenDb() as cursor:
            cursor.execute(
                "SELECT slot_id, slot_type FROM ParkingSlots WHERE is_occupied = False"
            )
            slots = cursor.fetchall()
        return slots if slots else None

    def is_available_slots(self):
        # getting available slots list of list
        slots = ParkingSlot.get_available_slots()
        if not slots:
            print("No parking slots available at the moment.")
            return
        print("\nAvailable Parking Slots:")
        for slot in slots:
            print(f"  - Slot #{slot[0]} ({slot[1]})")

    """
    
    This will used to get slot type for vehicles to update slots count or to update price (helpping function) 
    """

    def get_slot_type(self):

        while True:
            print(
                """Slot type:
                1. 4-wheeler
                2. 2-wheeler
                3. Exit"""
            )
            try:
                slot_type = int(input("Enter slot type (1/2/3): "))
                if slot_type == 1:
                    return "4-wheeler"
                elif slot_type == 2:
                    return "2-wheeler"
                elif slot_type == 3:
                    return None  # Exit
                else:
                    print("Invalid input! Please enter a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    """

    This is the menu to add or remove slot type
    """

    def manage_slot_menu(self):
        """Displays and handles parking slot management menu selection."""
        while True:
            print(
                """Managing Parking Slots:
                1. Add new slot
                2. Remove slot
                3. Exit"""
            )
            try:
                option = int(input("Enter (1/2/3): "))
                if option in [1, 2, 3]:
                    return option
                print("Invalid input! Please enter a valid option.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    """

    This will slot the slot from DB 

    **Here if slot is occupied then that slot will be removed and i need to add that case in my code**
    """

    def remove_slot(self):
        # Fetching from ParkingSlots
        with OpenDb() as cursor:
            cursor.execute("SELECT slot_id, slot_type FROM ParkingSlots")
            slots = cursor.fetchall()

            # no slots available then
            if not slots:
                print("No slots available to remove.")
                return

            # to choose which slot you need to delete
            print("Available Slots:")
            for slot in slots:
                print(f"ID: {slot[0]}, Type: {slot[1]}")

            try:
                slot_id = int(input("Enter Slot ID to remove: "))
                # Deleteing slot from ParkingSlots
                cursor.execute(
                    "DELETE FROM ParkingSlots WHERE slot_id = %s", (slot_id,)
                )
                if cursor.rowcount > 0:
                    print(f"Slot ID {slot_id} removed successfully!")
                else:
                    print(f"Slot ID {slot_id} not found.")
            except ValueError:
                print("Invalid input. Please enter a valid slot ID.")

    """

    THis will Add the slot in the DB

    """

    def add_slot(self):
        slot_type = self.get_slot_type()
        if not slot_type:
            print("Returning to main menu.")
            return
        with OpenDb() as cursor:
            cursor.execute(
                "INSERT INTO ParkingSlots (slot_type) VALUES (%s)", (slot_type,)
            )
        print(f"{slot_type} slot added successfully!")

    """

    This for manageing slots 
    Adding and removing slots

    """

    def manage_slot(self):
        while True:
            option = self.manage_slot_menu()
            if option == 1:
                # Adding slot
                self.add_slot()
            elif option == 2:
                # Removeing slot
                self.remove_slot()
            else:
                # Exit
                return
