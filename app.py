import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return sys.version
