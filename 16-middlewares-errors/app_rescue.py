#!/usr/bin/python3
from flask import Flask, render_template, request
import time, random
app = Flask(__name__)


@app.route('/')
def bonjour():
        return "au feu les pompiers !!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
