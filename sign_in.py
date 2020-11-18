import csv

from pathlib import Path
import logging


class SignIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password
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

    def check_user_info(self):

        f = open('user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.username == details[0] and (self.password) == details[1]:
                logging.warning('Welcome')
                break

            # this whole bit of code is meant to read from the csv and check if the login details are correct
        else:

            logging.error("User does not exists")


# add the user's username and pass to the main csv file


mohammad = SignIn("MOHAMMAD", "ALI")
mohammad.check_user_info()
mehdi = SignIn("hossain", "ALI")
mehdi.check_user_info()
