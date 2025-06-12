class System:
    WELCOME = "Welcome to WatchGuard Parking"
    SOMETHING_WRONG = "Something went wrong."
    ADMIN_MENU = """\nWelcome Admin, please select an option:
                1. Add User
                2. Manage Parking Slots
                3. Set Pricing Rates
                4. View Income (Daily/Monthly)
                5. View Total Income per Vehicle
                6. Log Out"""
    CUSTOMER_MENU = """\nWelcome User, please select an option:
                1. View Available Parking Slots
                2. Park Vehicle
                3. Unpark Vehicle
                4. View Parking History
                5. Log Out"""
    GET_SLOT_TYPE = """Slot type:
                1. 4-wheeler
                2. 2-wheeler
                3. Exit"""
    MANAGE_SLOT_MENU = """Managing Parking Slots:
                1. Add new slot
                2. Remove slot
                3. Exit"""
    DISPLAY_MENU = """Set Pricing for Parking:
            1. 4-Wheeler - ₹? per hour
            2. 2-Wheeler - ₹? per hour
            3. Exit"""
    ADD_USER = """ADD USER
                1. Add User
                2. Exit"""
    INCOME_MENU = """\nChoose the income view option:
    1. Daily Income
    2. Monthly Income
    """
    ENTER_OPTION = "Enter your option"
    ENTER_NAME = "Enter your User Name: "
    ENTER_PASSWORD = "Enter your Password: "
    INVALID_OPTION = "Invalid input! Please enter a valid option."
    INVALID_USER_PASSWORD = "\n** Username or Password is incorrect. Please try again. **\n"
    MUST_INTEGER = "Input must be an integer."
    NO_INCOME_RECORD = "No income recorded for"
    TOTAL_INCOME = "\nTotal Income for"
    EXITING = "\nYou had pressed ctrl+C bye..!!"
    NO_VEHICLE_FOUND = "No vehicles found in the system."
    ENTER_VEHICLE_ID = "\nEnter Vehicle ID to view income: "
    AVAILABLE_VEHICLES = "\nAvailable Vehicles:"
    NO_PARKING_HISTORY = "No parking history found for this user!"
    INVALID_VEHICLE_TYPE = "Invalid vehicle type. Please enter 'Car' or 'Bike'."
