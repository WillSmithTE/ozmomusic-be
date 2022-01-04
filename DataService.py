import requests
from util import read, save
from flask import Flask
from flask_cors import CORS
import json
import os
from datetime import datetime
import youtube_dl

class DataService:

    def __init__(self):
        self.youtubeDl = youtube_dl.YoutubeDL({})

    def getMetadata(self, url):
        return self.youtubeDl.extract_info(
        url,
        download=False
    )
