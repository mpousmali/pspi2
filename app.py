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

mongo_uri = "mongodb://localhost:27017/pspi"


client = pymongo.MongoClient(mongo_uri)

db = client["pspi"]

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

collection = db["products"]

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
     products = []
     query_result = collection.find({}, {'_id':0,'name': 1}).sort({"price":-1}) 
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
               products.append({"id":id,"name": name,"production_year":production_year,"price":price,"color":color,"size":size})
     #print(products)
     if not products:
        return jsonify([])
     return jsonify(products)
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    str = request.args.get('name')
    str_lower=str.lower()
    query_result = collection.find({})
    i=0
    for doc in query_result:
        i=i+1
    i=i+1
    id= "% s" % i
    index = str_lower.find('/')


    inputName = str_lower[:index]
    parts = str_lower.split('/')

    new_person = {}
    new_person['id']=id
    new_person['name']=inputName
    
    
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

    request = {
       "id": str,
        "name": "str", 
       "production_year": 5, 
       "price": 2, 
       "color": 2, 
       "size": 2
    }

    json_str = request

    data = request

    similarity_scores = {}
    for product in db.products.find():

     input_vector = np.array([
        data['id'],
        np.array(data['name']),
        np.array(data['production_year']),
        np.array(data['price']),
        np.array(data['color']),
        np.array(data['size'])
    ])
    product_vector = np.array([
        product['id'],
        np.array(product['name']),
        np.array(product['production_year']),
        np.array(product['price']),
        np.array(product['color']),
        np.array(product['size'])
    ])
    cosine_similarity = np.dot(input_vector, product_vector) / (np.linalg.norm(input_vector) * np.linalg.norm(product_vector))
    
    similarity_scores[product['name']] = cosine_similarity

    similar_products = [name for name, similarity in similarity_scores.items() if similarity > 0.7]

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