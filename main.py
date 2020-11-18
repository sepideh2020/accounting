from user import User
from account import Account
import os

# list of all user
users = []


def load_old_users():
    if os.path.exists('./users'):
        for user_directory in os.listdir("users"):
            user = User(user_directory, 123, "accounts.csv")
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
users.append(User("mahnaz_divargar", 123, ))
users.append(User("maryam_divargar", 123, ))
users[0].new_account("5022_2910", 100, "tejarat", "501010")
users[0].new_account("5022_2911", 100, "tejarat", "501010")
print(users[0].accounts[0].balance)
users[0].earn("5022_2910", 2000, "salary")
users[0].spend("5022_2910", 100, "food")
users[0].earn("5022_2910", 2000, "salary")
users[0].spend("5022_2910", 100, "food")
users[0].spend("5022_2910", 100, "food")
users[0].earn("5022_2910", 2000, "salary")
users[0].spend("5022_2910", 100, "food")
users[0].spend("5022_2910", 100, "food")
users[0].earn("5022_2910", 2000, "salary")
