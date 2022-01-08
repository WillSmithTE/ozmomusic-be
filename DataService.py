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
        logging.debug("parsedUrl=%s", parsedUrl)
        return self.youtubeDl.extract_info(
            parsedUrl,
            download=False
        )

# can save straight into io with this? https://github.com/ytdl-org/youtube-dl/issues/17379#issuecomment-521804927
    def downloadFile(self, url):
        parsedUrl = UrlParser.soundcloud(url)
        
        filename = str(uuid.uuid4())

        options = {'outtmpl': filename, 'format': 'mp3'}
        with youtube_dl.YoutubeDL(options) as ydl:
            metadata = ydl.extract_info(parsedUrl)

        return filename, metadata
