# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("foodcalculator.html")
# need routes for all html pages



# Query the database and send the jsonified results
@app.route("/send", methods=["POST"])
def send():

    if request.method == "POST":
        ohu2010 = request.form["OHU2010"]
        numgqtrs = request.form["NUMGQTRS"]
        familyincome = request.form["MedianFamilyIncome"]
        seniors = request.form["TractSeniors"]
        tractwhite = request.form["TractWhite"]
        tractblack = request.form["TractBlack"]
        tractasian = request.form["TractAsian"]
        tracthopi = request.form["TractNHOPI"]
        trackaian = request.form["TractAIAN"]  
        multir = request.form["TractOMultir"]
        hispanic = request.form["TractHispanic"]
        snap = request.form["TractSNAP"]
        busstop = request.form["bus_stops"]
        storecount = request.form["store_count"]
             


    input_data = [ohu2010,
                  numgqtrs,
                    familyincome,seniors,
                    tractwhite,
                    tractblack,
                    tractasian,
                    tracthopi,
                    trackaian,  
                    multir,
                    hispanic,
                    snap,
                    busstop,
                    storecount]



    return jsonify(input_data)


if __name__ == "__main__":
    app.run()
