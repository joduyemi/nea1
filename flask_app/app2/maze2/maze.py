from .prims_final import PrimsRandomized
class Cell:
    def __init__(self, x, y, walls, id):
        self.x = x
        self.y = y
        self.walls = walls
        self.id = id

    def serialise(self):
        return {
            "x": self.x,
            "y": self.y,
            "walls": self.walls,
            "id":self.id,
        }

class rectMaze:
    def __init__(self, n=10, sideLen=10):
        self.n = n
        self.sideLen = sideLen
        self.pr = PrimsRandomized(self.n)


    def create_maze(self):
        self.mst = self.pr.prims_mst()
    

    def serialise_cells(self):
        count = 0
        serialised_cells = []
        for i in range(self.pr.total_nodes):
            x = self.pr.position[i][0]
            y = self.pr.position[i][1]
            walls = self.mst[i]

            curr_cell = Cell(x, y, walls, count)
            curr_cell.serialise()
            serialised_cells.append(curr_cell.serialise())
            count += 1
        return serialised_cells
    



