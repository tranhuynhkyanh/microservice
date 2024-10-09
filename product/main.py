import os
import random
from dataclasses import dataclass

from dotenv import load_dotenv
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
import requests

from product.producer import publish

load_dotenv()
app = Flask(__name__)

# Cấu hình SQLAlchemy với biến môi trường
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
CORS(app)


@dataclass
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')


@app.route('/api/products', methods=['GET'])
def index():
    products = Product.query.all()
    return jsonify(products)


@app.route('/api/product/<int:product_id>/like', methods=['POST'])
def like(product_id):
    randomId = random.randint(1, 5)
    productUser = ProductUser(user_id=randomId, product_id=product_id)
    db.session.add(productUser)
    db.session.commit()

    publish('product_liked', product_id)
    return jsonify({
        'message': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8002)
