#Python API by Sayan Banerjee
import flask
from flask import request, jsonify
from flask_restful import Api, Resource, reqparse
import random

app = flask.Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

# Test data.
product = [
    {'id': 0,
     'name': 'iPhone 12',
     'description': 'Apple iPhone 12 64GB Blue',
     'category': 'Premium Smartphone',
     'brand': 'Apple',
     'size': 'N/A',
     'gender': 'Unisex',
     'image': 'https://www.apple.com/in/'},

    {'id': 1,
     'name': 'iPhone 12 mini',
     'description': 'Apple iPhone 12 mini 64GB Blue',
     'category': 'Premium Smartphone',
     'brand': 'Apple',
     'size': 'N/A',
     'gender': 'Unisex',
     'image': 'https://www.apple.com/in/'},

    {'id': 2,
     'name': 'iPhone 12 pro',
     'description': 'Apple iPhone 12 pro 128GB Blue',
     'category': 'Premium Smartphone',
     'brand': 'Apple',
     'size': 'N/A',
     'gender': 'Unisex',
     'image': 'https://www.apple.com/in/'},

    {'id': 3,
     'name': 'iPhone 11 pro',
     'description': 'Apple iPhone 11 pro 128GB Gold',
     'category': 'Premium Smartphone',
     'brand': 'Apple',
     'size': 'N/A',
     'gender': 'Unisex',
     'image': 'https://www.apple.com/in/'},

    {'id': 4,
     'name': 'iPhone 11',
     'description': 'Apple iPhone 11 pro 128GB Product Red',
     'category': 'Premium Smartphone',
     'brand': 'Apple',
     'size': 'N/A',
     'gender': 'Unisex',
     'image': 'https://www.apple.com/in/'}



]
#test
"""
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to Python API POC</h1>
    <p>This is created as a part of Assignment by Blueconch Technologies by Sayan Banerjee</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/products', methods=['GET'])
def api_all():
    return jsonify(product)

app.run()
"""




class Product(Resource):

    def get(self, id=0):
        if id == 0:
            return (product), 200

        for pr in product:
            if pr["id"] == id:
                return pr, 200
        return "Product not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("description")
        parser.add_argument("category")
        parser.add_argument("brand")
        parser.add_argument("size")
        parser.add_argument("gender")
        parser.add_argument("image")
        params = parser.parse_args()
        for pr in product:
            if id == pr["id"]:
                return f"Product with id {id} already exists", 400
        product_in = {
            "id": int(id),
            "name": params["name"],
            "description": params["description"],
            "category": params["category"],
            "brand": params["brand"],
            "size": params["size"],
            "gender": params["gender"],
            "image": params["image"]
        }
        product.append(product_in)
        return product, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("description")
        parser.add_argument("category")
        parser.add_argument("brand")
        parser.add_argument("size")
        parser.add_argument("gender")
        parser.add_argument("image")
        params = parser.parse_args()
        for pr in product:
            if (id == pr["id"]):
                pr["name"] = params["name"]
                pr["description"] = params["description"]
                pr["category"] = params["category"]
                pr["brand"] = params["brand"]
                pr["size"] = params["size"]
                pr["gender"] = params["gender"]
                pr["image"] = params["image"]
                return pr, 200

        product_in = {
            "id": int(id),
            "name": params["name"],
            "description": params["description"],
            "category": params["category"],
            "brand": params["brand"],
            "size": params["size"],
            "gender": params["gender"],
            "image": params["image"]
        }

        product.append(product_in)
        return product, 201

    def delete(self, id):
        global product
        product = [pr for pr in product if pr["id"] != id]
        return f"Product with id {id} is deleted.", 200


api.add_resource(Product, "/product", "/product/", "/product/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)
