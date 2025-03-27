from src.utils.db import OpenDb


class VehicleRegister:
    @staticmethod
    def get_user_id(username):
        """Fetch user_id from Users table using username."""
        with OpenDb() as cursor:
            cursor.execute("SELECT user_id FROM Users WHERE username = %s", (username,))
            user = cursor.fetchone()
            return user[0] if user else None

    @staticmethod
    def register(vehicle_number, owner_name, vehicle_type, user_id):
        """Registers a vehicle if not found in the database and returns vehicle_id."""
        with OpenDb() as cursor:

            # Checking if vehicle is already in the db
            cursor.execute(
                "SELECT vehicle_id,user_id FROM Vehicles WHERE vehicle_number = %s AND vehicle_type = %s",
                (vehicle_number, vehicle_type),
            )
            vehicle = cursor.fetchall()

            if vehicle:
                print(f"Vehicle {vehicle_number} already registered.")
                return vehicle[0]  # Return existing vehicle_id
            else:

                # Adding new user to bd
                cursor.execute(
                    "INSERT INTO Vehicles (vehicle_number, owner_name, vehicle_type, user_id) VALUES (%s, %s, %s, %s)",
                    (vehicle_number, owner_name, vehicle_type, user_id),
                )
                print(
                    f"Vehicle {vehicle_type}: {vehicle_number} registered successfully."
                )
                # Get the last inserted vehicle_id
                return cursor.lastrowid, user_id
