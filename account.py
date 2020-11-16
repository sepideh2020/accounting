from input import Input

class Account():
    acc_no = 0
    card_no = 0
    bank_name = ""
    deposit = 0

    def __init__(self, balance, show_balance_after_transaction=True):
        self.balance = balance
        self.starting_balance = balance
        self.show_balance_after_transaction = show_balance_after_transaction
        self.transactions = []

    # def create_account(self):
    #     self.acc_no = int(input("Enter the account no : "))
    #     self.bank_name = input("Enter the account holder name : ")
    #     self.card_no = int(input("Enter the card no : "))
    #     self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current"))
    #     print("\n\n\nAccount Created")

    # def show_account(self) :
    #     print("Account Number : ", self.acc_no)
    #     print("Card Number : ", self.card_no)
    #     print("Account Holder Name : ", self.bank_name)
    #     print("Balance : ", self.deposit)

    def get_balance(self):
        return self.balance

    def show_balance(self):
        print('balance is {}'.format(self.balance))
        print()

    def acc_income(self ,amount):
        self.balance += amount
        self.transactions.append(['2', amount])
        if self.show_balance_after_transaction:
            self.show_balance()

    def acc_expenses(self, amount):
        if self.balance >= amount :
            self.balance -= amount
            self.transactions.append(['3', amount])
            if self.show_balance_after_transaction:
                self.show_balance()
        else:
            print("inefficient balance")


    def process_transactions(account):
        while True:
            amount = None
            op = Input().get_operation()
            if op == 6:
                break
            elif op == 4:
                account.show_transactions()
            elif op is not None:
                amount = Input().get_amount()

            if amount is None:
                pass
            elif op == 2:
                account.acc_income(amount)
                deposit_option = Input().get_income_op()
            elif op == 3:
                account.acc_expenses(amount)
                withdraw_option = Input().get_expenses_op()

    def show_transactions(self):
        balance = self.starting_balance
        print('   op       amount     balance')
        print('--------  ----------  ----------')
        print('                         {}  (starting)'.format(balance))
        for transaction in self.transactions:
            [op, amount] = transaction
            if op == 3:
                opp_label = 'withdraw'
                balance -= amount
            elif op == 2:
                opp_label = 'deposit'
                balance += amount
            print('{}      {}       {}'.format(opp_label, amount, balance))
        print()

