#Import Dependencies
# The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
# The second line says we'll use PyMongo to interact with our Mongo database.
# The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#Setup Flask
app = Flask(__name__)

## Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL.
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app"
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Set Up App routes
#mars = mongo.db.mars.find_one() uses PyMongo to find the "mars" collection in our database,
#  which we will create when we convert our Jupyter scraping code to Python Script.
#return render_template("index.html" tells Flask to return an HTML template using an index.html file. 
# We'll create this file after we build the Flask routes.
#mars=mars tells python to use the "mars collection in mongo db"
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)
#the above funtction links our visual representation of our work(our web app), to the code that powers it

#mars = mongo.db.mars assigns a variable that points to our mars database
#Next, we created a new variable to hold the newly scraped data: mars_data = scraping.scrape_all().    
# #(Note: .scrape_all is referencing the function in the scraping.py file exported form jupyter notebook)
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)
#redirect takes us back to the / after the scrape
# Syntax to update database   .update(query_parameter, data, options)


#This tells flask to run
if __name__ == "__main__":
   app.run()

