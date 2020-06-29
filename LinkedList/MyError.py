class InsertError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class RemoveError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class IsEmpty(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message