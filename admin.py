import csv
import pandas as pd

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
        self.name = input("USER Name : ")
        self.account_number = int(input("USER Account number : "))
        self.transaction_limit = int(input("Set transaction limit : "))
        self.deposit_amount = int(input("Amount to be deposited : "))
        self.pin = int(input("SET PIN FOR USER : "))
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
        self.typeAccount = str(input("TYPE ACCOUNT NUMBER TO GET DETAILS : "))
        self.found_row = {}
        with open('File1.csv', 'r') as rf:
            self.readfile = csv.reader(rf)
            self.found_user = False
            for row in self.readfile:
                if row[0] == self.typeAccount:
                    self.found_user = True
                    self.found_row = {"Account Number": row[0], "Name": row[1], "Balance": row[2], "Transfer Limit": row[3], 'Account Status': row[5]}

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
                    row[5] = str(input("PLEASE 'F' OR 'FREEZE' TO FREEZE ACCOUNT & 'ACTIVE' TO UNFREEZE : ").upper())
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