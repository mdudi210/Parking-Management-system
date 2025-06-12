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
            - source .venv\Scripts\activate

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

- This is default Costumer in our Database <br>
    Welcome to WatchGuard Parking <br>
    Enter your User Name: user <br>
    Enter your Password: user123 <br>
    Login successful! <br>

    Welcome User, please select an option: <br>
        1. View Available Parking Slots <br>
        2. Park Vehicle <br>
        3. Unpark Vehicle <br>
        4. View Parking History <br>
        5. Log Out <br>
    Enter your option: <br>

- This is default admin in our Database <br>
    Enter your User Name: admin <br>
    Enter your Password: admin123 <br>
    Login successful! <br>

    Welcome Admin, please select an option: <br>
        1. Add User <br>
        2. Manage Parking Slots <br>
        3. Set Pricing Rates <br>
        4. View Income (Daily/Monthly) <br>
        5. View Total Income per Vehicle <br>
        6. Log Out <br>
    Enter your option: <br>

**Change the folder's
 name if it's starting with Capital Character to Small Character**