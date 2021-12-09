import csv
import pandas as pd
import datetime
import admin
import user


if __name__ == "__main__":
    admin = admin.ADMIN()
    user = user.USER()
    press_key_list = {"A": "ADMIN", "U": "USER", "Q": "Quit"}
    key_press = False
    while not (key_press == "q"):
        print(f"\n----------ACCOUNT MANAGEMENT SYSTEM---------\n")
        for key, value in press_key_list.items():
            print(f"PRESS {key} TO {value}\n")
        key_press = input("Press Key : ").lower()
        if key_press == "a":
            print("\n-----------ADMIN-----------\n")
            press_key_list_2 = {"C": "CREATE ACCOUNT", "S": "SHOW DETAILS", "F": "FREEZE ACCOUNT",
                                "D": "DELETE ACCOUNT",
                                "T": "SET TRANSACTION LIMIT", "H": "SHOW TRANSACTIONS", "Q": "QUIT"}
            key_press_2 = False
            for key, value in press_key_list_2.items():
                print(f"PRESS {key} TO {value}\n")
            print(f"\n---------------------------------------\n")
            key_press_2 = input("Press Key : ").lower()
            if key_press_2 == 'c':
                print("\nCREATE USER\n")
                admin.create_user()

            elif key_press_2 == 's':
                print("\nUSER  DETAILS\n")
                admin.show_details()

            elif key_press_2 == 't':
                print("\nSHOW ALL TRANSACTIONS\n")

            elif key_press_2 == 'f':
                print("\nFREEZE ACCOUNT.\n")
                admin.freeze_acount()

            elif key_press_2 == 'd':
                print("\nDELETE ACCOUNT.\n")
                admin.delete_account()

            elif key_press_2 == 't':
                print("\n SET TRANSACTION LIMIT.\n")
                admin.set_limit()
            elif key_press_2 == 'h':
                print("\nSHOW TRANSACTIONS\n")
                admin.show_transactions()

            elif key_press_2 == 'q':
                break
            else:
                print("WRONG INPUT")
                continue

        elif key_press == "u":
            print("\nPLEASE ENTER ACOUNT NUMBER & PIN. \n")
            user.user_login()
            press_key_list_3 = {"C": "CHECK BALANCE", "D": "DEPOSIT AMOUNT", "S": "SET PIN", "W": "WITHDRAW",
                                "T": "TRANSFER AMOUNT", "H": "TRANSACTION HISTORY", "Q": "QUIT"}
            key_press_3 = False
            for key, value in press_key_list_3.items():
                print(f"PRESS {key} TO {value}")
            print(f"\n---------------------------------------\n")

            key_press_3 = input("Press Key : ").lower()
            if key_press_3 == 'c':
                user.check_balance()

            elif key_press_3 == 'd':
                user.depositamount()

            elif key_press_3 == 'w':
                user.withdraw()

            elif key_press_3 == 's':
                user.setPin()

            elif key_press_3 == 't':
                user.transfer_amount()

            elif key_press_3 == 'h':
                user.transaction_history()

            elif key_press_3 == 'q':
                break

            else:
                print("WRONG INPUT")
                continue


        elif key_press == "q":
            break
        else:
            continue
