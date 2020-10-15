from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Weather API!<br/><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )




if __name__ == "__main__":
    app.run(debug=True)