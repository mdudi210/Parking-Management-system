# To get started with this project you need to follow following steps:

- Step1:
    - Install Python3.13.2 --> https://www.python.org/downloads/
    - To Setup Python --> https://docs.python.org/3/using/index.html

- Step2:
    - Create Virtual Environment
        - {For Windows}
            - python -m venv venv
            - Set-ExecutionPolicy Unrestricted -Scope Process
            - venv\Scripts\Activate.ps1 
        - {For Mac}
            - python -m venv venv
            - Source .venv\Scripts\Activate.ps1

- Step3:
    - Upgrade the pip version
        - python.exe -m pip install --upgrade pip
    - Install all the dependencies from requirement.txt
    - {For mac/windows}
        - pip install -r requirement.txt

- Step4:
    - Install mysql Workbench from Official website
    - check this link to download mysql Workbench --> https://dev.mysql.com/downloads/workbench/
    - steps to download and setup mysql account --> https://dev.mysql.com/doc/workbench/en/wb-installing.html

- Step5:
    - Navigate to assets
    - open config.py and change following Variables according to your's
        - HOST = "###########" if running locally then "localhost" else your database-server "link" 
        - USER = "###########" your mysql username
        - PASSWORD = "#######" your mysql password
        - DATABASE = "#######" your Database name

- Step6:
    - Navigate to database/scripts
    {This will create your Database}
    - Run Command [python create_db.py] 
    
- Step7:
    - Run Command [python -m src.app.py]

# Flow of project

- This is default Costumer in our Database
    Welcome to WatchGuard Parking
    Enter your User Name: user
    Enter your Password: user123 
    Login successful!

    Welcome User, please select an option:
                    1. View Available Parking Slots
                    2. Park Vehicle
                    3. Unpark Vehicle
                    4. View Parking History
                    5. Log Out
    Enter your option:

- This is default admin in our Database
    Enter your User Name: admin
    Enter your Password: admin123
    Login successful!

    Welcome Admin, please select an option:
                    1. Add User
                    2. Manage Parking Slots
                    3. Set Pricing Rates
                    4. View Income (Daily/Monthly)
                    5. View Total Income per Vehicle
                    6. Log Out
    Enter your option: