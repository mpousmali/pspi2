# BEGIN CODE HERE
from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
import base64
import uuid
from selenium import webdriver


import pymongo

# Replace these values with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/pspi"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Access or create a database
db = client["pspi"]

# Example: Inserting a document into a collection
collection = db["products"]
#document = {"id":"1","name": "f","production_year":2,"price":2,"color":1, "size":2}
#collection.insert_one(document)

#new_product = {}
#new_product["id"] = "1"
#new_product["name"] = "A4"
#if (db.products.find({"name":new_product['name']}) is True):
#    db.products.update_one ({"name":"paper"}, 
#                           {'$set': {"production_year": 2023, "price":2, "color":2, "size":2}})
#else:
#    new_product["production_year"] = 2023
#    new_product["price"] = 2
#    new_product["color"] = 2
#    new_product["size"] = 2
#    collection.insert_one(new_product)


# Example: Querying documents from the collection
#query_result = collection.find({"age": {"$gt": 20}})
#for doc in query_result:
#    print(doc)



# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])


@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
     get_search= request.args.get("search")
     search=get_search.lower()
     print(search)
     products = []
     query_result = collection.find({}, {'_id':0,'name': 1}).sort({"age":-1})
     index=0 
     for doc in query_result:
        if search in doc.get('name'):
            apot=collection.find({"name":doc.get('name')})
            for k in apot:
               id=k.get('id')
               name=k.get('name')
               production_year=k.get('production_year')
               price=k.get('price')
               color=k.get('color')
               size=k.get('size')
               products.append(id)
               products.append(name)
               products.append(production_year)
               products.append(price)
               products.append(color)
               products.append(size)
               #index,{"id": id, "name": name,"production_year": production_year, "price": price, "color": color , "size": size }
               #index=index+1
     for i in products:
      print(i)
     if not products:
        return jsonify([])
     return jsonify(products)
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    #if (request.method=="POST"):
    #information=request.form
    #data = request.get_json()
    #if (not data):
    #    return jsonify('error')
    #new_product = {}
    #new_product["id"] = "1"
    #new_product["name"] = request.args.get('name')
    #if (db.products.find({"name":new_product['name']}) is True):
    #    mongo.db.products.update_one ({"name":request.form['inputName']},
    #                       {'$set': {"production_year": request.form['inputProductionYear'], "price":request.form['inputPrice'], "color":request.form['inputColor'], "size":request.form['inputSize']}})   
    #else:
    #    new_product["production_year"] = request.form['inputProductionYear']
    #    new_product["price"] = request.form['inputPrice']
    #    new_product["color"] = request.form['inputColor']
    #    new_product["size"] = request.form['inputSize']
    #    mongo.db.products.insert_one(new_product)
    #print("hi")
    
    #return jsonify(new_product)

    #return render_template("products.html",data=information)
    str = request.args.get('name')
    str_lower=str.lower()
    #id=base64.urlsafe_b64encode(uuid.uuid1().bytes)
    #str_id=id.replace('=', '')
    #str_id=str_id[:5]
    #id="a1"
    index = str_lower.find('/')


    inputName = str_lower[:index]
    parts = str_lower.split('/')

    # Initialize a dictionary to hold the key-value pairs
    new_person = {}
    #new_person['id']=str_id
    new_person['name']=inputName
    #new_person['id']=str(id)
    
    # Loop through the parts and extract key-value pairs
    for i in parts[1:]:
        key, value = i.split('=')
        new_person[key] = value
    exists = mongo.db.products.find_one({"name": new_person.get('name')})
    if exists is None:
        mongo.db.products.insert_one(new_person)
    else:
        mongo.db.products.update_one ({"name":new_person.get('name')},
                           {'$set': {"production_year": new_person.get('production_year'),
                                      "price":new_person.get('price'), 
                                      "color":new_person.get('color'), 
                                      "size":new_person.get('size')}})
    return jsonify({"message":"success"})


if (__name__=='__main__'):
    app.run(debug=True,  host='127.0.0.1', port=5000)
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