from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lon": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lon": -80.13},
    {"id": 3, "campus": "DC", "lat": 38.89, "lon": -77.01}
]

next_id = 4

@app.route("/")
def index():
    return """
        <h1> FIU Campuses API</h1>
        <p> Try these endpoints </p>
        <ul>
            <li><a href = "/hello">/hello</a></li>
            <li><a href = "/data">/data</a></li>
        """

@app.route("/hello")
def hello():
    return jsonify({"Hello": "world!"})

@app.route("/data")
def data():
    return jsonify(DATA), 200


if __name__ == '__main__':
    app.run(debug=True)
