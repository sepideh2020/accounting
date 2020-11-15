from logging import Logging


class Signup(Logging):
    def __init__(self, new_username, new_password, user_name, password):
        super().__init__(user_name, password)
        self.new_username = new_username
        self.new_password = new_password

    def check_new_user_info(self, user_username, user_password):
        # check in the main csv file
        if self.new_password == self.user_name:
            print("username already exists,enter a new user name")
        # while the username already exists ask the user to choose a username
        else:
            self.new_username = user_username
            self.new_password = user_password
        # add the user's username and pass to the main csv file
