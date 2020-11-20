import os
import pandas as pd
from account import Account
from user import User
from sign_in import SignIn
from sign_up import SignUp
import time

# list of all user
users = []
current_object = None


def load_old_users():
    if os.path.exists('./users'):
        for user_directory in os.listdir("users"):
            # find password for this user
            users_password_file = pd.read_csv('users_info/user_information.csv')
            hash_password = users_password_file.loc[users_password_file["User Name"] == user_directory, "Password"]
            # reload user
            user = User(user_directory, hash_password, "accounts.csv")
            with open("users/{}/accounts.csv".format(user_directory)) as accounts_file:
                for line in accounts_file:
                    row, account_number, bank_name, cart_number, balance = line.split(",")
                    if row == "row":
                        pass
                    else:

                        user.accounts.append(
                            Account(account_number.strip(), float(balance.strip()), bank_name.strip(),
                                    cart_number.strip(),
                                    user_directory))

            users.append(user)


load_old_users()
sign_up = SignUp()
sign_in = SignIn()
# user = users[1].display_account_turnover_with_charts("5022 2910 6268 9722")
# user = users[1].pie_chart("5022 2910 6268 9722")

op = 0
while op != 11:

    print("\n")
    print("\t   MAIN MENU")
    print("\t1. REGISTER")
    print("\t2. LOGIN")
    print("\t4. NEW ACCOUNT ")
    print("\t5. EARN")
    print("\t6. SPEND")
    print("\t7. TRANSACTIONS")
    print("\t8. ACCOUNT INFORMATION")
    print("\t9. Display account turnover with pie charts")
    print("\t10. Display account turnover with broken line chart")
    print("\t11. EXIT")
    print("\t Select Your Option (1-8)")
    op = int(input("ENTER :"))
    time.sleep(2)
    os.system('cls')

    if op == 1:
        user_name = input("user_name:")
        pass_word = input("password:")
        if len(users) == 0:
            sign_up.new_user_info(user_name, pass_word)
            users.append(User(user_name, pass_word))
        else:
            for user in users:
                if user.user_name == user_name:
                    print('this user_name already exist chose another user_name')
                    break
                else:
                    sign_up.new_user_info(user_name, pass_word)
                    users.append(User(user_name, pass_word))

    elif op == 2:
        while True:
            user_name = input("user_name:")
            pass_word = input("password:")
            if sign_in.check_user_info(user_name, pass_word):
                for user in users:
                    if user.user_name == user_name:
                        current_object = user
                        print('***Login Successful***\n')
                        break
                break
            else:
                print("***some thing is not correct check 1.signup first 2.enter correct user or pass word***")
                print('Try Again\n')

    elif op == 4:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")
        else:
            print("new account")
            account_number = input("account_number:")
            initial_amount = input("initial_amount:")
            bank_name = input("bank_name")
            cart_number = input("cart_number")
            current_object.new_account(account_number, float(initial_amount), bank_name, cart_number)

    elif op == 5:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")
        else:
            account_number = input("account_number:")
            value = float(input("value:"))

            while True:
                print("\t   EARN CATEGORY")
                for key, val in Account.dict_income.items():
                    print("\t{}. {}".format(key, val))

                spend_type = int(input("type:"))
                if spend_type == 0:
                    new_income_key = input("Enter new income:")
                    Account.new_income(new_income_key)
                    continue
                else:
                    spend_type = Account.dict_income[spend_type]

                    if current_object.earn(account_number, value, spend_type):
                        print("earn successfully")

                    else:
                        print("account_number wrong")
                    break

    elif op == 6:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")

        else:
            account_number = input("account_number:")
            value = float(input("value:"))
            while True:
                print("\t   COST CATEGORY")
                for key, val in Account.dict_cost.items():
                    print("\t{}. {}".format(key, val))

                spend_type = int(input("type:"))
                if spend_type == 0:
                    new_cost_key = input("Enter new cost:")
                    Account.new_cost(new_cost_key)
                    continue
                else:
                    spend_type = Account.dict_cost[spend_type]

                    if current_object.spend(account_number, value, spend_type):
                        print("spend successfully")
                    else:
                        print("account_number wrong")
                    break

    elif op == 7:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")

        else:
            account_number = input("account_number:")
            current_object.list_of_transactions(account_number)

    elif op == 8:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")

        else:
            account_number = input("account_number:")
            current_object.show_account(account_number)

    elif op == 9:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")

        else:
            account_number = input("account_number:")
            current_object.pie_chart(account_number)

    elif op == 10:
        if current_object is None:
            print("***PLEASE LOGIN FIRST***\n")

        else:
            account_number = input("account_number:")
            current_object.display_account_turnover_with_charts(account_number)

    elif op not in range(1, 12):
        print('Invalid operation.  Please try again.')
