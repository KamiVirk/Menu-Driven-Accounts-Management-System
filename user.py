import admin
import csv
import pandas as pd
import datetime


# class USER
class USER(admin.ADMIN):
    """
    This is a sub class of ADMIN class.
    It is consist of total six modules check balance, deposit amount, withdraw amount, set pin, transfer amount and show
    transaction history.
    """

    def __init__(self):
        pass

    # user login
    def user_login(self):
        self.typeAccNum = str(input("ENTER YOUR ACCOUNT NUMBER\t: "))
        self.pin = input("ENTER ACCOUNT PIN\t: ")
        self.user_info_1 = {}
        with open('File1.csv', 'r') as rf:
            file = csv.reader(rf)
            self.found_acount = False
            for row in file:
                if row[0] == self.typeAccNum and row[4] == self.pin:
                    self.found_acount = True
                    self.user_info_1 = {"Account Number": row[0], "Name": row[1], "Balance": row[2],
                                        "Transfer Limit": row[3], "pin": row[4], "Account Status": row[5]}
                    self.account_status = self.user_info_1['Account Status']
            rf.close()
            if self.found_acount == False:
                print("\n----------INVALID CREDENTIALS.----------\n")
                self.user_login()
            elif not self.account_status == "ACTIVE":
                print("\n----------ACCOUNT IS FREEZED.----------\n")
                self.user_login()
            else:
                print("\n----------SUCCESSFULLY LOGGED IN.----------\n")

    # check balance
    def check_balance(self):
        print(f"\n---------------------------------------\n")
        print(f"AVAILABLE BALANCE : {self.user_info_1['Balance']} Rs.")
        print(f"\n---------------------------------------\n")

    # File Update
    def update_balance(self, account_number, balance):
        self.account_num = account_number
        self.new_Balance = balance
        with open("File1.csv", 'r') as fs:
            reader = csv.reader(fs)
            self.user_info = []
            self.found = False
            for row in reader:
                if row[0] == self.account_num:
                    self.found = True
                    row[2] = str(self.new_Balance)
                self.user_info.append(row)
            fs.close()
            if self.found == True:
                with open('File1.csv', 'w', newline='') as fws:
                    filei = csv.writer(fws)
                    filei.writerows(self.user_info)
                    fws.close()

    def update_transaction_limit(self, account_number, tlimit):
        self.account_num = account_number
        self.new_tlimit = tlimit
        with open("File1.csv", 'r') as fs:
            reader = csv.reader(fs)
            self.user_info_9 = []
            found = False
            for row in reader:
                if row[0] == self.account_num:
                    found = True
                    row[3] = str(self.new_tlimit)
                self.user_info_9.append(row)
            fs.close()
            if found == True:
                with open('File1.csv', 'w', newline='') as fws:
                    filei = csv.writer(fws)
                    filei.writerows(self.user_info_9)
                    fws.close()

    def update_transaction(self, t_account, f_account, amount):
        self.account_1 = t_account
        self.account_2 = f_account
        self.amount = amount
        self.date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.time = datetime.datetime.now().strftime("%H:%M:%S")
        self.Transaction_data = {'Amount': self.amount, 'From Account': self.account_2,
                                 'To Account': self.account_1, 'Date': self.date, 'Time': self.time}
        with open('File2.csv', 'a', newline='') as file:
            field_name = ['Amount', 'From Account', 'To Account', 'Date', 'Time']
            self.infile = csv.DictWriter(file, fieldnames=field_name)
            self.infile.writerow(self.Transaction_data)
            file.close()

    # deposit amount
    def depositamount(self):
        self.available_balance = int(self.user_info_1['Balance'])
        self.deposit = int(input("ENTER AMOUNT TO BE DEPOSITED : "))
        self.new_balance = self.available_balance + self.deposit
        self.update_balance(self.user_info_1['Account Number'], self.new_balance)
        self.update_transaction(self.user_info_1['Account Number'], 'Deposited', self.deposit)

    # withdraw amount
    def withdraw(self):
        self.balance = int(self.user_info_1['Balance'])
        self.tlimit = int(self.user_info_1['Transfer Limit'])
        self.withdraw = int(input(" ENTER AMOUNT YOU WANT TO WITHDRAW \t: "))
        if self.balance >= self.withdraw:
            if self.tlimit >= self.withdraw:
                self.remaining = self.balance - self.withdraw
                self.tlimit_remaining = self.tlimit - self.withdraw
                print(f"\n------------------------------------------\n"
                      f"YOUR REMAINING BALANCE IS |{self.remaining} Rs.|"
                      f"\n------------------------------------------\n"
                      f"YOUR REMAINING TRANSACTION LIMIT IS |{self.tlimit_remaining} Rs|"
                      f"\n------------------------------------------\n")
                self.update_balance(self.user_info_1['Account Number'], self.remaining)
                self.update_transaction_limit(self.user_info_1['Account Number'], self.tlimit_remaining)
                self.update_transaction('Withdrawed', self.user_info_1['Account Number'], self.withdraw)
            else:
                print("\nYour Transaction limit is complete or less.\n")
        else:
            print("\nYour balance is low.Please Deposit.\n")

    # set pin
    def setPin(self):
        with open("File1.csv", 'r') as fs:
            reader = csv.reader(fs)
            self.user_info_4 = []
            self.found = False
            for row in reader:
                if row[0] == self.user_info_1['Account Number']:
                    self.found = True
                    row[4] = str(input("PLEASE ENTER THE NEW PIN : "))
                self.user_info_4.append(row)
            fs.close()
            if self.found == True:
                with open('File1.csv', 'w', newline='') as fws:
                    filei = csv.writer(fws)
                    filei.writerows(self.user_info_4)
                    fws.close()

    # transfer amount to other account
    def transfer_amount(self):
        self.accountT = str(input("ENTER ACCOUNT NUMBER TO WHICH YOU WANT TOO TRANSFER : "))
        self.amountbt = int(input("ENTER AMOUNT TO TRANSFER : "))
        self.found_to = False
        self.accountbalance = int(self.user_info_1['Balance'])
        self.rtlimit = int(self.user_info_1['Transfer Limit'])
        if self.accountbalance >= self.amountbt:
            if self.rtlimit >= self.amountbt:
                self.new_balance = self.accountbalance - self.amountbt
                self.remining_limit = self.rtlimit - self.amountbt
                self.update_balance(self.user_info_1['Account Number'], self.new_balance)
                self.update_transaction_limit(self.user_info_1['Account Number'], self.remining_limit)
                self.update_transaction(self.accountT, self.user_info_1['Account Number'], self.amountbt)

            else:
                print("\nLIMIT EXCCEEDED\n")
        else:
            print("\nLOW BALANCE\n")

    # show transaction history
    def transaction_history(self):
        account = str(self.user_info_1["Account Number"])
        df = pd.read_csv('File2.csv')
        new_df = df.loc[(df["From Account"] == account) | (df["To Account"] == account)]
        print(new_df)
