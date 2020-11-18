import csv

from sign_in import SignIn
from pathlib import Path
import logging


class SignUp:
    def __init__(self, new_username, new_password):
        self.new_username = new_username
        self.new_password = new_password
        user_accounts = Path(
            'user_information.csv')
        if user_accounts.is_file():  # check if the user_accounts.csv file exists
            pass
        else:
            # make user_accounts.csv file which has all user's account information
            with open(
                    'user_information.csv',
                    'w', newline='') as users_info:
                fieldnames = ['User Name', 'Password']
                headers = csv.DictWriter(users_info, fieldnames=fieldnames)
                headers.writeheader()

    def check_new_user_info(self):
        fieldnames = ['User Name', 'Password']
        # with open(
        #         'user_information.csv',
        #         'r',) as check_account_existence:
        #
        #     reader = csv.DictReader(check_account_existence, fieldnames=fieldnames)
        f = open('user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.new_username == details[0] and (self.new_password) == details[1]:
                logging.error('user already exists')
                break
            # this whole bit of code is meant to read from the csv and check if the login details are correct
        else:

            with open(
                    'user_information.csv',
                    'a', ) as check_account_existence:

                writer = csv.DictWriter(check_account_existence, fieldnames=fieldnames)
                # row['User Name'] = self.new_username
                writer.writerow({'User Name': self.new_username, 'Password': self.new_password})
            logging.warning("user added")


# add the user's username and pass to the main csv file

#
# mohammad = SignUp("MOHAMMAD", "ALI")
# mohammad.check_new_user_info()
# mehdi = SignUp("hossain", "ALI")
# mehdi.check_new_user_info()
