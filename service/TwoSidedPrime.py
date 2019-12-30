# service functions responsible for executing the business logic and evaluate the result
from math import sqrt
from math import floor

# accept the request from controller
# call other service functions (if required) to execute business logic
# return evaluated result back to controller function
# obtain all possible numbers by left and right-truncation


def check_two_sided_prime(num: int):
    test_str = str(num)
    length = len(test_str)
    for i in range(length):
        temp = int(test_str[i:length])
        if not (check_prime(temp)):
            return False
        temp = int(test_str[0:length-i])
        if not (check_prime(temp)):
            return False
    return True


# check whether each number (original, left-truncated and right-truncated) is prime


def check_prime(num):
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

