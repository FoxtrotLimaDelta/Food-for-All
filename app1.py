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

#from config import username, password
from config import pswrd, port, sql

#engine = create_engine(os.environ.get('DATABASE_URL', ''))
engine = create_engine(f'postgresql://postgres:{pswrd}@localhost:{port}/{sql}')


Base = automap_base()
Base.prepare(engine, reflect=True)

Desert = Base.classes.deserts

 # Flask Routes

@app.route("/")
def welcome():
    
    """List all available API routes."""
    
    return (
        f"Welcome to your Latitude Dashboard!:<br/>"
        f"/api/v1.0/about<br/>"
        f"/api/v1.0/{sql}<br/>"
        f"/api/v1.0/contact"
    )
    
      
@app.route("/api/v1.0/about")

def about():
   name = "Flynn LLC"
   location = "Arizona"
   
   return f"We are {name} and we are located in sunny {location}."


@app.route("/api/v1.0/{sql}")
def data():
    # Create our session (link) from Python to the DB
    #session = Session(engine)
results = session.query(desert.columnName, desert.columnName).all()


@app.route("/api/v1.0/contact")
def contact():
   email = "Flynnworking@gmail.com"
     
   return f"Questions, Comments, Complaints? Send an email to {email}."

if __name__ == "__main__":
    
 app.run(debug=True)