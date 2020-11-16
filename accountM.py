import csv
import os.path


class Account:
    income_type = ["Food", "clothing", "housing"]
    cost_type = ["Salary", "profit_of_capital", "inheritance"]

    def __init__(self, bank_name, account_number, card_number):  # lozomi nadare vaghti karbar mikhad accounteshocheck
        # kone azash mojodisho begirim ya mikhad  variz kone

        self.account_number = account_number
       #self.initial_amount = initial_amount   #initial amount inha niyazi nist
        self.bank_name = bank_name
        self.card_number = card_number
        try:

            with open(
                    '/Users/Niktab/Desktop/AI/MaktabSahrif/projects/accounting/users/users_info/mohammad/user_accounts.csv',
                    'r') as check_account_existence:
                reader = csv.DictReader(check_account_existence)
                for row in reader:

                    if row['Card Number'] == str(self.card_number) and row['Account Number'] == str(self.account_number) and row['Bank Name'] == self.bank_name:
                        self.account_balance = row['Account Balance']
                        # print(self.account_balance)
                        self.initial_amount=row['Initial Amount']
                        # print(self.initial_amount)
                    else:
                        print("Account does not exist")
        except FileNotFoundError:
            print("File does not exist")




# add to file
# add to logg file
# logger.debug("account_number:  " + self.account_number + "  initial_amount :  " + initial_amount +
#              "  bank_name:  " + self.bank_name + "  card_number:  " + self.card_number)


#
#     @classmethod
#     def new_income(cls, income):  # income name changed
#         cls.income_type.append(income)
#
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
#a = Account("Melat".capitalize(),1234, 5000)
#mohammad = Account("tejarat".capitalize(), 1234, 5000)
# print(mohammad)
