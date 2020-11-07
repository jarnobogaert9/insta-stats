import flask
from dotenv import load_dotenv
from mongo import MongoClient
import json
# import os
# load_dotenv()


db = MongoClient()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/followers-history', methods=['GET'])
def get_history():
    amounts = db.find(query={}, coll='amounts')
    print(amounts)
    return flask.jsonify(amounts)

app.run()
