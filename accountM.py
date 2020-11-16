import csv
import os.path
import logging
import users
from tempfile import NamedTemporaryFile
import shutil


class Account:

    def __init__(self, bank_name, account_number, card_number):  # lozomi nadare vaghti karbar mikhad accounteshocheck
        self.income_types = ["Food", "clothing", "housing"]
        self.cost_types = ["Salary", "profit_of_capital", "inheritance"]
        # kone azash mojodisho begirim ya mikhad  variz kone
        self.bank_name = bank_name
        self.account_number = account_number
        # self.initial_amount = initial_amount   #initial amount inha niyazi nist

        self.card_number = card_number
        try:

            with open(
                    '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad/user_accounts.csv',
                    'r') as check_account_existence:
                reader = csv.DictReader(check_account_existence)
                try:
                    for row in reader:

                        if row['Bank Name'] == self.bank_name and row['Account Number'] == str(
                                self.account_number) and row['Card Number'] == str(self.card_number):
                            self.account_balance = int(row['Account Balance'])
                            # print(self.account_balance)
                            self.initial_amount = int(row['Initial Amount'])
                            # print(self.initial_amount)

                except AssertionError:  ###chetor handle konam agar esm nabashe
                    # print("Account already exists")
                    logging.error("Account does not exist")

        except FileNotFoundError:
            raise Exception("File does not exist")
            # logging.error('This is an error message')
            # print("File does not exist")

    # add to file
    # add to logg file
    # logger.debug("account_number:  " + self.account_number + "  initial_amount :  " + initial_amount +
    #              "  bank_name:  " + self.bank_name + "  card_number:  " + self.card_number)

    # income name changed
    # #inja nemishe az class method estefade kard
    def new_income(self, income_amount, income_type):

        if income_type in self.income_types:
            self.account_balance += int(income_amount)
        else:
            self.income_types.append(income_amount)
            self.account_balance += int(income_amount)

        tempfile = NamedTemporaryFile(mode='w', delete=False)
        fieldnames = ['Bank Name', 'Account Number', 'Card Number', 'Initial Amount', 'Account Balance']
        with open(
                '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad/user_accounts.csv',
                'r', newline='',encoding='utf8') as update_account, tempfile:

            reader = csv.DictReader(update_account, fieldnames=fieldnames)
            writer = csv.DictWriter(tempfile, fieldnames=fieldnames)
            for row in reader:
                if row['Bank Name'] == self.bank_name and row['Account Number'] == str(
                        self.account_number) and row['Card Number'] == str(self.card_number):
                    row['Account Balance'] = str(self.account_balance)
                    writer.writerow({'Account Balance': row['Account Balance']})


#     @classmethod
#     def new_cost(cls, cost):  # cost name changed
#         cls.cost_type.append(cost)
#
#     def spend_account_balance(self, amount):
#         self.account_balance -= amount
#
#     def earn_income(self, amount):
#         self.account_balance += amount
#
#     def __str__(self):
#         return "Balance:" + str(
#             self.account_balance) + "Bank_name:" + self.bank_name + "card_number :" + self.card_number
#
#
ali = Account("tejarat".capitalize(), 35465768, 5678890)
ali.new_income(4000, "food")
# a = Account("Melat".capitalize(), 1234, 5000)
