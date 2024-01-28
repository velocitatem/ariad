Let's create a basic e-commerce platform structure using Python, Flask for the backend, and a simple HTML page for the front end to handle adding and retrieving products.

### Backend with Flask

First, we'll set up the backend functionalities using Flask. Ensure you have Flask installed (`pip install Flask`) before proceeding.

backend.py
---
```python
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
```

### Frontend Interface

Next, we'll create a simple HTML page for adding and displaying product information. This part will communicate with the Flask backend for operations.

index.html
---
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-Commerce Platform</title>
</head>
<body>
    <h2>Add Product</h2>
    <form id="addProductForm">
        Name:<br>
        <input type="text" id="name"><br>
        Price:<br>
        <input type="number" id="price"><br>
        Description:<br>
        <input type="text" id="description"><br>
        <button type="button" onclick="addProduct()">Add Product</button>
    </form>
    
    <h2>Get Product</h2>
    Product ID:<br>
    <input type="text" id="getProductId"><br>
    <button type="button" onclick="getProduct()">Get Product</button>
    
    <div id="productDetails"></div>
    
    
    <script>
        function addProduct() {
            var name = document.getElementById('name').value;
            var price = document.getElementById('price').value;
            var description = document.getElementById('description').value;
            var product = {
                ProductId: new Date().getTime().toString(), // Simple product ID generator
                Name: name,
                Price: price,
                Description: description
            };
            fetch('/add_product', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(product),
            })
            .then(response => response.json())
            .then(data => alert(JSON.stringify(data)));
        }

        function getProduct() {
            var productId = document.getElementById('getProductId').value;
            var url = '/get_product/' + productId;
            fetch(url)
            .then(response => response.json())
            .then(data => {
                var details = document.getElementById('productDetails');
                details.innerHTML = JSON.stringify(data);
            });
        }
    </script>
</body>
</html>
```

### Integration

1. Run the backend server by executing `python backend.py`.
2. Open the `index.html` file in a browser to interact with the backend.

This solution covers a simplified version of the project requirements. It includes adding products to a backend database (mocked as a Python dictionary) and retrieving them. The frontend portion enables users to interact with the backend using basic HTML and JavaScript.