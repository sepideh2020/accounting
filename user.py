import logging
import os
import pandas as pd
from csv import writer
from account import Account


class User:
    def __init__(self, user_name):
        """for each user make directory that has info of accounts"""
        self.user_name = user_name
        self.accounts = []
        # create folder for each user
        os.system("mkdir {}".format(user_name))
        # make log file for each user to see log of crate new account
        self.logger = logging.getLogger(user_name)
        f_handler = logging.FileHandler(os.path.join(user_name, "accounts.log"))
        f_handler.setLevel(logging.DEBUG)
        f_format = logging.Formatter('%(message)s in  %(asctime)s  ')
        f_handler.setFormatter(f_format)
        # Add handlers to the logger
        self.logger.addHandler(f_handler)

    def new_account(self, account_number, initial_amount, bank_name, cart_number):
        """create new account for user in his directory and make log to know account create"""
        self.accounts.append(Account(account_number, initial_amount, bank_name, cart_number, self.user_name))
        self.logger.warning(
            "{} account with {} account_number added successfully".format(self.user_name, account_number))

    def spend(self, unique, value, category):
        """give account_number or card_number as unique then find account and do spend code
        if account exist return true else return false"""
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                if account.spend_account_balance(value):
                    account.logger.warning("{} toman spend for {} ".format(value, category))
                    with open(account.csv_file, 'a') as csv_file:
                        spend = pd.DataFrame([account.account_number, value, category, "spend"])
                        spend.to_csv(csv_file, header=False)

                    # spend = pd.DataFrame([account.account_number, value, category, "spend"])
                    # spend.to_csv(account.csv_file)

                else:
                    account.logger.warning("your balance is not enough for to spend money for {} ".format(category))
                return True
        else:
            return False

    def earn(self, unique, value, category):
        """give account_number or card_number as unique then find account and do earn code
                if account exist return true else return false"""
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                account.earn_income(value)
                account.logger.warning("{} toman earn form {} ".format(value, category))
                with open(account.csv_file, 'a') as csv_file:
                    earn = pd.DataFrame([account.account_number, value, category, "earn"])
                    earn.to_csv(csv_file, header=False)
                # spend = pd.DataFrame([account.account_number, value, category, "earn"])
                # spend.to_csv(account.csv_file)
                return True
        else:
            return False

    def show_account(self, unique):
        """give account_number or card_number as unique then show detail about account
        if account exist return true else return false"""
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                print(account)
                return True
        else:
            return False

    def list_of_transactions(self, unique):
        """give account number or card number and show transactions that save in log file
        if account exist return true else return false"""
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                path = os.path.join(self.user_name, '{}.log'.format(account.account_number))
                log_file = open(path)
                for line in log_file:
                    print(line)
                return True
        else:
            return False
