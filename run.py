import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI_BAKING_HOT")
app.config["MONGO_DBNAME"] = "baking_hot"

mongo = PyMongo(app)

@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html", recipe=mongo.db.recipes.find_one({'popular_recipe': True}))

@app.route('/recipes')
def recipes():
    return render_template("recipes.html", recipes=list(mongo.db.recipes.find()))

@app.route('/add_recipe')
def add_recipe():
    return render_template("add_recipe.html", recipe_types=list(mongo.db.recipe_types.find()))

@app.route('/insert_recipe', methods=["POST"])
def insert_recipe():
    recipes = mongo.db.recipes
    # Convert form data to a dictionary to make it usable by Mongo.
    recipes.insert_one(request.form.to_dict())
    #return redirect(gitpod_url + 'recipes')
    return redirect(url_for('recipes'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)