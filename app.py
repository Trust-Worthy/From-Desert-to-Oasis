
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
    """
    Should display a map of the zip code and all of the grocery stores
    that were compared against that zip code
    """
    return render_template("map.html")




if __name__ == "__main__":
    app.run()