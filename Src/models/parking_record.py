from datetime import datetime
from src.utils.db import OpenDb
from src.models.vehicle_register import VehicleRegister
from src.models.parking_slot import ParkingSlot


class ParkingRecord:
    """
    To maintain session for users
    """

    def __init__(self, user_id=0, username="", password="", role=None):
        self.user_id = user_id
        self.username = username.strip()
        self.password = password
        self.role = role

    """
    This is for history of parking
    """

    def parking_history(self):
        with OpenDb() as cursor:
            # Fetching parking records for vehicles owned by this user
            cursor.execute(
                # """SELECT V.vehicle_number, PR.entry_time,
                # PR.exit_time, PR.parking_fee
                #    FROM ParkingRecords PR
                #    JOIN Vehicles V ON PR.vehicle_id = V.vehicle_id
                #    WHERE V.user_id = %s
                #    ORDER BY PR.entry_time DESC""",
                """SELECT Vehicles.vehicle_number, ParkingRecords.entry_time,
                PArkingRecords.exit_time, ParkingRecords.parking_fee
                FROM ParkingRecords JOIN Vehicles ON
                ParkingRecords.vehicle_id = Vehicles.vehicle_id
                WHERE Vehicles.user_id = %s
                ORDER BY ParkingRecords.entry_time DESC""",
                (self.user_id,),
            )
            records = cursor.fetchall()

            if not records:
                print("No parking history found for this user!")
                return

            # Displaying Parking History
            print("\nParking History:")
            print("-" * 90)
            print(
                f"{'Vehicle Number':<20}{'Entry Time':<25} \
                {'Exit Time':<25}{'Fee':<20}"
            )
            print("-" * 90)

            for record in records:
                vehicle_number, entry_time, exit_time, fee = record
                exit_time_str = exit_time if exit_time else "Still Parked"
                fee_str = f"${fee:.2f}" if fee is not None else "N/A"
                print(
                    f"{vehicle_number:<20}{str(entry_time):<25} \
                    {str(exit_time_str):<25}{fee_str:<20}"
                )

            print("-" * 90)

    """
    This is for parking the vehicle
    """

    def park_vehicle(self):
        # Taking info for parking a vehicle
        vehicle_number = input("Enter Vehicle Number: ").strip()
        owner_name = input("Enter Owner Name: ").strip()
        vehicle_type = input("Enter Vehicle Type (Car/Bike): ").strip().lower()

        if vehicle_type not in ["car", "bike"]:
            print("Invalid vehicle type. Please enter 'Car' or 'Bike'.")
            return False

        # Mapping of vehicle and vehicle type
        vehicle_type_mapping = {"car": "4-wheeler", "bike": "2-wheeler"}

        # Convert input to vehicle type in database
        vehicle_type_db = vehicle_type_mapping.get(vehicle_type)

        if not vehicle_type_db:
            # Return None for invalid input
            print("Invalid vehicle type. Please enter 'Car' or 'Bike'.")
            return None

        # Register vehicle (or get existing one)
        vehicle_id, user_id = VehicleRegister.register(
            vehicle_number, owner_name, vehicle_type_db, self.user_id
        )

        # if vehicle is registered with different user then
        if user_id != self.user_id:
            print(
                f"This vehicle is registered with \
                    different user you can't park this"
            )
            return None

        # if vehicle is already parked then what?
        with OpenDb() as cursor:
            cursor.execute(
                """SELECT record_id, slot_id, entry_time FROM ParkingRecords
                    WHERE vehicle_id = %s AND exit_time IS NULL""",
                (vehicle_id,),
            )
            parking_record = cursor.fetchone()
            print(parking_record)

            if parking_record:
                print("vehicle is already parked...!!")
                return

        # Assign a parking slot
        slot_id = ParkingSlot.assign_slot(vehicle_type_db)
        if not slot_id:
            print("No available parking slots for this vehicle type.")
            return False

        # Update time in DB for entry time
        entry_time = datetime.now()
        with OpenDb() as cursor:
            cursor.execute(
                """INSERT INTO ParkingRecords (vehicle_id, slot_id, entry_time)"
                VALUES (%s, %s, %s)""",
                (vehicle_id, slot_id, entry_time),
            )

        print(
            f"Vehicle successfully parked! Entry Time:\
                {entry_time.strftime('%I:%M %p')}"
        )
        return True

    """
    
    TO calculate fee for parking

    """

    @staticmethod
    def calculate_fee(vehicle_number):
        with OpenDb() as cursor:
            # Getting entry time and vehicle type
            cursor.execute(
                """
                SELECT pr.entry_time, v.vehicle_type
                FROM ParkingRecords pr
                JOIN Vehicles v ON pr.vehicle_id = v.vehicle_id
                WHERE v.vehicle_number = %s AND pr.exit_time IS NULL
            """,
                (vehicle_number,),
            )
            record = cursor.fetchone()

            if not record:
                print("No active parking record found for this vehicle.")
                return None

            entry_time, vehicle_type = record
            exit_time = datetime.now()
            # Charging at least for one hour
            hours_parked = max(1, (exit_time - entry_time).total_seconds() / 3600)

            # Getting pricing for per hour
            cursor.execute(
                "SELECT rate_per_hour FROM Pricing WHERE vehicle_type = %s",
                (vehicle_type,),
            )
            rate = cursor.fetchone()

            if not rate:
                print("Pricing not found for this vehicle type.")
                return None

            rate_per_hour = rate[0]
            total_fee = round(hours_parked * rate_per_hour, 2)

            return entry_time, exit_time, total_fee

    # @staticmethod
    def unpark_vehicle(self):
        vehicle_number = input("Enter your vehicle number to unpark: ").strip()
        """
        
        need to implement auth for 
        
        """
        vehicle_type = input("Enter Vehicle Type (Car/Bike): ").strip().lower()

        if vehicle_type not in ["car", "bike"]:
            print("Invalid vehicle type. Please enter 'Car' or 'Bike'.")
            return False

        # Map user input to database values
        vehicle_type_mapping = {"car": "4-wheeler", "bike": "2-wheeler"}

        # Convert input to correct database format
        vehicle_type_db = vehicle_type_mapping.get(vehicle_type)
        if not vehicle_type_db:
            print("Invalid vehicle type. Please enter 'Car' or 'Bike'.")
            return None  # Return None for invalid input

        # print(self.user_id, self.username, self.role)

        with OpenDb() as cursor:
            # Getting vehicle_id from the Vehicles table
            cursor.execute(
                "SELECT vehicle_id FROM Vehicles WHERE vehicle_number = %s AND user_id = %s AND Vehicle_type = %s",
                (vehicle_number, self.user_id, vehicle_type_db),
            )
            vehicle = cursor.fetchone()

            if not vehicle:
                print("Vehicle not found in records!")
                return

            vehicle_id = vehicle[0]

            # Getting parking record for the vehicle
            cursor.execute(
                """SELECT record_id, slot_id, entry_time FROM ParkingRecords 
                   WHERE vehicle_id = %s AND exit_time IS NULL""",
                (vehicle_id,),
            )
            parking_record = cursor.fetchone()

            if not parking_record:
                print("No active parking record found for this vehicle!")
                return

            record_id, slot_id, entry_time = parking_record
            exit_time = datetime.now()

            # Fetching the pricing rate
            cursor.execute(
                """SELECT rate_per_hour FROM Pricing 
                   WHERE vehicle_type = (SELECT vehicle_type FROM Vehicles WHERE vehicle_id = %s)""",
                (vehicle_id,),
            )
            price_data = cursor.fetchone()

            if not price_data:
                print("Pricing information not found!")
                return

            rate_per_hour = price_data[0]

            # Calculating the total fee
            total_hours = max(
                1, (exit_time - entry_time).seconds // 3600
            )  # Round up to at least 1 hour
            parking_fee = total_hours * rate_per_hour

            # Update ParkingRecords table with exit time and fee
            cursor.execute(
                """UPDATE ParkingRecords 
                   SET exit_time = %s, parking_fee = %s 
                   WHERE record_id = %s""",
                (exit_time, parking_fee, record_id),
            )

            # To free up slot where vehicle is parked
            ParkingSlot().unassign_slot(slot_id)

            print(f"Vehicle {vehicle_number} exited! Parking Fee: ${parking_fee:.2f}")
