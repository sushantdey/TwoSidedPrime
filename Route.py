# using flask_restful
from flask import Flask, jsonify
from flask_restful import Resource, Api
from controller.RestController import hello_world
from controller.RestController import two_sided_prime


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        return jsonify({'message': hello_world()})


# another resource to check if the number is Two Sided Prime
class TwoSidedPrime(Resource):

    def get(self, num):
        return jsonify({'Two Sided Prime': two_sided_prime(num)})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(TwoSidedPrime, '/twoSidedPrime/<int:num>')


# driver function
if __name__ == '__main__':
    app.run(debug=True)
