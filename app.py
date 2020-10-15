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
    results = session.query(meas.date,meas.prcp).filter(meas.date>="2016-08-23").all()
    session.close()

    pecipDict={}
    for measurments in results:
         pecipDict[measurments.date]=measurments.prcp

    return jsonify(pecipDict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(stat.station).all()
    session.close()

    statList=[]
    for station in results:
        statList.append(station[0])
    
    return jsonify(statList)

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)
    results = session.query(meas.date,meas.tobs).filter(meas.date>="2016-08-23",meas.station=="USC00519281").all()
    session.close()

    tobsDict={}
    for measurments in results:
         tobsDict[measurments.date]=measurments.tobs

    return jsonify(tobsDict)



if __name__ == "__main__":
    app.run(debug=True)