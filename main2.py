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


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CGREYBG = '\33[37m'
    RED = '\033[31m'
    GREEN = '\033[32m'


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

op = 0
while True:
    # Enter a number within range(1-10) if the number was not in range (1-10) or was not integer give error
    print(Bcolors.FAIL + "\n")
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
    print("\t Select Your Option (1-11)" + Bcolors.ENDC)
    try:
        op = int(input(Bcolors.FAIL + "Enter:" + Bcolors.ENDC))
        if op in range(1, 12):

            if op == 1:
                user_name = input(Bcolors.FAIL + "Username:")
                pass_word = input("Password:" + Bcolors.ENDC)
                if len(users) == 0:
                    sign_up.new_user_info(user_name, pass_word)
                    users.append(User(user_name, pass_word))

                    print(Bcolors.GREEN + "singed up successfully" + Bcolors.ENDC)
                else:
                    for user in users:
                        if user.user_name == user_name:
                            print(Bcolors.HEADER + 'Username already exists choose another username' + Bcolors.ENDC)
                            break
                    else:
                        sign_up.new_user_info(user_name, pass_word)
                        users.append(User(user_name, pass_word))
                        print("\a")
                        print(Bcolors.GREEN + "singed up successfully" + Bcolors.ENDC)


            elif op == 2:
                if current_object is not None:
                    print(Bcolors.HEADER + "{},you already logged in".format(current_object.user_name) + Bcolors.ENDC)
                else:

                    exi = 0
                    while exi != 1:

                        user_name = input(Bcolors.FAIL + "Username:")
                        pass_word = input("Password:" + Bcolors.ENDC)
                        if sign_in.check_user_info(user_name, pass_word):
                            for user in users:
                                if user.user_name == user_name:
                                    current_object = user
                                    print("\a")
                                    print(Bcolors.HEADER + '***Welcome***\n' + Bcolors.ENDC)
                                    break
                            break

                        else:
                            print(Bcolors.RED + "***Wrong Username or Password***" + Bcolors.ENDC)
                            print(Bcolors.HEADER + 'Try Again' + Bcolors.ENDC)

                        exi = input(Bcolors.HEADER + "Do you want to sign out? Y/N :" + Bcolors.ENDC)
                        if exi in ["Y", "y"]:
                            exi = 1
                        if exi not in ["y", "Y", "n", "N"]:
                            logging.error(Bcolors.HEADER + "Enter a valid input\n" + Bcolors.ENDC)





            elif op == 3:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)
                else:
                    while True:
                        try:

                            print(Bcolors.HEADER + "      ***New account***" + Bcolors.ENDC)
                            account_number = input(Bcolors.FAIL + "Account number:").strip().replace(" ", "")
                            initial_amount = float(input("Initial amount:").replace(" ", ""))
                            bank_name = str(input("Bank name:").strip())
                            cart_number = input("Cart number:" + Bcolors.ENDC).strip().replace(" ", "")
                            current_object.new_account(account_number, initial_amount, bank_name, cart_number)
                            print(Bcolors.GREEN + "your account add successfully" + Bcolors.ENDC)
                            break
                        except ValueError:
                            logging.error(Bcolors.HEADER + "enter a valid input" + Bcolors.ENDC)

            elif op == 4:

                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:
                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1
                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.HEADER + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            break

                    value = float(input(Bcolors.FAIL + "Amount:" + Bcolors.ENDC))
                    while True:
                        print(Bcolors.HEADER + "\t  Earning Types" + Bcolors.ENDC)
                        for key, val in Account.dict_income.items():
                            print(Bcolors.FAIL + "\t{}. {}".format(key, val) + Bcolors.ENDC)

                        spend_type = int(input(Bcolors.FAIL + "type:" + Bcolors.ENDC))
                        if spend_type == 1:
                            new_income_key = input(Bcolors.HEADER + "Enter new income type:" + Bcolors.ENDC)
                            Account.new_income(new_income_key)
                            continue
                        else:
                            spend_type = Account.dict_income[spend_type]

                            if current_object.earn(dict1[account_number], value, spend_type):
                                print("\a")
                                print(Bcolors.GREEN + "Earned successfully" + Bcolors.ENDC)
                                break

                            else:
                                print(Bcolors.RED + "Wrong account number" + Bcolors.ENDC)
                                break


            elif op == 5:

                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:

                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1

                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.HEADER + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            break

                    value = float(input(Bcolors.FAIL + "Amount:" + Bcolors.ENDC))
                    while True:
                        print(Bcolors.HEADER + "\t  Spend Types" + Bcolors.ENDC)
                        for key, val in Account.dict_cost.items():
                            print(Bcolors.FAIL + "\t{}. {}".format(key, val)+ Bcolors.ENDC)

                        spend_type = int(input(Bcolors.FAIL + "Spend type:" + Bcolors.ENDC))
                        if spend_type == 1:
                            new_cost_key = input(Bcolors.FAIL + "Enter new type:" + Bcolors.ENDC)
                            Account.new_cost(new_cost_key)
                            continue
                        else:
                            spend_type = Account.dict_cost[spend_type]

                            if current_object.spend(dict1[account_number], value, spend_type):
                                print("\a")
                                print(Bcolors.GREEN + "spent successfully" + Bcolors.ENDC)
                                break
                            else:
                                print(Bcolors.WARNING + "your balance is not enough" + Bcolors.ENDC)
                                break




            elif op == 6:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:

                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1
                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.HEADER + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            current_object.list_of_transactions(dict1[account_number])
                            break

            elif op == 7:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:

                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1
                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.FAIL + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            current_object.show_account(dict1[account_number])
                            break

                    # nabashe hesab chizi nemige!!

            elif op == 8:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:

                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1
                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.HEADER + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            current_object.pie_chart(dict1[account_number])
                            break


            elif op == 9:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)

                else:

                    dict1 = {}
                    with open(current_object.csv_file, "r") as f:
                        i = 1
                        for line in f:
                            line = line.split(",")
                            if line[1] == "account_number":
                                print(Bcolors.HEADER + "\n" + line[1] + Bcolors.ENDC)
                            else:
                                print(Bcolors.FAIL + str(i) + " . " + line[1] + Bcolors.ENDC)
                                dict1[i] = line[1]
                                i += 1
                    while True:

                        try:
                            account_number = 0
                            account_number = int(
                                input(Bcolors.HEADER + "Please enter your account number:" + Bcolors.ENDC))
                        except ValueError:
                            pass
                        if account_number not in dict1.keys():
                            print(
                                Bcolors.HEADER +
                                "\n please enter correct number you don`t have any account with this input\n"
                                + Bcolors.ENDC)
                        else:
                            current_object.display_account_turnover_with_charts(dict1[account_number])
                            break


            elif op == 10:
                if current_object is None:
                    print(Bcolors.HEADER + "***Please login***" + Bcolors.ENDC)
                else:
                    current_object = None
                    print("\a")
                    print(Bcolors.GREEN + "Log out successfully" + Bcolors.ENDC)


            elif op == 11:
                print(Bcolors.HEADER + "Hope enjoyed our application" + Bcolors.ENDC)
                sys.exit()


        else:
            logging.error(Bcolors.RED + "Enter a number within range (1-10)" + Bcolors.ENDC)

    except ValueError:
        logging.error(Bcolors.RED + "Input is not valid,please enter a number" + Bcolors.ENDC)

    time.sleep(4)
    os.system('cls')
