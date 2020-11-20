import os
import sys

import pandas as pd
from account import Account
from user import User
from sign_in import SignIn
from sign_up import SignUp
import time
import logging
import math

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
while True:
    # Enter a number within range(1-10) if the number was not in range (1-10) or was not integer give error
    print("\n")
    print("\t   Main menu")
    print("\t1. Sign up")
    print("\t2. login")
    print("\t3. Add new account ")
    print("\t4. Earn")
    print("\t5. Spend")
    print("\t6. Transaction")
    print("\t7. Account Information")
    print("\t8. Display account turnover with Pie Charts")
    print("\t9. Display account turnover with broken Line Chart")
    print("\t10.Log out")
    print("\t11.Exit")

    print("\t Select Your Option (1-11)")
    try:
        op = int(input("Enter:"))
        if op in range(1, 12):

            if op == 1:
                user_name = input("Username:")
                pass_word = input("Password:")
                if len(users) == 0:
                    sign_up.new_user_info(user_name, pass_word)
                    users.append(User(user_name, pass_word))
                else:
                    for user in users:
                        if user.user_name == user_name:
                            print('Username already exists choose another username')
                            break
                        else:
                            sign_up.new_user_info(user_name, pass_word)
                            users.append(User(user_name, pass_word))

            elif op == 2:
                if current_object is not None:
                    print("{},you already logged in".format(current_object.user_name))
                else:
                    exit = 0
                    while exit != 1:

                        user_name = input("Username:")
                        pass_word = input("Password:")
                        if sign_in.check_user_info(user_name, pass_word):
                            for user in users:
                                if user.user_name == user_name:
                                    current_object = user
                                    print('***Welcome***\n')
                                    break
                            break

                        else:
                            print("***Wrong Username or Password***")
                            print('Try Again')

                        exit2 = input("Do you want to sign out? Y/N :")  # agar addad vared kard kar nemikone????????????????
                        if exit2 in "Yy":
                            print()
                            exit = 1
                        else:
                            logging.error("Enter a valid input")
                            break




            elif op == 3:
                if current_object is None:
                    print("***Please login***")
                else:
                    while True:
                        try:
                            print("New account")
                            account_number = int(input("Account number:").strip().replace(" ", ""))
                            initial_amount = float(input("Initial amount:").replace(" ", ""))
                            bank_name = str(input("Bank name:").strip())
                            cart_number = int(input("Cart number:").strip().replace(" ", ""))
                            current_object.new_account(account_number, initial_amount, bank_name, cart_number)
                        except ValueError:
                            logging.error("enter a valid input")

            elif op == 4:

                if current_object is None:
                    print("***Please login***")

                else:
                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print("\n" + line[1])
                            else:
                                print(str(i) + " . " + line[1])
                                dict1[i] = line[1]
                                i += 1

                    account_number = int(input("Please enter your account number:"))
                    value = float(input("Amount:"))
                    while True:
                        print("\t  Earning Types")
                        for key, val in Account.dict_income.items():
                            print("\t{}. {}".format(key, val))

                        spend_type = int(input("type:"))
                        if spend_type == 1:
                            new_income_key = input("Enter new income type:")
                            Account.new_income(new_income_key)
                            continue
                        else:
                            spend_type = Account.dict_income[spend_type]

                            if current_object.earn(dict1[account_number], value, spend_type):
                                print("Earned successfully")
                                break

                            else:
                                print("Wrong account number")
                                break


            elif op == 5:

                if current_object is None:
                    print("***Please login***")

                else:
                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print("\n" + line[1])
                            else:
                                print(str(i) + " . " + line[1])
                                dict1[i] = line[1]
                                i += 1

                    account_number = int(input("Please enter your account number:"))

                    value = float(input("Amount:"))
                    while True:
                        print("\t  Cost Types")
                        for key, val in Account.dict_cost.items():
                            print("\t{}. {}".format(key, val))

                        spend_type = int(input("Spend type:"))
                        if spend_type == 1:
                            new_cost_key = input("Enter new type:")
                            Account.new_cost(new_cost_key)
                            continue
                        else:
                            spend_type = Account.dict_cost[spend_type]

                            if current_object.spend(dict1[account_number], value, spend_type):
                                print("spent successfully")
                                break
                            else:
                                print("wrong Account number ")
                            break


            elif op == 6:
                if current_object is None:
                    print("***Please login***\n")

                else:
                    while True:
                        try:
                            account_number = int(input("Account number:"))
                            current_object.list_of_transactions(account_number)
                        except ValueError:
                            logging.error("Enter a valid input")

            elif op == 7:
                if current_object is None:
                    print("***Please login***\n")

                else:
                    account_number = input("Account number:")
                    current_object.show_account(account_number)
                    # nabashe hesab chizi nemige!!

            elif op == 8:
                if current_object is None:
                    print("***Please login***\n")

                else:
                    account_number = input("Account number:")
                    current_object.pie_chart(account_number)

            elif op == 9:
                if current_object is None:
                    print("***PLEASE LOGIN FIRST***\n")

                else:
                    account_number = input("account_number:")
                    current_object.display_account_turnover_with_charts(account_number)
            elif op==10:
                current_object=None
                print("Log out successfully")


            elif op == 11:
                print("Hope enjoyed our application")
                sys.exit()


        else:
            logging.error("Enter a number within range (1-10)")

    except ValueError:
        logging.error("Input is not valid,please enter a number")

    time.sleep(1)
    os.system('cls')
