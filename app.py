import flask
from dotenv import load_dotenv
from mongo import MongoClient
import json


db = MongoClient()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/followers-history', methods=['GET'])
def get_history():
    amounts = db.find(query={}, coll='amounts')
    return flask.jsonify(amounts)

@app.route('/latest', methods=['GET'])
def get_latest():
    latest = db.find(query={}, coll='amounts')[0]
    return flask.jsonify(latest)
    
app.run()
