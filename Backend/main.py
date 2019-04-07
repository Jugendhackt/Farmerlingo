# First install necessary packages

# pip install flask

# Import the modules
from flask import Flask, jsonify, request
from flask_cors import CORS

# create the app. This variable named jh constains our app
jh = Flask(__name__)

CORS(jh)


producerDict = dict(name='producer', producers=[])
foodDict = dict(name = 'availableFood', foods=[])
# foodPriceDict = dict(banana = 50, apple = 100, rice = 40)

producerIdCounter = 0

# add routes to our app
@jh.route('/')
def hello_world():
    return 'Hello, World!'

@jh.route('/producers')
def producers():
    return jsonify(producerDict)

@jh.route('/producer/add')
#Diese Funktion erstellt einen neuen Produzenten. Dafuer erwartet sie den Namen (String und eindeutig), Telefonnummer (int), Ort(String), Passwort(String)
def add_producer():
    args = request.args.to_dict()
    name = args['name']
    for i in producerDict['producers']:
        if i['name'] == name:
            return jsonify(dict(error=True, message="Name already taken, choose another one"))
    phoneNumber = args['phoneNumber']
    place = args['place']
    password = args['place']
    newProducer = dict(name = name, place = place, phoneNumber = phoneNumber, password = password)
    #producerIdCounter = producerIdCounter + 1
    producerDict['producers'].append(newProducer)
    return 'Added producer {}'.format(name)


# @jh.route('/foodPriceDict')
# def foodPriceDict():
#     return jsonify(foodPriceDict)


@jh.route('/food')
def food():
    return jsonify(foodDict)

@jh.route('/food/add')
def add_food():
    args = request.args.to_dict()
    type = args['type']
    # found = False
    # for i in foodPriceDict:
    #     if i == type:
    #         found = True
    # if not found:
    #     return jsonify(dict(error = True, message = "We don't have this product yet :("))
    amount = args['amount']
    price = args['price']
    # producer = args['producer']
    # for i in producerDict['producers']:
    #     if i['name'] == producer:
    #         newProduct = dict(type=type, amount = amount, price = price, producer = i)
    #         foodDict['foods'].append(newProduct)
    #         return 'Added food {}'.format(type)
    # return jsonify(dict(error=True, message= "no producer with this name found"))
    newProduct = dict(type=type, amount = amount, price = price)
    foodDict['foods'].append(newProduct)
    return 'Added food {}'.format(type)

# This comment a comment
# Run the app if someone runs this file.
if __name__ == "__main__":
    jh.run(debug=True)

# to run call: python filename.py
