import os
from accountM import Account
import csv


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
        # self.accounts = []

    def new_account(self, bank_name, account_number, cart_number, initial_amount, account_balance):
        self.bank_name = bank_name
        self.account_number = account_number
        self.initial_amount = initial_amount
        self.cart_number = cart_number
        self.account_balance = account_balance
        path = '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad'
        # os.path.join(path, bank_name)
        try:
            path = '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad'
            new_dir = os.path.join(path, bank_name)
            os.mkdir(new_dir)
        except FileExistsError:
            print("Account already exists")
        with open(
                '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info\mohammad/user_accounts.csv',
                'w', newline='') as user_accounts:
            fieldnames = ['Bank Name', 'Cart Number ', 'Account Number', 'Initial Amount', 'Account Balance']
            headers = csv.DictWriter(user_accounts, fieldnames=fieldnames)
            headers.writeheader()
            headers.writerow({'Bank Name': bank_name, 'Cart Number ': cart_number, 'Account Number': account_number,
                              'Initial Amount': initial_amount, 'Account Balance': account_balance})

    # self.accounts.append(Account(account_number, initial_amount, bank_name, cart_number))

#
# def spend(self, unique, value, category):
#     for account in self.accounts:
#         if account.account_number == unique or account.cart_number == unique:
#             account.spend_account_balance(value)
#             # file add (account_number , cart_number ,value,category)
#             # log : successfully translate
#
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
mohammad.new_account("tejarat", 1234, 5000, 43321, 10000)
print(mohammad)