class Account:
    income_type = ["Food", "clothing", "housing"]
    cost_type = ["Salary", "profit_of_capital", "inheritance"]

    def __init__(self, account_number, initial_amount, bank_name, cart_number):
        self.account_number = account_number
        self.initial_amount = initial_amount
        self.bank_name = bank_name
        self.cart_number = cart_number
        self.balance = initial_amount

        # add to file
        # add to logg file
        # logger.debug("account_number:  " + self.account_number + "  initial_amount :  " + initial_amount +
        #              "  bank_name:  " + self.bank_name + "  cart_number:  " + self.cart_number)

    @classmethod
    def new_income(cls, income):  # income name changed
        cls.income_type.append(income)

    @classmethod
    def new_cost(cls, cost):  # cost name changed
        cls.cost_type.append(cost)

    def spend_account_balance(self, amount):
        self.balance -= amount

    def earn_income(self, amount):
        self.balance += amount

    def __str__(self):
        return "Balance:" + str(self.balance) + "Bank_name:" + self.bank_name + "cart_number :" + self.cart_number


a = Account("50222910", "1000", "pasargad", "552")
