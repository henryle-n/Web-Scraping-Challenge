# import dependencies
from flask import Flask, render_template, request, redirect
from get_mars_data import get_data
from load_mongo_db import load_new_data
import load_mongo_db

# Create a Flask app instance
app = Flask(__name__)


# Route to render index.html template using data from Mongo
@app.route("/")
def home_page():

    # Find one record of data from the mongo database
    return_data = get_data()

    # Return template and data
    return render_template("index.html", mars_data=return_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def new_data():

    # Run the scrape function
    new_data = load_new_data()

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)