import queue
import math

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