import os
import math
import datetime
import pytz
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

gitpod_url = 'https://5000-cbeeb210-5c15-4820-9704-0260a4ea51d9.ws-eu01.gitpod.io/'

def roundup_nearest_ten(x):
    return int(math.ceil(x / 10.0)) * 10

def roundup_nearest_one(x):
    return int(math.ceil(x))

def compute_temperature_settings(temperature_value, temperature_type):

    if temperature_type == "celsius":
        return convert_from_celsius(temperature_value)

    if temperature_type == "celsius-fan":
        return convert_from_celsius_fan(temperature_value)

    if temperature_type == "fahrenheit":
        return convert_from_fahrenheit(temperature_value)

    if temperature_type == "gas-mark":
        return convert_from_gas_mark(temperature_value)

def create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark):
    temperature_object = {
        "celsius": str(celsius),
        "celsius_fan": str(celsius_fan),
        "fahrenheit": str(fahrenheit),
        "gas_mark": str(gas_mark)
    }
    return temperature_object

def convert_from_celsius(temperature_value):
    celsius = temperature_value
    celsius_fan = temperature_value - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark)

def convert_from_celsius_fan(temperature_value):
    celsius = temperature_value + 20
    celsius_fan = temperature_value
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark)

def convert_from_fahrenheit(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value - 32) * 5/9))
    celsius_fan = celsius - 20
    fahrenheit = temperature_value
    gas_mark = roundup_nearest_one(int((celsius - 121) / 14))
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark)

def convert_from_gas_mark(temperature_value):
    celsius = roundup_nearest_ten(int((temperature_value * 14) + 121))
    celsius_fan = celsius - 20
    fahrenheit = roundup_nearest_ten(int((celsius * 9/5) + 32))
    gas_mark = temperature_value
    return create_temperature_object(celsius, celsius_fan, fahrenheit, gas_mark)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", recipe=mongo.db.recipes.find_one({'popular_recipe': True}))

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find()))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipe_categories=list(mongo.db.recipe_categories.find()), usernames=list(mongo.db.users.find()))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    
    # Multi-line input elements need converted to a list before saving to MongoDB.
    ingredients = request.form.getlist("ingredients[]")
    method = request.form.getlist("method[]")

    temperature_value = int(request.form.get("temperature-value"))
    temperature_type = request.form.get("temperature-type")
    
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
            "popular_recipe": False
        }
    )    
    return redirect(gitpod_url + 'recipe')
    #return redirect(url_for('recipe'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    _recipe = mongo.db.recipe.find_one({"_id": ObjectId(_id)})
    _recipe_categories = mongo.db.recipe_categories.find()
    recipe_category_list = [recipe_category for recipe_category in _recipe_categories]
    return render_template("edit_recipe.html", recipe=_recipe, recipe_categories = recipe_category_list)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_task(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({"_id": ObjectId(_id)},
    {
        "category": request.form.get("category_name"),
        "title": request.form.get("title"),
        "description": request.form.get("description"),
        "ingredients": ingredients,
        "method": method,
        "temperature": temperature_object,
        "cooking_time": request.form.get("cooking_time"),
        "posted_by": request.form.get("username"),
        "date_posted": request.form.get("date_posted"),
        "date_last_updated": datetime.datetime.utcnow(),
        "popular_recipe": request.form.get("popular_recipe")
    })
    return redirect(gitpod_url + 'recipes')
    #return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)