import os
import math
import datetime
import pytz
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

gitpod_url = 'https://5000-cbeeb210-5c15-4820-9704-0260a4ea51d9.ws-eu01.gitpod.io/'

# Retain this sanity check to ensure the test module is working!
def check():
    return 1

def string_to_boolean(boolean_string):
    if boolean_string == "True":
         return True
    elif boolean_string == "False":
         return False
    else:
         raise ValueError("Cannot convert {} to a boolean.".format(boolean_string))
   
def roundup_nearest_ten(x):
    return int(math.ceil(x / 10.0)) * 10

def roundup_nearest_one(x):
    return int(math.ceil(x))

def compute_temperature_settings(temperature_value, temperature_type):

    if temperature_type == "celsius":
        return convert_from_celsius(temperature_value)

    if temperature_type == "celsius_fan":
        return convert_from_celsius_fan(temperature_value)

    if temperature_type == "fahrenheit":
        return convert_from_fahrenheit(temperature_value)

    if temperature_type == "gas_mark":
        return convert_from_gas_mark(temperature_value)

def create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type):

    temperature_object = {
        "celsius": str(celsius),
        "celsius_fan": str(celsius_fan),
        "fahrenheit": str(fahrenheit),
        "gas_mark": str(gas_mark),
        "user_temperature_type": user_temperature_type
    }
    return temperature_object

def convert_from_celsius(temperature_value):
    celsius = temperature_value
    celsius_fan = temperature_value - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 0
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_celsius_fan(temperature_value):
    celsius = temperature_value + 20
    celsius_fan = temperature_value
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 1
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_fahrenheit(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value - 32) * 5/9))
    celsius_fan = celsius - 20
    fahrenheit = temperature_value
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    user_temperature_type = 2
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

def convert_from_gas_mark(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value * 14) + 121))
    celsius_fan = celsius - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = temperature_value
    user_temperature_type = 3
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark, user_temperature_type)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", recipe=mongo.db.recipes.find_one({"popular_recipe": True, "archived": False}))

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find({"archived": False})))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipe_categories=list(mongo.db.recipe_categories.find()), usernames=list(mongo.db.users.find()))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    
    # Multi-line input elements need converted to a list before saving to MongoDB.
    ingredients = request.form.getlist("ingredients[]")
    method = request.form.getlist("method[]")

    temperature_value = int(request.form.get("temperature_value"))
    temperature_type = request.form.get("temperature_type")
    
    # Call temperature conversion functions to populate the temperature object.
    temperature_object = compute_temperature_settings(temperature_value, temperature_type)

    data = request.form.to_dict() 
    recipes.insert_one(
        {
            "category": data["category_name"],
            "title": data["title"],
            "description": data["description"],
            "ingredients": ingredients,
            "method": method,
            "temperature": temperature_object,
            "cooking_time": data["cooking_time"],
            "posted_by": data["username"],
            "date_posted": datetime.datetime.utcnow(),
            "popular_recipe": False,
            "archived": False
        }
    )    
    #return redirect(gitpod_url + 'recipe')
    return redirect(url_for('recipe'))

@app.route('/view_recipe/<_id>')
def view_recipe(_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(_id)})

    # The user_temperature_type variable determines the type the user originally selected
    # when adding the recipe to the database i.e. celsius, celsius fan, fahrenheit or gas mark. This 
    # is need when redisplaying the temperature for update because only one type is entered by the 
    # user when adding the recipe. The rest are derived by formulae.
    _user_temperature_type = _recipe["temperature"]["user_temperature_type"]

    if _user_temperature_type == 0:
        _temperature_value = _recipe["temperature"]["celsius"]

    if _user_temperature_type == 1:
        _temperature_value = _recipe["temperature"]["celsius_fan"]

    if _user_temperature_type == 2:
        _temperature_value = _recipe["temperature"]["fahrenheit"]

    if _user_temperature_type == 3:
        _temperature_value = _recipe["temperature"]["gas_mark"]

    _recipe_categories = mongo.db.recipe_categories.find()
    recipe_category_list = [recipe_category for recipe_category in _recipe_categories]
    return render_template("view_recipe.html", recipe = _recipe, user_temperature_type = _user_temperature_type, temperature_value = _temperature_value, recipe_categories = recipe_category_list, usernames=list(mongo.db.users.find()))

@app.route('/edit_recipe/<_id>')
def edit_recipe(_id):
    _recipe = mongo.db.recipes.find_one({"_id": ObjectId(_id)})

    # The user_temperature_type variable determines the type the user originally selected
    # when adding the recipe to the database i.e. celsius, celsius fan, fahrenheit or gas mark. This 
    # is need when redisplaying the temperature for update because only one type is entered by the 
    # user when adding the recipe. The rest are derived by formulae.
    _user_temperature_type = _recipe["temperature"]["user_temperature_type"]

    if _user_temperature_type == 0:
        _temperature_value = _recipe["temperature"]["celsius"]

    if _user_temperature_type == 1:
        _temperature_value = _recipe["temperature"]["celsius_fan"]

    if _user_temperature_type == 2:
        _temperature_value = _recipe["temperature"]["fahrenheit"]

    if _user_temperature_type == 3:
        _temperature_value = _recipe["temperature"]["gas_mark"]

    _recipe_categories = mongo.db.recipe_categories.find()
    recipe_category_list = [recipe_category for recipe_category in _recipe_categories]
    return render_template("edit_recipe.html", recipe = _recipe, user_temperature_type = _user_temperature_type, temperature_value = _temperature_value, recipe_categories = recipe_category_list, usernames=list(mongo.db.users.find()))

@app.route('/update_recipe/<_id>', methods=["POST"])
def update_recipe(_id):
    recipes = mongo.db.recipes

    # Multi-line input elements need converted to a list before saving to MongoDB.
    ingredients = request.form.getlist("ingredients[]")
    method = request.form.getlist("method[]")

    temperature_value = int(request.form.get("temperature_value"))
    temperature_type = request.form.get("temperature_type")
 
    # Call temperature conversion functions to populate the temperature object before update.
    temperature_object = compute_temperature_settings(temperature_value, temperature_type)
    
    recipes.replace_one({"_id": ObjectId(_id)},
    {
        "category": request.form.get("category_name"),
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "ingredients": ingredients,
        "method": method,
        "temperature": temperature_object,
        "cooking_time": request.form.get("cooking_time"),
        "posted_by": request.form.get("posted_by"),
        "date_posted": datetime.strptime(request.form.get("date_posted"), '%Y-%m-%d %H:%M:%S'),
        "date_last_updated": datetime.utcnow(),
        "popular_recipe": string_to_boolean(request.form.get("popular_recipe")),
        "archived": string_to_boolean(request.form.get("archived"))
    })
    #return redirect(gitpod_url + 'recipes')
    return redirect(url_for('recipes'))

@app.route('/archive_recipe/<_id>')
def archive_recipe(_id):
    recipes = mongo.db.recipes
    
    # Set the archived flag for this recipe.
    recipes.update_one({"_id": ObjectId(_id)},
    {"$set":
        {"archived": True}
    })
    
    # Refresh recipes page now that recipe has been archived and should no longer be displayed.
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find({"archived": False})))

@app.route('/delete_recipe/<_id>')
def delete_recipe(_id):

    mongo.db.recipes.delete_one({"_id:": ObjectId(_id)})

    # Refresh recipes page now that recipe has been deleted and should no longer be displayed.
    #return redirect(gitpod_url + 'recipes')
    return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)