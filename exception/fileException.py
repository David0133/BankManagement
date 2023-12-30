class WrongInput(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(message)



# raise WrongInput("Invalid option please enter a valid response")
class EmptyString(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NotValidMob(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NumNotAllow(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
