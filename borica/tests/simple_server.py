# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    print(request.__dict__)
    return "Hello World!"


if __name__ == '__main__':
    app.run(port=9005)
