# BEGIN CODE HERE
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT


import pymongo

# Replace these values with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/pspi"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Access or create a database
db = client["pspi"]

# Example: Inserting a document into a collection
collection = db["products"]
document = {"name": "example", "age": 25}
collection.insert_one(document)

# Example: Querying documents from the collection
query_result = collection.find({"age": {"$gt": 20}})
for doc in query_result:
    print(doc)




# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    return ""
    # END CODE HERE
