# import necessary libraries
import os
import numpy as np
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.preprocessing import MinMaxScaler



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")
# need routes for all html pages



# Query the database and send the jsonified results
@app.route("/send", methods=["POST"])
def send():

    if request.method == "POST":
        ohu2010 = request.form["OHU2010"]
        numgqtrs = request.form["NUMGQTRS"]
        familyincome = request.form["MedianFamilyIncome"]
        tractKids = request.form["TractKids"]
        seniors = request.form["TractSeniors"]
        tractwhite = request.form["TractWhite"]
        tractblack = request.form["TractBlack"]
        tractasian = request.form["TractAsian"]
        tracthopi = request.form["TractNHOPI"]
        trackaian = request.form["TractAIAN"]  
        multir = request.form["TractOMultir"]
        hispanic = request.form["TractHispanic"]
        tractHUNV = request.form["TractHUNV"]
        snap = request.form["TractSNAP"]
        distance = request.form["distance"]
        busstop = request.form["bus_stops"]
        storecount = request.form["store_count"]
             


    input_data = np.array([ohu2010,
                  numgqtrs,
                    familyincome,
                    tractKids,
                    seniors,
                    tractwhite,
                    tractblack,
                    tractasian,
                    tracthopi,
                    trackaian,  
                    multir,
                    hispanic,
                    tractHUNV,
                    snap,
                    distance,
                    busstop,
                    storecount])

    
    X = input_data.reshape(1,-1)
    print(X)
    
    X = scaler.transform(X)
    
    prediction = loaded_model.predict(X).tolist()
    print (prediction)
    
    if prediction[0]== 1: 
        prediction = "Food Desert"
    else: 
        prediction = "Not a Food Desert"
    
    results = {"prediction":prediction}
    return render_template("foodcalculator.html", results=results)

@app.route("/about.html")
def about():
       
   return render_template("about.html")

@app.route("/foodstory.html")
def foodstory():
       
   return render_template("foodstory.html")

@app.route("/geomap.html")
def geomap():
       
   return render_template("geomap.html")

@app.route("/foodcalculator.html")
def foodcalculator():
       
   return render_template("foodcalculator.html")

@app.route("/research.html")
def research():
       
   return render_template("research.html")

@app.route("/traditional.html")
def traditional():
       
   return render_template("traditional.html")


if __name__ == "__main__":
    scaler = pickle.load(open("x_scale.sav", 'rb'))
    loaded_model = pickle.load(open("logistic_regression.sav", 'rb'))
    app.run()
