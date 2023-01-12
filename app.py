from products import products
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', )
def ping():
    return jsonify({'message': 'Pong!!!'})


@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({'status': 'SUCCESS', 'message': 'Product´s list', 'products': products})


@app.route('/products/<string:product_name>', methods=['GET'])
def getProduct(product_name):
    productsFound = [
        product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({'status': 'SUCCESS', 'message': 'Product', 'product': productsFound[0]})
    return jsonify({'status': 'FAILED', 'message': 'Product not found'})


@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity'],
    }
    products.append(new_product)
    return jsonify({'status': 'SUCCESS', 'message': 'Product added succesfully', 'products': products})


@app.route('/products/<string:product_name>', methods=['PUT'])
def updateProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({'status': 'SUCCESS', 'message': 'Product updated', 'product': productFound})

    return jsonify({'status': 'FAILED', 'message': 'Product not found'})


@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [
        product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({'status': 'SUCCESS', 'message': 'Product deleted', 'products': products})

    return jsonify({'status': 'FAILED', 'message': 'Product not found'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
