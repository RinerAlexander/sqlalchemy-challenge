from flask import Flask, jsonify

import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

meas = Base.classes.measurement
stat = Base.classes.station

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Weather API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)
    results = session.query(meas.date,meas.prcp).all()

    session.close()

    pecipDict={}
    for measurments in results:
         pecipDict[measurments.date]=measurments.prcp

    return jsonify(pecipDict)



if __name__ == "__main__":
    app.run(debug=True)