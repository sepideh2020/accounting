import os

import pandas as pd

from account import Account
from user import User
from sign_in import SignIn
from sign_up import SignUp

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
user = users[1].display_account_turnover_with_charts("5022 2910 6268 9722")
user = users[1].pie_chart("5022 2910 6268 9722")

# ثبت نام کردن در برنامه
# for i in range(3):
#     user_name = input("user_name:")
#     pass_word = input("password:")
#     if len(users) == 0:
#         sign_up.new_user_info(user_name, pass_word)
#         users.append(User(user_name, pass_word))
#     else:
#         for user in users:
#             if user.user_name == user_name:
#                 print('this user_name already exist chose another user_name')
#                 break
#         else:
#             sign_up.new_user_info(user_name, pass_word)
#             users.append(User(user_name, pass_word))


# login
# user_name = input("user_name:")
# pass_word = input("password:")
# if sign_in.check_user_info(user_name, pass_word):
#     for user in users:
#         if user.user_name == user_name:
#             current_object = user
#             break
# else:
#     # یه حلقه که تا درست نشده خارج نشه یا خودش بخواد خارج شه
#     print("some thing is not correct check 1.signup first 2.enter correct user or pass word")

# # new account
# # اول ببین اگر کارنت ابجکت خالی هست بگه لاگین کن
# print("new account")
# account_number = input("account_number:")
# initial_amount = input("initial_amount:")
# bank_name = input("bank_name")
# cart_number = input("cart_number")
#current_object.new_account(account_number, float(initial_amount), bank_name, cart_number)
#
# # spend
# print(Account.cost)
# account_number = input("account_number:")
# value = float(input("value:"))
# spend_type = input("type:")
# if current_object.spend(account_number, value, spend_type):
#     print("send successfully")
# else:
#     print("account_number wrong")
#
# # earn
# print(Account.income)
# account_number = input("account_number:")
# value = float(input("value:"))
# spend_type = input("type:")
# if current_object.earn(account_number, value, spend_type):
#     print("earn successfully")
# else:
#     print("account_number wrong")
#
# # new_spend_type
# spend_type = input("type:")
# Account.new_cost(spend_type)
#
# # new_income_type
# income_type = input("type:")
# Account.new_income(spend_type)
