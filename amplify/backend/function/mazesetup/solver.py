from maze import rectMaze
import turtle
import tkinter
import prims_final
import time
#import ghostscript
#from PIL import Image
import io
import contextlib
import os
import pprint
import json
import requests
import ast
import re
import math
import queue
from dijkstra import dijkstra


if __name__ == "__main__":

    n = 20
    sideLen = 18

    rm = rectMaze(n, sideLen)
    #rm.t.pensize(2)
    #rm.t.hideturtle()
    #rm.t.speed(0)
    #rm.create_square()
    #rm.create_grid()
    rm.create_maze()
    #rm.save_screen()
    with contextlib.redirect_stdout(io.StringIO()) as f:
        pprint.pp(rm.serialise_cells())
    with contextlib.redirect_stdout(io.StringIO()) as f2:
        print(rm.serialise_cells())
    data = json.dumps(f.getvalue())
    #print(data)
    api_url = "http://localhost:5000/api/maze"
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Maze data successfully sent to Flask")
    else:
        print("Error when sending maze data to Flask")


    new_maze = f2.getvalue()
    new_maze = new_maze[1:len(new_maze)-2]
    p = re.compile('(?<!\\\\)\'')
    new_maze= ast.literal_eval(p.sub('\"', new_maze))
    new_maze_ids = []
    new_walls = []
    for i in range(len(new_maze)):
        new_maze_ids.append(new_maze[i]["id"])
        new_walls.append(new_maze[i]["walls"])
    new = []
    for i in range(int(math.sqrt(len(new_maze)))):
        for j in range(int(math.sqrt(len(new_maze)))):
            new.append([0, 0, 0, 0])

    end_val = n**2 - 1

    for i in range(len(new_maze)):
        if new_maze[i]["x"] != 0 and new_maze[i]["walls"][0] == 1:
            new_walls[i][0] = 1
        if new_maze[i]["y"] != 0 and new_maze[i]["walls"][1] == 1:
            new_walls[i][1] = 1
        if new_maze[i]["x"] != int(math.sqrt(len(new_maze))) - 1 and new_maze[i]["walls"][2] == 1:
            new_walls[i][2] = 1
        if new_maze[i]["y"] != int(math.sqrt(len(new_maze))) - 1 and new_maze[i]["walls"][3] == 1:
            new_walls[i][3] = 1
    #print(new_walls)
    #print(dijkstra(new_maze, new_maze_ids, 0, end_val, new_walls))
    final_path = json.dumps(dijkstra(new_maze, new_maze_ids, 0, end_val, new_walls))
    #print(final_path)
    path_url = "http://localhost:5000/api/data"

    response = requests.post(path_url, json=final_path)
    if response.status_code == 200:
        print("Path data successfully sent to Flask")
    else:
        print("Error when sending maze data to Flask2")