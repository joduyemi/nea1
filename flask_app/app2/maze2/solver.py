from .maze import rectMaze
import io
import contextlib
import pprint
import json
import requests
import ast
import re
import math
import queue


def generate_maze(n, sideLen):


    rm = rectMaze(n, sideLen)
    rm.create_maze()
    with contextlib.redirect_stdout(io.StringIO()) as f:
        pprint.pp(rm.serialise_cells())
    with contextlib.redirect_stdout(io.StringIO()) as f2:
        print(rm.serialise_cells())
    data = json.dumps(f.getvalue())
    #print(data)
    api_url = "https://8fs6lykh95.execute-api.eu-west-2.amazonaws.com/Prod/api/maze"
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
    path_url = "https://8fs6lykh95.execute-api.eu-west-2.amazonaws.com/Prod/api/data"

    response = requests.post(path_url, json=final_path)
    if response.status_code == 200:
        print("Path data successfully sent to Flask")
    else:
        print("Error when sending maze data to Flask2")

def handle_maze_generation_event(event):
    if event["event"] == "maze_generation":
        data = event["data"]
        n = data["n"]
        sideLen = data["sideLen"]
        
        generate_maze(n, sideLen)



def dijkstra(maze, ids, start, end, new_walls):
    priority_queue = queue.PriorityQueue()
    distance = {cell:float('inf') for cell in ids}
    parent = {}
    row_len = int(math.sqrt(len(ids)))
    visited = []
    count = 0
    distance[start] = 0
    priority_queue.put((start, 0))
    while not priority_queue.empty():
        #print("Count: " + str(count))
        count += 1
        #print(priority_queue.queue)
        #print(distance)
        current = priority_queue.get()
        #print(current)
        if current[0] == end:
            break
        no = 0
        for i in range(len(maze)):
            if maze[i]["id"] == current[0]:
                no = i
                #print(no)
                visited.append(no)
                #print(visited)
                for j in range(4):
                    if new_walls[no][j] == 1:
                        if j == 0:
                            neighbour = no - row_len
                        elif j == 1:
                            neighbour = no - 1
                        elif j == 2:
                            neighbour = no + row_len
                        elif j == 3:
                            neighbour = no + 1

                        if neighbour not in visited:
                            #print("Neigbour: "+ str(neighbour))
                            tentative_distance = current[1] + 1
                            #print("Tentative distance: " + str(tentative_distance))
                            #print("Current distance: "+ str(distance[neighbour]))

                            if tentative_distance < distance[neighbour]:
                                distance[neighbour] = tentative_distance
                                parent[neighbour] = current[0]
                                priority_queue.put((neighbour, tentative_distance))
                        else:
                            continue
                        
                    
    if end not in parent.keys():
        return None
    
    path = []
    current = end
    while current:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path
    

def lambda_handler(event, context):
    # Existing code
    # ...

    handle_maze_generation_event(event)
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Maze generation completed successfully"})
    }

    # Existing code
    # ...