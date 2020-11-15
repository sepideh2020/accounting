
class Input:

    def get_operation(self):

        print("\t MAIN MENU")
        print("\t1. NEW ACCOUNT")
        print("\t2. DEPOSIT AMOUNT")
        print("\t3. WITHDRAW AMOUNT")
        print("\t4. TRANSACTIONS")
        print("\t5. CLOSE AN ACCOUNT")
        print("\t6. LOGIN ")
        print("\t7. LOGOUT ")
        print("\t8. EXIT")
        print("\t Select Your Option (1-8)")
        op = input()

        if op not in range(1,7):
            print('Invalid operation.  Please try again.')
            op = None
        return op

    def get_income_op(self):
        print("\t deposit options:")
        print("\t 1.salary")
        print("\t 2.profit")
        print("\t 3.inheritance")

        income_op = input()
        if income_op not in range(1,4):
            print('Invalid operation.  Please try again.')
            income_op = None
        return income_op

    def get_expenses_op(self) :
        print("\t withdraw options:")
        print("\t 1.wear")
        print("\t 2.housing")
        print("\t 3.dish")

        expenses_op = input()
        if expenses_op not in range(1, 4) :
            print('Invalid operation.  Please try again.')
            expenses_op = None
        return expenses_op


    def get_amount(self):
        amount = None
        try:
            value = input('Enter amount: ')
            amount = float(value)
            if amount <= 0:
                raise Exception('The amount must be positive.')
        except ValueError:
            print('Invalid amount.  Please try again.')
        except Exception as e:
            print(e)
            amount = None

        return amount