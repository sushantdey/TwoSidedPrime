# A python program to create user-defined exception
# class MyError is derived from super class Exception


class InvalidInputError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)
