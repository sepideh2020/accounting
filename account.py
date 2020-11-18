import logging
import os
import pandas as pd


class Account:
    # there are two class variable that are type of incomes and costs
    income = ["Food", "clothing", "housing"]
    cost = ["Salary", "profit_of_capital", "inheritance"]

    def __init__(self, account_number, initial_amount, bank_name, cart_number, directory):
        """for each account init it`s attributes then create .log and .csv for it """
        self.account_number = account_number
        # first balance of account
        self.initial_amount = initial_amount
        self.bank_name = bank_name
        self.cart_number = cart_number
        self.balance = initial_amount
        # make log file for each account
        self.logger = logging.getLogger(self.account_number)
        f_handler = logging.FileHandler(os.path.join(directory, '{}.log'.format(account_number)))
        f_handler.setLevel(logging.INFO)
        f_format = logging.Formatter('%(message)s in %(asctime)s')
        f_handler.setFormatter(f_format)
        self.logger.addHandler(f_handler)
        # make csv file for each account
        df = pd.DataFrame(list(), columns=['account_number', 'value', "category", "type"])
        df.to_csv(os.path.join(directory, '{}.csv'.format(account_number)))
        self.csv_file = os.path.join(directory, '{}.csv'.format(account_number))

    @classmethod
    def new_income(cls, income):
        """add new in come type"""
        cls.income.append(income)

    @classmethod
    def new_cost(cls, cost):    #chera bedone  class method  nemishe?
        """add new cost"""
        cls.cost.append(cost)

    def spend_account_balance(self, amount):
        """check for spend if possible return True and change balance else return false"""
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            return True

    def earn_income(self, amount):
        """update balance after earn """
        self.balance += amount

    def __str__(self):
        """print for account"""
        return "Balance:" + str(self.balance) + "Bank_name:" + self.bank_name + "cart_number :" + self.cart_number

# a = Account("50222910", "1000", "pasargad", "552", "mahnaz_divargar")
# b = Account("50222920", "1000", "pasargad", "552", "mahnaz_divargar")
# a.logger.warning('This is a warning')
