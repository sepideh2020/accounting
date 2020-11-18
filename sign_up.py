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

        logging.basicConfig(filename='users_info/users_information.log', level=logging.INFO, filemode='w',
                            format='%(name)s - %(levelname)s - %(message)s-%(asctime)s', datefmt='%d-%b-%y %H:%M:%S')
        logging.info('New user added at :')

    def check_new_user_info(self):
        fieldnames = ['User Name', 'Password']

        f = open('users_info/user_information.csv', 'r')
        for line in f:
            details = line.strip().split(",")
            if self.new_username == details[0] and (self.new_password) == details[1]:
                logging.error('user already exists')
                break
            # add the user's username and pass to the main csv file

        else:

            with open(
                    'users_info/user_information.csv',
                    'a', ) as check_account_existence:

                writer = csv.DictWriter(check_account_existence, fieldnames=fieldnames)
                # row['User Name'] = self.new_username
                writer.writerow({'User Name': self.new_username, 'Password': self.new_password})
            logging.warning("user added")

            # add the user's username and pass added to the user_accounts.csv
#
# mohammad = SignUp("MOHAMMAD", "ALI")
# mohammad.check_new_user_info()
# mehdi = SignUp("hossain", "ALI")
# mehdi.check_new_user_info()
