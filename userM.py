import os
from accountM import Account
import csv
import logging


class User:
    def __init__(self):
        self.bank_name = None
        self.cart_number = 0
        self.account_number = 0
        self.initial_amount = 0
        self.account_balance = 0
        with open(
                '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info\mohammad/user_accounts.csv',
                'w', newline='') as user_accounts:
            fieldnames = ['Bank Name', 'Cart Number ', 'Account Number', 'Initial Amount', 'Account Balance']
            headers = csv.DictWriter(user_accounts, fieldnames=fieldnames)
            headers.writeheader()

        # add Existing accounts from file
        self.accounts = []

    def new_account(self, bank_name, account_number, cart_number, initial_amount, account_balance):
        """BY CALLING THIS FUNCTION USER CAN MAKE A NEW ACCOUNT AND ADD IT TO THE USERS ACCOUNT.CSV IF DOES NOT EXITS
        ,WHEN THE ACCOUNT IS ADDED A TRANSACTION.CSV FILE IS MADE FOR ADDING TRANSACTIONS WHICH ARE RELATED TO THAT ACCOUNT
        """
        self.bank_name = bank_name.capitalize()
        self.account_number = account_number
        self.initial_amount = initial_amount
        self.cart_number = cart_number
        self.account_balance = account_balance
        # os.path.join(path, bank_name)
        try:
            path = '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad'
            new_dir = os.path.join(path, bank_name)
            os.mkdir(new_dir)  # each bank will have a directory directory is made if exits user gets an error

        except FileExistsError:
            print("Account already exists")

        with open(
                '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info\mohammad/user_accounts.csv',
                'w', newline='') as user_accounts:
            fieldnames = ['Bank Name', 'Cart Number ', 'Account Number', 'Initial Amount', 'Account Balance']
            headers = csv.DictWriter(user_accounts, fieldnames=fieldnames)
            headers.writeheader()  # users_account.csv file is made is user_info directory
            headers.writerow(
                {'Bank Name': self.bank_name, 'Cart Number ': self.cart_number, 'Account Number': self.account_number,
                 'Initial Amount': self.initial_amount, 'Account Balance': self.account_balance})

        with open(os.path.join(new_dir, 'transactions.csv'), 'w', newline='') as transactions:
            fieldnames = ['Withdraw or Deposit amount', 'Type', 'Date']
            headers = csv.DictWriter(transactions, fieldnames=fieldnames)
            headers.writeheader()  # each bank account will have a transaction file

    # self.accounts.append(Account(account_number, initial_amount, bank_name, cart_number))

    def spend(self, unique, value, category):

        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                account.spend_account_balance(value)
                # file add (account_number , cart_number ,value,category)
                # log : successfully translate


# def earn(self, unique, value, category):
#     for account in self.accounts:
#         if account.account_number == unique or account.cart_number == unique:
#             account.earn_income(value)
#             # file add (account_number , cart_number ,value,category)
#             # log : successfully translate
#
# @staticmethod
# def show_account(unique):
#     for account in User.accounts:
#         if account.account_number == unique or account.cart_number == unique:
#             print(account)

mohammad = User()
mohammad.new_account("tejarat".capitalize(), 1234, 5000, 43321, 10000)
print(mohammad)
