from flask import Flask, render_template, request
import json
import csv
import sqlite3


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

    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Products")
            data = cursor.fetchall()
            data = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in data]
            conn.close()
        except sqlite3.Error as e:
            return render_template('product_display.html', error="Database error: {}".format(e))

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
