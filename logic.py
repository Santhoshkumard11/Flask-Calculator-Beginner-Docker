from flask_restful import Resource
from flask import request, jsonify


# Checks whether the posted data is valid
def check_posted_data(posted_data, function_name):
    if function_name == "add" or function_name == "subtract" or function_name == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # Missing parameter
        else:
            return 200
    elif function_name == "division":
        if "x" not in posted_data or "y" not in posted_data:
            return 301
        elif int(posted_data["y"]) == 0:
            return 302
        else:
            return 200


# Math functions
class Add(Resource):
    def post(self):
        # If I am here, then the resouce Add was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        print(posted_data)

        # Steb 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "add")
        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Add the posted data
        ret = x+y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Subtract(Resource):
    def post(self):
        # If I am here, then the resource Subtract was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "subtract")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Subtract the posted data
        ret = x-y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Multiply(Resource):
    def post(self):
        # If I am here, then the resource Multiply was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "multiply")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Multiply the posted data
        ret = x*y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)


class Divide(Resource):
    def post(self):
        # If I am here, then the resource Divide was requested using the method POST

        # Step 1: Get posted data:
        posted_data = request.get_json()

        # Step 1b: Verify validity of posted data
        status_code = check_posted_data(posted_data, "division")

        if status_code != 200:
            ret_json = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If i am here, then status_code == 200
        x = posted_data["x"]
        y = posted_data["y"]
        x = int(x)
        y = int(y)

        # Step 2: Multiply the posted data
        ret = (x*1.0)/y
        ret_map = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(ret_map)

