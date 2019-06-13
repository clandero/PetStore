from __future__ import print_function
from flask import Flask, request, jsonify, abort, render_template
from google.appengine.ext import ndb
from marshmallow import Schema, fields
import werkzeug
import logging
import requests
import json
import sys

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
	r = requests.get('http://practiceiv-on-gcloud.appspot.com/products/fetch')
	return render_template('index.html',products=json.loads(r.text)['products'])
	