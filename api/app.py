from flask import Flask, jsonify

app = Flask(__name__)
@app.route("/details")
def details():
    detail = {"Name": "AlokK", "Age":18}
    return jsonify(detail)

