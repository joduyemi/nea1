import turtle
import tkinter
import sbfl
import time
from PIL import Image

window = tkinter.Tk()
canvas = tkinter.Canvas(master = window, width = 800, height = 800)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
t = turtle.RawTurtle(canvas)

class rectMaze:
    def __init__(self, n=10, sideLen=10):
        self.n = n
        self.sideLen = sideLen

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
    
    def create_maze(self):
        pr = sbfl.PrimsRandomized(self.n)
        mst = pr.prims_mst()

        x = - (self.n / 2) * self.sideLen
        y = - x
        t.penup()
        t.goto(x,y)

        for row in range(self.n):
            for col in range(self.n):
                node = row * self.n + col
                current_row = node // self.n
                current_col = node % self.n

                t.pendown()

                if mst[node][pr.TOP] == 1 or (current_row > 0 and mst[node][pr.TOP] == 0 and mst[node-4][pr.BOTTOM] == 0):
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if mst[node][pr.RIGHT] == 1 or node == self.n **2 - 1:
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if mst[node][pr.BOTTOM] == 1:
                    t.penup()

                t.forward(self.sideLen)
                t.right(90)

                t.pendown()

                if mst[node][pr.LEFT] == 1 or node == 0 or (current_col > 0 and mst[node][pr.LEFT] == 0 and mst[node-1][pr.RIGHT] == 0):
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

if __name__ == '__main__':
    t.pensize(2)
    t.hideturtle()
    t.speed(0)

    n = 10
    sideLen = 20

    rm = rectMaze(n, sideLen)
    # rm.create_square()
    # rm.create_grid()
    rm.create_maze()
    canvas.postscript('x.eps', width=1000, height=1000)
    img = Image.open('x.eps')
    img.save('x.jph')

    t.done()