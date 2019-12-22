import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/whitebreadrecipes')
def whitebreadrecipes():
    return render_template("whitebreadrecipes.html")

@app.route('/wholemealrecipes')
def wholemealrecipes():
    return render_template("wholemealrecipes.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)