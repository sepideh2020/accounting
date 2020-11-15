from logging import Logging


# in run.py first make an empty folder whose name is the user's name
class Account(Logging):
    def __init__(self, user_name, password):
        super().__init__(user_name, password)
        self.bank_name = 0
        self.account_number = 0
        self.card_number = 0
        self.deposit = 0
        self.expense = 0
        self.income = 0
        self.account_balance = 0
        self.expense_type = ["cloth", "rent", "tuition", "other"]
        self.income_type = ["salary", "stock", "gift", "other"]

    def add_new_account(self, new_bank_name, new_account_number, new_card_number, new_deposit):
        self.bank_name = new_bank_name
        self.account_number = new_account_number
        self.card_number = new_card_number
        self.deposit = new_deposit
        self.account_balance = new_deposit
        # go to the users folder
        # make an empty csv file for user's bank info
        # if user's bank info exits add info to it else make a users_bank_info.csv
        # add the info to the csv file (in the user folder(user bank information)
        # if bank directory does not exist make an empty directory
        # in the bank directory make transaction csv file for each account and add the info to it

    def add_expense(self, bank_name, account_number, expense, expense_type):
        pass
        # in the run ask the user to enter the account number
        # ask the user type of expense (in the run file)add  the date and type to the transaction.csv
        # check the account number and bank name in the bank_info.csv
        # if file exits add the transaction to bank_name transaction csv file
        # tell the user file does not exits
        # update the account balance
        # then log and add it to the log file which is beside transactions.csv file

    def add_income(self, bank_name, account_number, income, income_type):
        pass
        # in the run ask the user to enter the account number
        # ask the user type of income (in the run file)add  the date and type to the transaction.csv
        # check the account number and bank name in the bank_info.csv
        # if exits add the transaction to bank_name transaction csv file
        # tell the user file does not exits
        # update the account balance
        # then log and add it to the log file which is beside transactions.csv file

    def check_transactions(self, bank_name, account_number):
        pass
    # open the transaction file which is in the bank folder and print it
