from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import json
import os
from DataService import DataService
import logging
import mimetypes
import io

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1000 * 1000 # max size 500 MB

dataService = DataService()


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({'message': 'hi'})


@app.route("/api/media/metadata", methods=["GET"])
def getMetadata():
    url = request.args.get('url')
    logging.info("getMetadata (url=%s)", url)
    return jsonify(dataService.getMetadata(url))


@app.route("/api/media/download", methods=["GET"])
def getFile():
    url = request.args.get('url')
    logging.info("getFile (url=%s)", url)

    filePath, metadata = dataService.downloadFile(url)

    data = io.BytesIO()
    with open(filePath, 'rb') as fo:
        data.write(fo.read())

    # (after writing, cursor will be at last byte, so move it to start)
    data.seek(0)

    os.remove(filePath)

    extension = metadata.get("ext")
    mimetype = mimetypes.guess_extension(extension)
    extractor = metadata.get("extractor")
    songId = metadata.get("id")

    return send_file(
        data,
        as_attachment=True,
        download_name=extractor + "_" + songId + "." + extension,
        mimetype=mimetype
    )

if os.environ.get("LOCAL") == "True":
    logging.debug("In local mode, starting server")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
