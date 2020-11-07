from flask import render_template
from flask_cors import CORS
import flask
from dotenv import load_dotenv
from mongo import MongoClient
import json
import os
load_dotenv()

host = os.getenv('HOST')

db = MongoClient()

app = flask.Flask(__name__)
CORS(app)

if not host:
    app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def index():
    return render_template('stats.html')

@app.route('/followers-history', methods=['GET'])
def get_history():
    amounts = db.find(query={}, coll='amounts')
    return flask.jsonify(amounts)

@app.route('/latest', methods=['GET'])
def get_latest():
    latest = db.find(query={}, coll='amounts')[0]
    return flask.jsonify(latest)

if host:
    app.run(host='0.0.0.0')
else:
    app.run()
