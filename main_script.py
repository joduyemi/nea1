import math
import maze
import json
import simplejson
from solver import dijkstra
from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})