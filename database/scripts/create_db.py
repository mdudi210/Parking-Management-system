import mysql.connector
import hashlib
from assests.config import Config

# Connect to MySQL Server (without specifying a database)
conn = mysql.connector.connect(
    host=Config.HOST,
    user=Config.USER,
    password=Config.PASSWORD,
)

cursor = conn.cursor()

# Creating Database
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DATABASE}")
print("Database created successfully!")

# Going into Database
cursor.execute(f"use {Config.DATABASE}")
print("Using your database!")

# Creating Users table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Roles(
        role_id INT PRIMARY KEY,
        role_type VARCHAR(100) NOT NULL
        )
"""
)
print("Roles table created!")

# Creating Users table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Users(
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL,
        role INT,
        FOREIGN KEY (role) REFERENCES Roles(role_id)
        )
"""
)
print("Users table created!")


# Creating Vehicles table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Vehicles(
        vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
        vehicle_number VARCHAR(50) NOT NULL,
        owner_name VARCHAR(100) NOT NULL,
        vehicle_type VARCHAR(50) NOT NULL,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES Users(user_id)
        )
"""
)
print("Vehicles table created!")

# Creating Pricing table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Pricing (
        vehicle_type VARCHAR(50) PRIMARY KEY,
        rate_per_hour DECIMAL(5,2) NOT NULL
        )
"""
)
print("Pricing table created!")

# Creating ParkingSlots table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ParkingSlots (
        slot_id INT AUTO_INCREMENT PRIMARY KEY,
        slot_type VARCHAR(50) NOT NULL,
        is_occupied BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (slot_type) REFERENCES Pricing(vehicle_type)
        )
"""
)
print("ParkingSlots table created!")


# Creating ParkingRecords table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS ParkingRecords (
        record_id INT AUTO_INCREMENT PRIMARY KEY,
        vehicle_id INT,
        slot_id INT,
        entry_time DATETIME DEFAULT CURRENT_TIMESTAMP,
        exit_time DATETIME,
        parking_fee DECIMAL(10,2),
        FOREIGN KEY (vehicle_id) REFERENCES Vehicles(vehicle_id),
        FOREIGN KEY (slot_id) REFERENCES ParkingSlots(slot_id)
        )
"""
)
print("ParkingRecords table created!")


# Creating IncomeRecords table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS IncomeRecords (
        income_id INT AUTO_INCREMENT PRIMARY KEY,
        income_date DATE NOT NULL,
        total_income DECIMAL(10,2)
        )
"""
)
print("IncomeRecords table created!")


# Adding Default Users
cursor.execute(
    """
    INSERT INTO Roles(role_id,role_type) VALUES (%s,%s)
""",
    (1, "admin"),
)
cursor.execute(
    """
    INSERT INTO Roles(role_id,role_type) VALUES (%s,%s)
""",
    (2, "user"),
)
print(
    """
    Default Roles are:
      {
      admin : 1
      user : 2
      }
"""
)

# Adding Default Users
cursor.execute(
    """
    INSERT INTO Users(username,password,role) VALUES (%s,%s,%s)
""",
    ("admin", hashlib.sha512("admin123".encode("utf-8")).hexdigest(), 1),
)
cursor.execute(
    """
    INSERT INTO Users(username,password,role) VALUES (%s,%s,%s)
""",
    ("user", hashlib.sha512("user123".encode("utf-8")).hexdigest(), 2),
)
print(
    """
    Default Users are:
      {
      1 : { username : 'admin'
      password : 'admin123' }
      2 : { username : 'user'
      password : 'user123' }
      }
"""
)

cursor.execute("""DELIMITER $$

CREATE PROCEDURE GetParkingHistory(IN userId INT)
BEGIN
    SELECT Vehicles.vehicle_number, 
           ParkingRecords.entry_time,
           ParkingRecords.exit_time, 
           ParkingRecords.parking_fee
    FROM ParkingRecords
    JOIN Vehicles ON ParkingRecords.vehicle_id = Vehicles.vehicle_id
    WHERE Vehicles.user_id = userId
    ORDER BY ParkingRecords.entry_time DESC;
END$$

DELIMITER ;""")


# Committing changes
conn.commit()
# Closing connection
conn.close()
