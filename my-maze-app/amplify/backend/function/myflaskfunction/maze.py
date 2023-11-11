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
#home = os.environ['HOME']
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
        self.pr = prims_final.PrimsRandomized(self.n)
        #window = tkinter.Tk()
        #canvas = tkinter.Canvas(master = window, width = 800, height = 800)
        #canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
        #self.t = turtle.RawTurtle(canvas)

    '''
    def create_square(self):
        side = self.sideLen * 5
        x = - side / 2
        y = side / 2

        t.penup()
        t.goto(x,y)
        t.pendown()

        for i in range(4):
            t.forward(side)
            t.right(90)

    def create_grid(self):
        x = - (self.n * self.sideLen) / 2
        y = - x

        t.penup()
        t.goto(x,y)

        for row in range(self.n):
            for col in range(self.n):
                t.pendown()

                t.forward(self.sideLen)
                t.right(90)
                t.forward(self.sideLen)
                t.right(90)
                t.forward(self.sideLen)
                t.right(90)
                t.forward(self.sideLen)
                t.right(90)
                t.penup()

                t.forward(self.sideLen)
            y += self.sideLen
            t.goto(x, y)
    
    '''
    def create_maze(self):
        self.mst = self.pr.prims_mst()
        
        '''
        x = - (self.n / 2) * self.sideLen
        y = - x
        self.t.penup()
        self.t.goto(x,y)

        for row in range(self.n):
            for col in range(self.n):
                node = row * self.n + col
                current_row = node // self.n
                current_col = node % self.n

                self.t.pendown()

                if self.mst[node][self.pr.TOP] == 1 or (current_row > 0 and self.mst[node][self.pr.TOP] == 0 and self.mst[node-4][self.pr.BOTTOM] == 0):
                    self.t.penup()

                self.t.forward(self.sideLen)
                self.t.right(90)

                self.t.pendown()

                if self.mst[node][self.pr.RIGHT] == 1 or node == self.n **2 - 1:
                    self.t.penup()

                self.t.forward(self.sideLen)
                self.t.right(90)

                self.t.pendown()

                if self.mst[node][self.pr.BOTTOM] == 1:
                    self.t.penup()

                self.t.forward(self.sideLen)
                self.t.right(90)

                self.t.pendown()

                if self.mst[node][self.pr.LEFT] == 1 or node == 0 or (current_col > 0 and self.mst[node][self.pr.LEFT] == 0 and self.mst[node-1][self.pr.RIGHT] == 0):
                    self.t.penup()

                self.t.forward(self.sideLen)
                self.t.right(90)

                self.t.penup()
                self.t.forward(self.sideLen)

                x += self.sideLen
                self.t.penup()
                self.t.goto(x,y)
            x -= self.sideLen * self.n
            y -= self.sideLen
            self.t.goto(x,y)
    def save_screen(self):
        ts = self.t.getscreen()
        cv = ts.getcanvas()
        cv.postscript(file="C:\\Users\\jodu0\\Desktop\\nea\\f.eps")
        im = "C:\\Users\\jodu0\\Desktop\\nea\\f.eps"
        eps_image = Image.open(im)
        img = eps_image.convert("RGB")
        img.save("C:\\Users\\jodu0\\Desktop\\nea\\f.jpg", lossless=True)
    '''
    

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
    '''
    def print_maze(self):
        self.mst = self.pr.prims_mst()


        for row in range(self.n):
            for col in range(self.n):
                node = row * self.n + col
                current_row = node // self.n
                current_col = node % self.n

                if self.mst[node][self.pr.TOP] == 1 or (current_row > 0 and self.mst[node][self.pr.TOP] == 0 and self.mst[node-4][self.pr.BOTTOM] == 0):
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if self.mst[node][self.pr.RIGHT] == 1 or node == self.n **2 - 1:
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if self.mst[node][self.pr.BOTTOM] == 1:
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if self.mst[node][self.pr.LEFT] == 1 or node == 0 or (current_col > 0 and self.mst[node][self.pr.LEFT] == 0 and self.mst[node-1][self.pr.RIGHT] == 0):
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.penup()
                t.forward(self.sideLen)

                x += self.sideLen
                t.penup()
                t.goto(x,y)
            x -= self.sideLen * self.n
            y -= self.sideLen
            t.goto(x,y)
    '''
    



