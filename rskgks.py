import turtle
import tkinter
import prims_final
import time
#import ghostscript
#from PIL import Image
import io
import os
import pprint

class rectMaze2:
    def __init__(self, n=10):
        self.n = n
        self.pr = prims_final.PrimsRandomized(self.n)
        self.grid = self.generateGrid()

    def generateGrid(self):
        grid = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                # Initialize cells with both left and bottom walls
                cell = {"wallLeft": True, "wallBottom": True}
                row.append(cell)
            grid.append(row)
        
        return grid

    def create_maze(self):
        self.mst = self.pr.prims_mst()

        for row in range(self.n):
            for col in range(self.n):
                node = row * self.n + col

                if self.mst[node][self.pr.LEFT] == 1:
                    self.grid[row][col]["wallLeft"] = False

                if self.mst[node][self.pr.BOTTOM] == 1:
                    self.grid[row][col]["wallBottom"] = False

    def print_maze(self):
        for row in self.grid:
            for cell in row:
                if cell["wallLeft"]:
                    print("|", end="")
                else:
                    print(" ", end="")
                if cell["wallBottom"]:
                    print("__", end="")
                else:
                    print("  ", end="")
            print("|")


yh = rectMaze2()
yh.create_maze()
yh.print_maze()