from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as f:
        data = json.load(f)
    return render_template('items.html', items=data["items"])


@app.route('/products')
def products():
    source = request.args.get('source')
    products_id = request.args.get('id')
    
    if source == 'json':
        with open('products.json') as f:
            data = json.load(f)

    elif source == 'csv':
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            data = list(reader)

    else:
        return render_template('product_display.html', error="Wrong source")
    
    if products_id:
        data = [product for product in data if str(product['id']) == str(products_id)]
        if not data:
            error = "Product not found"
            return render_template('product_display.html', error=error)
        
    return render_template('product_display.html', products=data)



if __name__ == '__main__':
    app.run(debug=True, port=5000)
