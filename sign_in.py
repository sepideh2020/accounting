import csv
import os

from pathlib import Path
import logging


class SignIn:
    """class for sign in and check whether the user exists or not"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        if not os.path.exists('users_info'):  #if users directory does not exists make it
            os.makedirs('users_info')
        user_accounts = Path(
            'users_info/user_information.csv')
        if user_accounts.is_file():  # check if the user_information.csv file exists
            pass
        else:

            # make user_accounts.csv file which has all user's user name and password
            with open(
                    'users_info/user_information.csv',
                    'w', newline='') as users_info:
                fieldnames = ['User Name', 'Password']
                headers = csv.DictWriter(users_info, fieldnames=fieldnames)
                headers.writeheader()
        self.logger = logging.getLogger(username)
        f_handler = logging.FileHandler("users_info/accounts.log")
        f_handler.setLevel(logging.WARNING)
        f_format = logging.Formatter(' %(levelname)s - %(message)s-%(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
        f_handler.setFormatter(f_format)
        # Add handlers to the logger
        self.logger.addHandler(f_handler)

    def check_user_info(self):
        # check whether the user exits or not

        f = open('users_info/user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.username == details[0] and (self.password) == details[1]:
                self.logger.warning("{} logged in ".format(self.username))
                break

        else:

            self.logger.error("{} does not exists ".format(self.username))


mohammad = SignIn("MOHAMMAD", "ALI")
mohammad.check_user_info()
mehdi = SignIn("hossain", "ALI")
mehdi.check_user_info()
