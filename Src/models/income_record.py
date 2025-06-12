from src.utils import db
from datetime import datetime
from src.dbutils import DbConfig
from src.system import System
import sys

class IncomeRecord:
    @staticmethod
    def view_income():
        """View income for daily or monthly basis."""
        print(System.INCOME_MENU)       
        try:
            option = int(input(f"\n{System.ENTER_OPTION} (1/2): "))
            if option == 1:
                IncomeRecord.view_daily_income()
            elif option == 2:
                IncomeRecord.view_monthly_income()
            else:
                print(System.INVALID_OPTION)
        except ValueError:
            print(System.INVALID_OPTION)
        except KeyboardInterrupt:
            print(System.EXITING)
            sys.exit(0)


    @staticmethod
    def view_daily_income():
        """View total income for the current day."""
        current_date = datetime.now().strftime("%Y-%m-%d")

        # with db.OpenDb(DbConfig.VIEW_DAILY_INCOME,(current_date,),'fetchone') as data:
        #     daily_income = data
        #     if daily_income and daily_income[0] is not None:
        #         print(f"\nTotal Income for {current_date}: {daily_income[0]}")
        #     else:
        #         print(f"No income recorded for {current_date}.")
        with db.OpenDb() as cursor:
            # Query for daily income
            cursor.execute(
                DbConfig.VIEW_DAILY_INCOME, (current_date,)
                )
            daily_income = cursor.fetchone()
            if daily_income and daily_income[0] is not None:
                print(f"{System.TOTAL_INCOME} {current_date}: {daily_income[0]}")
            else:
                print(f"{System.NO_INCOME_RECORD} {current_date}.")


    @staticmethod
    def view_monthly_income():
        """View total income for the current month."""
        current_month = datetime.now().strftime("%Y-%m")
        # with db.OpenDb(DbConfig.VIEW_MONTHLY_INCOME,(current_month,),'fetchone') as data:
        #     monthly_income = data
            
        #     if monthly_income and monthly_income[0] is not None:
        #         print(f"\nTotal Income for {current_month}: {monthly_income[0]}")
        #     else:
        #         print(f"No income recorded for {current_month}.")
        with db.OpenDb() as cursor:
            # Query for monthly income
            cursor.execute(
                DbConfig.VIEW_MONTHLY_INCOME, (current_month,)
                )
            monthly_income = cursor.fetchone()
            
            if monthly_income and monthly_income[0] is not None:
                print(f"{System.TOTAL_INCOME} {current_month}: {monthly_income[0]}")
            else:
                print(f"{System.NO_INCOME_RECORD} {current_month}.")


    @staticmethod
    def view_total_income_per_vehicle():
        """View total income for a selected vehicle."""
        # with db.OpenDb(DbConfig.GET_VEHICLES,(),'fetchall') as data:
        #     vehicles = data
            
        #     if not vehicles:
        #         print(System.NO_VEHICLE_FOUND)
        #         return
        #     print(System.AVAILABLE_VEHICLES)
        #     for vehicle in vehicles:
        #         print(f"ID: {vehicle[0]} | Number: {vehicle[1]}")
                
        #     try:
        #         vehicle_id = int(input(System.ENTER_VEHICLE_ID))
        #     except ValueError:
        #         print("Invalid input. Please enter a valid Vehicle ID.")
        #         return
        with db.OpenDb() as cursor:
            # Fetch and display all vehicles
            cursor.execute(
                DbConfig.GET_VEHICLES
                )
            vehicles = cursor.fetchall()
            
            if not vehicles:
                print(System.NO_VEHICLE_FOUND)
                return
            print(System.AVAILABLE_VEHICLES)
            for vehicle in vehicles:
                print(f"ID: {vehicle[0]} | Number: {vehicle[1]}")
                
            try:
                vehicle_id = int(input(System.ENTER_VEHICLE_ID))
            except ValueError:
                print(System.INVALID_OPTION)
                return
            except KeyboardInterrupt:
                print(System.EXITING)
                sys.exit(0)
            
            # Fetch total income for the selected vehicle
        
        # with db.OpenDb(DbConfig.GET_INCOME_PER_VEHICLE,(vehicle_id,),'fetchone') as data:
            cursor.execute(
                DbConfig.GET_INCOME_PER_VEHICLE,(vehicle_id,)
                )
            income = cursor.fetchone()

            if income and income[0] is not None:
                print(f"{System.TOTAL_INCOME} Vehicle ID {vehicle_id}: {income[0]}")
            else:
                print(f"{System.NO_INCOME_RECORD} this vehicle.")