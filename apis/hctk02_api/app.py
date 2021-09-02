from flask import Flask, jsonify
from flask_restplus import Api
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import default_exceptions
from missingdata import ns

app = Flask(__name__)
app.config["RESTPLUS_VALIDATE"] = True
api = Api(
    app,
    version="1.0",
    title="Hackathon 2 - Data Wrangling",
    description="Api to handle missing data in the dataset"
)
CORS(app)


@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code


for ex in default_exceptions:
    app.register_error_handler(ex, handle_error)

api.add_namespace(ns)

if __name__ == "__main__":
    app.run()
