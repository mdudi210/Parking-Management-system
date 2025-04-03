class DbConfig:
    LOGIN_INSERT = "SELECT user_id,username, password,role FROM users WHERE username=%s"
    CHECK_EXISTING_USER = "SELECT username FROM users WHERE username=%s"
    ADD_USER_TO_DB = "INSERT INTO Users(username, password, role) VALUES (%s, %s, %s)"
    UNASSIGN_SLOT = "UPDATE ParkingSlots SET is_occupied = FALSE WHERE slot_id = %s"
    ASSIGN_SLOT = "SELECT slot_id FROM ParkingSlots WHERE slot_type = %s AND is_occupied = 0 LIMIT 1"
    UPDATE_SLOT_IN_DB = "UPDATE ParkingSlots SET is_occupied = 1 WHERE slot_id = %s"
    GET_AVAILABLE_SLOT = "SELECT slot_id, slot_type FROM ParkingSlots WHERE is_occupied = False"
    REMOVE_SLOT = "SELECT slot_id, slot_type, is_occupied FROM ParkingSlots"
    DELETE_SLOT = "DELETE FROM ParkingSlots WHERE slot_id = %s"
    ADD_SLOT = "INSERT INTO ParkingSlots (slot_type) VALUES (%s)"
    UPDATE_PRICE_IN_DB = """INSERT INTO Pricing (vehicle_type, rate_per_hour) 
    VALUES (%s, %s) ON DUPLICATE KEY UPDATE rate_per_hour = %s"""
    GET_PRICE = "SELECT rate_per_hour FROM Pricing WHERE vehicle_type = %s"
    VIEW_DAILY_INCOME = """SELECT SUM(parking_fee) FROM ParkingRecords
    WHERE DATE(entry_time) = %s;"""
    VIEW_MONTHLY_INCOME = """SELECT SUM(parking_fee) FROM ParkingRecords
    WHERE DATE_FORMAT(entry_time, '%Y-%m') = %s;"""
    GET_VEHICLES = "SELECT vehicle_id, vehicle_number FROM Vehicles"
    GET_INCOME_PER_VEHICLE = "SELECT SUM(parking_fee) FROM ParkingRecords WHERE vehicle_id = %s"
    PARKING_HISTORY  = """SELECT Vehicles.vehicle_number, ParkingRecords.entry_time,
    PArkingRecords.exit_time, ParkingRecords.parking_fee
    FROM ParkingRecords JOIN Vehicles ON ParkingRecords.vehicle_id = Vehicles.vehicle_id
    WHERE Vehicles.user_id = %s 
    ORDER BY ParkingRecords.entry_time DESC"""
    CHECK_PARKING = """SELECT record_id, slot_id, entry_time FROM ParkingRecords
    WHERE vehicle_id = %s AND exit_time IS NULL"""
    UPDATE_ENTRY_TIME = "INSERT INTO ParkingRecords (vehicle_id, slot_id, entry_time) VALUES (%s, %s, %s)"
    GET_ENTRY_TIME = """SELECT pr.entry_time, v.vehicle_type
    FROM ParkingRecords pr
    JOIN Vehicles v ON pr.vehicle_id = v.vehicle_id
    WHERE v.vehicle_number = %s AND pr.exit_time IS NULL"""
    GET_VEHICLES_ID = """SELECT vehicle_id FROM Vehicles 
    WHERE vehicle_number = %s AND user_id = %s AND Vehicle_type = %s"""
    GET_PARKING_RECORD = """SELECT record_id, slot_id, entry_time FROM ParkingRecords 
    WHERE vehicle_id = %s AND exit_time IS NULL"""
    FETCH_PRICE = """SELECT rate_per_hour FROM Pricing 
    WHERE vehicle_type = (SELECT vehicle_type FROM Vehicles WHERE vehicle_id = %s)"""
    UPDATE_PARKING_RECORD = """UPDATE ParkingRecords 
    SET exit_time = %s, parking_fee = %s 
    WHERE record_id = %s"""