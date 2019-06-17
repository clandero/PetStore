from __future__ import print_function
from flask import Flask, request, jsonify, abort, render_template
from google.appengine.ext import ndb
from marshmallow import Schema, fields
import werkzeug
import logging
import requests
import httplib
import json
import sys
import requests_toolbelt.adapters.appengine

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

app = Flask(__name__)
app.debug = True

@app.route('/pets')
def get_pets():
	r = requests.get('http://practiceiv-on-gcloud.appspot.com/products/fetch')
	print(r.text,file=sys.stdout)
	return render_template('pets.html',products=json.loads(r.text)['products'])
	#return render_template('pets.html')

@app.route('/pets/cats')
def get_cats():
	r = requests.get('http://practiceiv-on-gcloud.appspot.com/products/get/specie/Cats')
	print(r.text,file=sys.stdout)
	return render_template('pet_specie.html',products=json.loads(r.text)['Cats'],specie="Cats")

@app.route('/')
def index():
	return render_template('index.html')


