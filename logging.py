class Logging:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def check_username_password(self, username, password):
        if self.user_name == username and self.password == password:
            print("you logged successfully")
        else:
            print("try again")

            #user has the choice to not continue or enter the

