import csv
import os
from pathlib import Path
import logging


class SignUp:
    """class for making a new user and check whether the user already exists or not"""

    def __init__(self, new_username, new_password):
        self.new_username = new_username
        self.new_password = new_password
        if not os.path.exists('users_info'):  # if users directory does not exists make it
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

        self.logger = logging.getLogger(new_username)
        f_handler = logging.FileHandler("users_info/accounts.log")
        f_handler.setLevel(logging.WARNING)
        f_format = logging.Formatter(' %(levelname)s - %(message)s-%(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
        f_handler.setFormatter(f_format)
        # Add handlers to the logger
        self.logger.addHandler(f_handler)

    def check_new_user_info(self):
        fieldnames = ['User Name', 'Password']

        f = open('users_info/user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.new_username == details[0] and self.new_password == details[1]:
                self.logger.error("{} already exists".format(self.new_username))

                return False
            # add the user's username and pass to the main csv file

        else:

            with open(
                    'users_info/user_information.csv',
                    'a', ) as check_account_existence:

                writer = csv.DictWriter(check_account_existence, fieldnames=fieldnames)
                # row['User Name'] = self.new_username
                writer.writerow({'User Name': self.new_username, 'Password': self.new_password})
            # logging.warning("{} added".format(self.new_username)) chera neshonesh nemide?
            self.logger.warning("{} added".format(self.new_username))

            # add the user's username and pass added to the user_accounts.csv
            return True


# mohammad = SignUp("MOHAMMAD", "ALI")
# mohammad.check_new_user_info()
# mehdi = SignUp("hossain", "ALI")
# mehdi.check_new_user_info()
