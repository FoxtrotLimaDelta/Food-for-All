6# import necessary libraries
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

from config import username, password

#engine = create_engine(os.environ.get('DATABASE_URL', ''))


engine = create_engine(f'postgresql://{username}:{password}@localhost:5433/petpals')

Base = automap_base()
Base.prepare(engine, reflect=True)

Pet = Base.classes.pets

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("foodcalculator.html")

# Query the database and send the jsonified results
@app.route("/send", methods=["GET", "POST"])
def send():

    session = Session(engine)

    if request.method == "GET":
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
             


 pet = Pet(name=name, lat=lat, lon=lon)
        session.add(pet)
        session.commit()

        session.close()



        return redirect("/", code=302)
loading up a value and passing in the prediction 
    return render_template("foodcalculator.html", answer = predictedvalue)


@app.route("/api/pals")
def pals():

    session = Session(engine)

    results = session.query(Pet.name, Pet.lat, Pet.lon).all()

    names = [result[0] for result in results]
    lat = [result[1] for result in results]
    lon = [result[2] for result in results]

    pet_data = {
        "latitude": lat,
        "longitude": lon,
        "hover_text": names
    }

    session.close()

    return jsonify(pet_data)


if __name__ == "__main__":
    app.run()
