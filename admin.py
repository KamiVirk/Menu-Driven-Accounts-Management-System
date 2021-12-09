import csv
import pandas as pd
import datetime

class ADMIN:
    """
    This class is used to set and handle a user account.
    It has total total 6 modules create user, show details of user, show transactions, freeze account, set limit for
    user and delete account. 'File1.csv' should be text file for user data and 'File2.csv' for transaction history.
    """

    def __init__(self):
        pass

    # create USER
    def create_user(self):
        try:
            self.name = input("USER Name (Format 'kami' ) : ")
            self.account_number = int(input("USER Account number (Format '012345' ) : "))
            self.transaction_limit = int(input("Set transaction limit (Format '012345' ) : "))
            self.deposit_amount = int(input("Amount to be deposited (Format '012345' ) : "))
            self.pin = int(input("SET PIN FOR USER (Format '012345' ) : "))
        except ValueError:
            print("Invalid Input!Try again")
            self.create_user()
        self.user_data = {'Account Number': self.account_number, 'Name': self.name, 'Balance': self.deposit_amount,
                          'Transaction Limit': self.transaction_limit, 'pin': self.pin, 'Account Status': "ACTIVE"}
        self.found = False
        with open('File1.csv', 'r') as fr:
            reader = csv.reader(fr)
            for row in reader:
                if row[0] == str(self.account_number):
                    self.found = True
        fr.close()
        if self.found == False:
            with open('File1.csv', 'a', newline='') as file:
                field_name = ['Account Number', 'Name', 'Balance', 'Transaction Limit', 'pin', 'Account Status']
                self.infile = csv.DictWriter(file, fieldnames=field_name)
                self.infile.writerow(self.user_data)
            file.close()
            print(f"\nNEW USER '{self.name}' HAS BEEN ADDED.\n")
        else:
            print("THIS ACCOUNT EXISTS. PLEASE CHANGE ACCOUNT NUMBER.")
            self.create_user()

    # DETAILS OF USER
    def show_details(self):
        try:
            self.typeAccount = int(input("TYPE ACCOUNT NUMBER TO GET DETAILS : "))
        except ValueError:
            print("TYPE ERROR! TRY DIGIT")
        self.found_row = {}
        with open('File1.csv', 'r') as rf:
            self.readfile = csv.reader(rf)
            self.found_user = False
            for row in self.readfile:
                if row[0] == self.typeAccount:
                    self.found_user = True
                    self.found_row = {"Account Number": row[0], "Name": row[1], "Balance": row[2],
                                      "Transfer Limit": row[3], 'Account Status': row[5]}

            if self.found_user == False:
                print("\n----------INVALID CREDENTIALS.----------\n")
                self.show_details()
            else:
                print(f"\n|Account Number : {self.found_row['Account Number']} |"
                      f"|Name : {self.found_row['Name']} |"
                      f"|Balance : {self.found_row['Balance']} |"
                      f"|Transfer limit : {self.found_row['Transfer Limit']} |"
                      f"|Account Status : {self.found_row['Account Status']} |\n")

    # Show transaction details of Users
    def show_transactions(self):
        df = pd.read_csv("File2.csv")
        print(df)

    # Freeze Account
    def freeze_acount(self):
        self.acctF = input("ACCOUNT NUMBER : ")
        with open("File1.csv", 'r') as fs:
            reader = csv.reader(fs)
            self.user_info_4 = []
            self.found = False
            for row in reader:
                if row[0] == str(self.acctF):
                    self.found = True
                    try:
                        row[5] = str(input("PLEASE 'F' OR 'FREEZE' TO FREEZE ACCOUNT & 'ACTIVE' TO UNFREEZE : ").upper())
                    except ValueError:
                        print("Try Again!")

                self.user_info_4.append(row)
            fs.close()
            if self.found == True:
                with open('File1.csv', 'w', newline='') as fws:
                    filei = csv.writer(fws)
                    filei.writerows(self.user_info_4)
                    fws.close()
            else:
                print("\nENTER VALID ACCOUNT NUMMBER\n")

    # Set Limit For the user
    def set_limit(self):
        self.account = str(input("TYPE ACCOUNT NUMBER : "))
        with open("File1.csv", 'r') as fl:
            reader = csv.reader(fl)
            self.user_data_0 = []
            self.found = False
            for row in reader:
                if row[0] == self.account:
                    self.found = True
                    row[3] = str(input("TYPE TRANSACTION LIMIT : "))
                self.user_data_0.append(row)
            fl.close()
            if self.found == True:
                with open('File1.csv', 'w', newline='') as fsl:
                    filei = csv.writer(fsl)
                    filei.writerows(self.user_data_0)
                    fsl.close()
            else:
                print("RECORDS NOT FOUND!")

    # Delete account
    def delete_account(self):
        self.accountNumber = str(input("ENTER ACCOUNT NUMBER TO DELETE THE ACCOUNT : "))
        self.found = True
        with open('File1.csv', 'r') as File:
            reader = csv.reader(File)
            line = []
            for row in reader:
                if not row[0] == self.accountNumber:
                    line.append(row)
                else:
                    self.found = True
            File.close()
        if not self.found == False:
            with open('File1.csv', 'w', newline='') as writefile:
                writer = csv.writer(writefile)
                writer.writerows(line)
            writefile.close()
        else:
            print("\n RECORD NOT FOUND \n")

    """def reports(self):

        self.start_date = str(input("Enter FROM which date you want to check records : Format (YYYYMMDD) : "))
        self.to_date = str(input("Enter TO which date you want to check records : Format (YYYYMMDD) : "))
        if not len(self.start_date) == 8:
            print("INVALID INPUT")
        else:
            from_date = str(datetime.datetime.strptime(self.start_date, "%Y-%m-%d"))
            to_date = str(datetime.datetime.strptime(self.to_date, "%Y-%m-%d"))
            start_date = pd.to_datetime(from_date, utc=True)
            t_date = pd.to_datetime(to_date, utc=True)
            df = pd.read_csv('File2.csv')
            df2 = df.loc[(df['Date'] > start_date) & (df['Date'] < t_date)]
            print(df2)"""


