import random

class Maze:
    def __init__(self,rows=10,cols=10):
        self.rows=rows
        self.cols=cols
        self.grid=[[0]*cols]*rows

    def carve_passages_from(self,cx,cy):
        direction_dict = {'N':[1][0], 'S':[-1][0], 'E':[0][1], 'W':[0][-1]}
        for i in range(4):
            self.directions=random.choice(['N','S','E','W'])
            nx, ny = cx + direction_dict[self.directions][0], cy + direction_dict[self.directions][1]
            if (nx >= 0 and nx <= self.rows) and (ny >= 0 and nx <= self.cols) and (ny,nx) not in self.grid:
                self.grid[cy][cx] += [direction_dict[self.directions][1]][direction_dict[self.directions][0]]
                nx, ny = nx - direction_dict[self.directions][0], nx - direction_dict[self.directions][1]
                self.carve_passages_from(self,cx,cy)

z = Maze()

def emit_maze(grid, width, height):
    maze = ""
    maze += " " + "_" * (width * 2 - 1) + "\n"
    for y in range(height):
        maze += "|"
        for x in range(width):
            if grid[y][x] & S != 0:
                maze += " "
            else:
                maze += "_"
            if grid[y][x] & E != 0:
                if (grid[y][x] | grid[y][x+1]) & S != 0:
                    maze += " "
                else:
                    maze += "_"
            else:
                maze += "|"
        maze += "\n"
    return maze