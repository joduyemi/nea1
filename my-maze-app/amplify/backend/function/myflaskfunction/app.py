 
import math
import maze
import json
import simplejson
from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

maze_data = {}
path_data = []


@app.route("/api/maze", methods=["POST", "GET"])
def maze_data_handler():
    global maze_data
    if request.method == "POST":
        data = request.json
        maze_data = json.loads(json.dumps(data, indent=4))
        return jsonify({"message": "Maze data successfully received"})
    elif request.method == "GET":
        return jsonify({"maze_data": maze_data})


@app.route("/api/data", methods=["POST", "GET"])
def path_data_handler():
    global path_data
    if request.method == "POST":
        path_data = request.json
        path_data = json.dumps(path_data)
        return jsonify({"message": "Path data successfully received"})
    elif request.method == "GET":
        return jsonify(data=path_data)

@app.route("/")
def index():
    row_len = int(math.sqrt(len(maze_data)))
    return render_template('index.html', row_len=row_len)

@app.route("/about/")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)