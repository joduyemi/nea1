import math
import maze
import json
import simplejson
from flask import Flask, render_template, send_from_directory, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

maze_data = {}

@app.route("/api/maze", methods=["POST"])
def receive_maze_data():
    global maze_data
    data = request.json
    maze_data = json.loads(simplejson.dumps(data, iterable_as_array=True, indent=4))
    print(maze_data)
    return jsonify({"message": "Maze data succesfully received"})

@app.route("/api/maze", methods=["GET"])
def get_maze_data():
    global maze_data
    print(maze_data)
    return jsonify({"maze_data": maze_data})

@app.route("/")
def index():
    row_len = int(math.sqrt(len(maze_data)))
    return render_template('index.html', row_len=row_len)

@app.route("/about/")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)