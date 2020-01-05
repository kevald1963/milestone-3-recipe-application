import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

gitpod_url = 'https://5000-cbeeb210-5c15-4820-9704-0260a4ea51d9.ws-eu01.gitpod.io/'

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", recipe=mongo.db.recipes.find_one({'popular_recipe': True}))

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find()))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipe_categories=list(mongo.db.recipe_categories.find()))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    ingredients = request.form.to_dict["ingredients"]
    print("Ingredients: " + ingredients)
    data = request.form.to_dict() 
    recipes.insert_one(
        {
            "category": data["category_name"],
            "title": data["title"],
            "description": data["description"],
            "ingredients": ingredients
        }
    )    
    return redirect(gitpod_url + 'add_recipe')
    #return redirect(url_for('recipes'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)