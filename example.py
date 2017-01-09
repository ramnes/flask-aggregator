from flask import Flask, request
from flask_aggregator import Aggregator

app = Flask(__name__)
Aggregator(app=app, endpoint="/batch")


@app.route("/hello/<name>", methods=["GET"])
def hello_name(name):
    response = "Hello, {}!".format(name)
    question = request.args.get("question")
    if question:
        response += " " + question
    return response


if __name__ == "__main__":
    app.run()
