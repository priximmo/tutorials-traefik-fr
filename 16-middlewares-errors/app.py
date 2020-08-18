#!/usr/bin/python3
from flask import Flask, render_template, request
import time, random
app = Flask(__name__)

liste_code = [ 200, 200, 200, 404 ]

@app.route('/')
def bonjour():
        number = random.randint(0,3)
        ip = request.remote_addr
        origin=request.headers.get('X-Forwarded-For', request.remote_addr)
        time.sleep(number)
        return origin + " via "+ ip + " latency " + str(number) + " s", liste_code[number]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

