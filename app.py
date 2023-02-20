from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def get_ip():
    return request.remote_addr
