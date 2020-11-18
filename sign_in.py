import csv
import os

from pathlib import Path
import logging


class SignIn:
    """class for sign in and check whether the user exists or not"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if not os.path.exists('users'):  #if users directory does not exists make it
            os.makedirs('users')
        user_accounts = Path(
            'users/user_information.csv')
        if user_accounts.is_file():  # check if the user_information.csv file exists
            pass
        else:

            # make user_accounts.csv file which has all user's user name and password
            with open(
                    'users/user_information.csv',
                    'w', newline='') as users_info:
                fieldnames = ['User Name', 'Password']
                headers = csv.DictWriter(users_info, fieldnames=fieldnames)
                headers.writeheader()

    def check_user_info(self):
        # check whether the user exits or not

        f = open('user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.username == details[0] and (self.password) == details[1]:
                logging.warning('Welcome')
                break

        else:

            logging.error("User does not exists")


# mohammad = SignIn("MOHAMMAD", "ALI")
# mohammad.check_user_info()
# mehdi = SignIn("hossain", "ALI")
# mehdi.check_user_info()
