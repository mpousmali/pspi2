# BEGIN CODE HERE
from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import pymongo

# Replace these values with your MongoDB connection string
mongo_uri = "mongodb://localhost:27017/pspi"

# Connect to MongoDB
client = pymongo.MongoClient(mongo_uri)

# Access or create a database
db = client["pspi"]

# Αρχικοποίηση του Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

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

request = {
    "id": str,
    "name": str, 
    "production_year": int, 
    "price": int, 
    "color": int, 
    "size": int
 }

json_str = request

# Λήψη των δεδομένων από το body του request
data = request

# Υπολογισμός της ομοιότητας για κάθε προϊόν στη βάση δεδομένων
similarity_scores = {}
for product in db.products.find():
    # Υπολογισμός της ομοιότητας με βάση τον αλγόριθμο Content Based Filtering
    # με τη χρήση της βιβλιοθήκης numpy
    input_vector = np.array([
        data['id'],
        data['name'],
        data['production_year'],
        data['price'],
        data['color'],
        data['size']
    ])
    product_vector = np.array([
        product['id'],
        product['name'],
        product['production_year'],
        product['price'],
        product['color'],
        product['size']
    ])
    cosine_similarity = np.dot(input_vector, product_vector) / (np.linalg.norm(input_vector) * np.linalg.norm(product_vector))
    # Επιστρέφει μια τιμή μεταξύ 0 και 1 που αντιπροσωπεύει την ομοιότητα
    similarity_scores[product['name']] = cosine_similarity

    # Επιλογή των προϊόντων με ομοιότητα πάνω από 70%
    similar_products = [name for name, similarity in similarity_scores.items() if similarity > 0.7]


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
    #id=np.randint(10000, 100000)
    #str_id=str(np.randint(10000, 100000))
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
    if (new_person['size'].lower()=='small'):
        new_person['size']=1
    elif (new_person['size'].lower()=='medium'):
        new_person['size']=2
    elif (new_person['size'].lower()=='large'):
        new_person['size']=3
    elif (new_person['size'].lower()=='extra large'):
        new_person['size']=4
    else:
        new_person['size']=int(new_person['size'])

    if (new_person['color'].lower()=='blue' or new_person['color'].lower()=='μπλε'):
        new_person['color']=3
    elif (new_person['color'].lower()=='red' or new_person['color'].lower()=='κοκκινο' or new_person['color'].lower()=='κόκκινο'):
        new_person['color']=1
    elif (new_person['color'].lower()=='yellow' or new_person['color'].lower()=='κιτρινο' or new_person['color'].lower()=='κίτρινο'):
        new_person['color']=2
    else:
        new_person['color']=int(new_person['color'])

    new_person['production_year']=int(new_person['production_year'])
    new_person['price']=float(new_person['price'])

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
    # Λήψη των δεδομένων από το body του request
    #data = request.json

    # Υπολογισμός της ομοιότητας για κάθε προϊόν στη βάση δεδομένων
    #similarity_scores = {}
    #for product in mongo.db.products.find():
        # Υπολογισμός της ομοιότητας με βάση τον αλγόριθμο Content Based Filtering
        #similarity = calculate_similarity(data, product)
        #similarity_scores[product['name']] = similarity

    # Επιλογή των προϊόντων με ομοιότητα πάνω από 70%
    #similar_products = [name for name, similarity in similarity_scores.items() if similarity > 0.7]

    #return jsonify(similar_products)
    return " "
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    semester = request.args.get('semester', type=int)
    if semester is None:
        return jsonify({'error': 'Parameter "semester" is required'}), 400

    url = 'https://qa.auth.gr/el/x/studyguide/600000438/current'
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get(url)

    try:
        #Αναζήτηση για τα μαθήματα του συγκεκριμένου εξαμήνου
        wait = WebDriverWait(driver, 10)
        semester_xpath = f"//div[@data-semester='{semester}']//a[@class='course']"
        courses_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, semester_xpath)))
        
        courses = [course.text for course in courses_elements]
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        driver.quit()

    return jsonify(courses)
    # END CODE HERE