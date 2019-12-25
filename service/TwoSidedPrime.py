from math import sqrt
from math import floor


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


def check_prime(num):
    for i in range(2, floor(sqrt(num)+1)):
        if num % i == 0:
            return False
    return True

