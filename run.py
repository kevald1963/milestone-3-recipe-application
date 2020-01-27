import os
import pytz
from datetime import datetime
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

from utils.general import test_checker, string_to_boolean, roundup_nearest_ten, roundup_nearest_one
from utils.temperature_conversions import compute_temperature_settings, create_temperature_object, convert_from_celsius, convert_from_celsius_fan, convert_from_fahrenheit, convert_from_gas_mark

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

# Show the 'Home' page. 
@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", recipe=mongo.db.recipes.find_one({"popular_recipe": True, "archived": False}))

# Show the 'Recipes' page. 
# Invoked primarily from the Nav bar.
@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find({"archived": False})))

# Show the 'Add recipe' page. 
# Invoked from 'Recipes' page.
@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipe_categories=list(mongo.db.recipe_categories.find()), usernames=list(mongo.db.users.find()))

# Insert the recipe and return to the 'Recipes' page.
# Invoked from 'Add recipe' page.
@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    
    # Multi-line input elements need converted to a list before saving to MongoDB.
    ingredients = request.form.getlist("ingredients[]")
    method = request.form.getlist("method[]")
    equipment = request.form.getlist("equipment[]")
    
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
            "equipment": equipment,
            "temperature": temperature_object,
            "cooking_time": data["cooking_time"],
            "posted_by": data["username"],
            "date_posted": datetime.utcnow(),
            "popular_recipe": False,
            "archived": False
        }
    )    
    return redirect(url_for('recipes'))

# Show either the 'View or Edit recipe' page. These are differentiated by the 
# mode argument passed from the appropriate page. 
# Invoked from 'Recipes' page.
@app.route('/view_or_edit_recipe/<_id>/<mode>')
def view_or_edit_recipe(_id, mode):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(_id)})

    # The user_temperature_type variable determines the type the user originally selected
    # when adding the recipe to the database i.e. celsius, celsius fan, fahrenheit or gas mark. This 
    # is need when redisplaying the temperature for update because only one type is entered by the 
    # user when adding the recipe. The rest are derived by formulae.
    user_temperature_type = recipe["temperature"]["user_temperature_type"]

    if user_temperature_type == 0:
        temperature_value = recipe["temperature"]["celsius"]

    if user_temperature_type == 1:
        temperature_value = recipe["temperature"]["celsius_fan"]

    if user_temperature_type == 2:
        temperature_value = recipe["temperature"]["fahrenheit"]

    if user_temperature_type == 3:
        temperature_value = recipe["temperature"]["gas_mark"]

    recipe_categories = mongo.db.recipe_categories.find()
    recipe_category_list = [recipe_category for recipe_category in recipe_categories]
    if mode == "view":
        template = "view_recipe.html"
    if mode == "edit":
        template = "edit_recipe.html"

    return render_template(template, recipe = recipe, user_temperature_type = user_temperature_type, temperature_value = temperature_value, recipe_categories = recipe_category_list, usernames=list(mongo.db.users.find()))

# Update the recipe and return to the 'Recipes' page.
# Invoked from 'Edit recipe' page.
@app.route('/update_recipe/<_id>', methods=["POST"])
def update_recipe(_id):
    recipes = mongo.db.recipes

    # Multi-line input elements need converted to a list before saving to MongoDB.
    ingredients = request.form.getlist("ingredients[]")
    method = request.form.getlist("method[]")
    equipment = request.form.getlist("equipment[]")

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
        "equipment": equipment,
        "temperature": temperature_object,
        "cooking_time": request.form.get("cooking_time"),
        "posted_by": request.form.get("posted_by"),
        "date_posted": datetime.strptime(request.form.get("date_posted"), '%Y-%m-%d %H:%M:%S.%f'),
        "date_last_updated": datetime.utcnow(),
        "popular_recipe": string_to_boolean(request.form.get("popular_recipe")),
        "archived": string_to_boolean(request.form.get("archived"))
    })
    return redirect(url_for('recipes'))

# Set the recipe to 'archived', so that it's hidden, and return to the 'Recipes' page.
# Invoked from 'Recipes' page.
@app.route('/archive_recipe/<_id>')
def archive_recipe(_id):
    recipes = mongo.db.recipes
    
    # Set the archived flag for this recipe.
    recipes.update_one({"_id": ObjectId(_id)},
    {"$set":
        {"archived": True}
    })
    
    # Refresh recipes page now that recipe has been archived and should no longer be displayed.
    return redirect(url_for('recipes'))

# Delete the recipe and return to the 'Recipes' page.
# Invoked from 'Recipes' page.
@app.route('/delete_recipe/<_id>')
def delete_recipe(_id):

    result = mongo.db.recipes.delete_one({"_id:": ObjectId(_id)})
    print("result = " + str(result))

    # Refresh recipes page now that recipe has been deleted and should no longer be displayed.
    return redirect(url_for('recipes'))

# Show the 'Recipe category' page. 
# Invoked primarily from the Nav bar.
@app.route('/recipe_categories')
def recipe_categories():
    return render_template("recipe_categories.html", recipe_categories=list(mongo.db.recipe_categories.find()))

# Show the 'Add recipe category' page. 
# Invoked from 'Category' page.
@app.route('/add_recipe_category')
def add_recipe_category():
    return render_template("add_recipe_category.html")

# Insert the recipe category and return to the 'Recipe categories' page.
# Invoked from 'Add recipe category' page.
@app.route('/insert_recipe_category', methods=["POST"])
def insert_recipe_category():
    recipe_categories = mongo.db.recipe_categories
    recipe_category = {"category_name": request.form.get('category_name')}
    recipe_categories.insert_one(recipe_category)
    return redirect(url_for('recipe_categories'))

# Show the 'Edit recipe category' page.
# Invoked from 'Recipe category' page.
@app.route('/edit_recipe_category/<recipe_category_id>')
def edit_recipe_category(recipe_category_id):
    return render_template("edit_recipe_category.html", recipe_category = mongo.db.recipe_categories.find_one({"_id": ObjectId(recipe_category_id)}))

# Update the recipe category and return to the 'Recipe categories' page.
# Invoked from 'Edit recipe category' page.
@app.route('/update_recipe_category/<recipe_category_id>', methods=["POST"])
def update_recipe_category(recipe_category_id):
    mongo.db.recipe_categories.update(
        {'_id': ObjectId(recipe_category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('recipe_categories'))

# Delete the recipe category and return to the 'Recipe categories' page.
# Invoked from 'Recipe category' page.
@app.route('/delete_recipe_category/<recipe_category_id>')
def delete_recipe_category(recipe_category_id):
    mongo.db.recipe_categories.delete_one({'_id': ObjectId(recipe_category_id)})
    return redirect(url_for('recipe_categories'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=os.environ.get('PORT', "5000"),
            debug=True)

