import os
import csv
import logging
from pathlib import Path


class User:
    def __init__(self):
        self.bank_name = None
        self.card_number = 0
        self.account_number = 0
        self.initial_amount = 0
        self.account_balance = 0
        user_accounts = Path(
            '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad/user_accounts.csv')
        if user_accounts.is_file():  # check if the user_accounts.csv file exists
            pass
        else:
            # make user_accounts.csv file which has all user's account information
            with open(
                    '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad/user_accounts.csv',
                    'w', newline='') as user_accounts:
                fieldnames = ['Bank Name', 'Account Number', 'Card Number', 'Initial Amount', 'Account Balance']
                headers = csv.DictWriter(user_accounts, fieldnames=fieldnames)
                headers.writeheader()

        # add Existing accounts from file

        # self.accounts = []

    def new_account(self, bank_name, account_number, card_number, initial_amount):
        """BY CALLING THIS FUNCTION USER CAN MAKE A NEW ACCOUNT AND ADD IT TO THE USERS ACCOUNT.CSV IF DOES NOT EXITS
        ,WHEN THE ACCOUNT IS ADDED A TRANSACTION.CSV FILE IS MADE FOR ADDING TRANSACTIONS WHICH ARE RELATED TO THAT ACCOUNT
        """
        self.bank_name = bank_name.capitalize()
        self.card_number = card_number
        self.account_number = account_number
        self.initial_amount = initial_amount
        self.account_balance = initial_amount
        # os.path.join(path, bank_name)

        try:
            path = '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad'
            new_dir = os.path.join(path, str(account_number))
            os.mkdir(new_dir)  # each account will have a directory whose name is the account_number
            with open(
                    '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info\mohammad/user_accounts.csv',
                    'a+', newline='') as user_accounts:
                fieldnames = ['Bank Name', 'Account Number', 'Card Number', 'Initial Amount', 'Account Balance']
                headers = csv.DictWriter(user_accounts, fieldnames=fieldnames)
                # users_account.csv file is made is user_info directory
                headers.writerow(
                    {'Bank Name': self.bank_name, 'Account Number': self.account_number,
                     'Card Number': self.card_number,
                     'Initial Amount': self.initial_amount, 'Account Balance': self.account_balance})

            with open(os.path.join(new_dir, 'transactions.csv'), 'w', newline='') as transactions:
                fieldnames = ['Withdraw or Deposit amount', 'Type', 'Date']
                headers = csv.DictWriter(transactions, fieldnames=fieldnames)
                headers.writeheader()  # each bank account will have a transaction.csv folder


        except FileExistsError:
            logging.error('Account already exists')  # if account directory already exists log an error message

    # self.accounts.append(Account(account_number, initial_amount, bank_name, card_number))
    #
    # def spend(self, unique, value, category, ):
    #     # unique == account_number or card_number
    #     for account in self.accounts:
    #         if account.account_number == unique or account.card_number == unique:
    #             account.spend_account_balance(value)
    #             # file add (account_number , card_number ,value,category)
    #             # log : successfully translate


# def earn(self, unique, value, category):
#     for account in self.accounts:
#         if account.account_number == unique or account.card_number == unique:
#             account.earn_income(value)
#             # file add (account_number , card_number ,value,category)
#             # log : successfully translate
#
# @staticmethod
# def show_account(unique):
#     for account in User.accounts:i
#         if account.account_number == unique or account.card_number == unique:
#             print(account)
# mohammad = User()
# mohammad.new_account("tejarat".capitalize(), 1235, 464758, 785938465378)

# ali = User()
# ali.new_account("tejarat".capitalize(), 35465768, 5678890, 34654789)
