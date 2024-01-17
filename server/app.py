#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:str>")
def print_string(str):
    print(str)
    return str


@app.route("/count/<int:count>")
def count(count):
    result = ""
    for i in range(count):
        result += f"{i}\n"
    return result


@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    operations = {
        "+": str(num1 + num2),
        "-": str(num1 - num2),
        "*": str(num1 * num2),
        "div": str(num1 / num2),
        "%": str(num1 % num2),
    }
    return operations[operation] if operation in operations else "Not a valid operation"


if __name__ == "__main__":
    app.run(port=5555, debug=True)
