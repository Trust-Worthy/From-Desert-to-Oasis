
import math
from flask import Flask, render_template, request
from requests import Session


app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the home page
    :return:
    """
    return render_template('index.html')
@app.route("/food_desert")
def food_desert():
    return render_template("index.html")
# @app.route("/eval_food_desert")
# def is_food_desert():
    



if __name__ == "__main__":
    app.run()