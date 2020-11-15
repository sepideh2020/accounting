from accont import Account


class User:
    def __init__(self):
        # add Existing accounts from file
        self.accounts = []

    def new_account(self, account_number, initial_amount, bank_name, cart_number):
        self.accounts.append(Account(account_number, initial_amount, bank_name, cart_number))

    def spend(self, unique, value, category):
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                account.spend_account_balance(value)
                # file add (account_number , cart_number ,value,category)
                # log : successfully translate

    def earn(self, unique, value, category):
        for account in self.accounts:
            if account.account_number == unique or account.cart_number == unique:
                account.earn_income(value)
                # file add (account_number , cart_number ,value,category)
                # log : successfully translate

    @staticmethod
    def show_account(unique):
        for account in User.accounts:
            if account.account_number == unique or account.cart_number == unique:
                print(account)
