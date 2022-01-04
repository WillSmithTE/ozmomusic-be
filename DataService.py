import requests
from UrlParser import UrlParser
from util import read, save
from flask import Flask
from flask_cors import CORS
import json
import os
from datetime import datetime
import youtube_dl
from contextlib import redirect_stdout
from io import BytesIO
import logging
import uuid

class DataService:

    def __init__(self):
        self.youtubeDl = youtube_dl.YoutubeDL({})

    def getMetadata(self, url):
        parsedUrl = UrlParser.soundcloud(url)
        return self.youtubeDl.extract_info(
            parsedUrl,
            download=False
        )

    def downloadFile(self, url):
        parsedUrl = UrlParser.soundcloud(url)
        
        filename = str(uuid.uuid4())

        options = {'outtmpl': filename}
        with youtube_dl.YoutubeDL(options) as ydl:
            metadata = ydl.extract_info(parsedUrl)

        logging.debug("getFile (metadata=%s)", metadata)
        return filename, metadata
