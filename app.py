import os
from flask import Flask, request, jsonify
from flask_cors import cross_origin
import module as md

app = Flask(__name__)


@app.route("/")
@cross_origin()
def index():
    return {
        "status_code": 200,
        "message": "Success!"
    }


@app.route("/summarize", methods=["POST"])
@cross_origin()
def summarization():
    input_request = request.get_json()
    input_text = input_request["text"]
    if request.method == "POST":
        if input_text is None:
            json = {
                "data": "",
                "message": "Input text cannot be empty",
                "status_code": 400
            }
            return jsonify(json)
        else:
            summarized = md.summarize(text=input_text)
            json = {
                "result": summarized
            }
            return jsonify(json)
    else:
        json = {
            "data": "",
            "message": "Method not allowed",
            "status_code": 405
        }
        return jsonify(json)


@app.errorhandler(400)
def bad_request(error):
    return {
        "status_code": 400,
        "message": "Client side error!"
    }, 400


@app.errorhandler(404)
def not_found(error):
    return {
        "status_code": 404,
        "message": "URL not found"
    }, 404


@app.errorhandler(405)
def method_not_allowed(error):
    return {
        "status_code": 405,
        "message": "Request method not allowed!"
    }, 405


@app.errorhandler(500)
def internal_server_error(error):
    return {
        "status_code": 500,
        "message": "Server error"
    }, 500


if __name__ == "__main__":
    app.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
