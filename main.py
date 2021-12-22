from flask import Flask
from flask.json import jsonify
from data import data
app = Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message":"success"
    }),200
if __name__ == "__main__":
    app.run()