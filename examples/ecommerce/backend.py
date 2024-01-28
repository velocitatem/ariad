from flask import Flask, request, jsonify
app = Flask(__name__)

# Mock database
products_db = {}

@app.route('/add_product', methods=['POST'])
def add_product():
    product = request.json
    product_id = product.get('ProductId')
    products_db[product_id] = product
    return jsonify({'message': 'Product added successfully.', 'ProductId': product_id})

@app.route('/get_product/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_db.get(product_id, {})
    if product:
        return jsonify(product)
    return jsonify({'message': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
