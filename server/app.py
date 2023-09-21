#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string_hello>')
def print_string(string_hello):
    print(string_hello)
    return string_hello

@app.route('/<int:integer_num>')
def count(integer_num):
    return "<br>".join(str(i)for i in range(1, integer_num + 1))

@app.route('/math/<float:num1><string:operator><float:num2>')
def math(num1, operator, num2):
    if operator == "+":
        result=num1 + num2
    elif operator == "-":
        result=num1 - num2
    elif operator == "*":
        result=num1 * num2
    elif operator == "div":
        result=num1 / num2
    elif operator == "%":
        result=num1 % num2

    else:
        return "Invalid input"
    return str(result)

    


if __name__ == '__main__':
    app.run(port=5555, debug=True)
