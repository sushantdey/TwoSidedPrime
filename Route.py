# using flask_restful
from flask import Flask
from flask_restful import Resource, Api
from controller.RestController import two_sided_prime


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
# resource to check if the number is Two Sided Prime
class TwoSidedPrime(Resource):

    def get(self, num):
        return two_sided_prime(num)


# adding the defined resources along with their corresponding urls
api.add_resource(TwoSidedPrime, '/twoSidedPrime/<int:num>')


# driver function
if __name__ == '__main__':
    app.run(debug=True)
