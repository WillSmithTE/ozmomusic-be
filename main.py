from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from DataService import DataService
import logging

logging.basicConfig()
logging.root.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

dataService = DataService()

@app.route("/api/media/metadata", methods=["GET"])
def getMetadata():
    url = request.args.get('url')
    logging.info("getMetadata (url=%s)", url)
    return jsonify(dataService.getMetadata(url))

@app.route("/api/media/download", methods=["GET"])
def getFile():
    url = request.args.get('url')

    message = None
    outdatedPlaceServices = dataService.getOutdatedPlaceServices()
    outdatedPlaces = list(map(lambda service : service.NAME, outdatedPlaceServices))
    if len(outdatedPlaceServices) > 0:
        dataService.updateData(outdatedPlaceServices)
        message = "Data has been refreshed for " + str(outdatedPlaces)
    else:
        message = "No new data found to refresh"
    logging.info(message)
    return json.dumps({"outdatedPlaces": outdatedPlaces}), 200, {"ContentType": "application/json"}


app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
