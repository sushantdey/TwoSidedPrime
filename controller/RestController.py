# accept request from route
# call service functions to execute business logic and get the response
# return appropriate response back to route/ view
from flask import jsonify
from service.TwoSidedPrime import check_two_sided_prime

# define a function to get request from route and return response back
# call appropriate service function to execute business logic(check two sided prime) and get response


def two_sided_prime(num: int):
    return jsonify({'Two Sided Prime':check_two_sided_prime(num)})

