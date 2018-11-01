from tkinter import *
import random
import time

class Item:
    def __init__(self, canvas):
        self.canvas = canvas

class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.canvas_height = 400
        self.canvas_width = 500
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.hit_bottom = False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # returns coordinates of the ball ex.:[255.0, 29.0, 270.0, 44.0] first
        # two coordinates are top left coords and next two are bottom right
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if self.hit_paddle(pos):
            self.y = -2


def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
        if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
            return True
        return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = 500
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
    
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        if self.canvas.coords(self.id)[0] <= 0:
            self.x = 0
        if self.canvas.coords(self.id)[2] >= self.canvas_width:
            self.x = 0

def move_left(self, evt):
    if self.canvas.coords(self.id)[0] >= 0:
        self.x = -3
    
    def move_right(self, evt):
        if self.canvas.coords(self.id)[2] < self.canvas_width:
            self.x = 3

class Brick(Item):
    def __init__(self, canvas, color, pos1,pos2,pos3,pos4):
        self.canvas = canvas
        self.brick = canvas.create_rectangle(pos1,pos2,pos3,pos4,fill=color)
        super(Brick, self).__init__(canvas)

# def collide(self):



tk = Tk()

# adds title to the window
tk.title('Bouncing Ball')

# make the window non-resizable both horizontally and vertically
tk.resizable(0, 0)

# extra named parameters don't allow border
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
paddle = Paddle(canvas, color='black')
ball = Ball(canvas, color='blue', paddle=paddle)
brick1 = Brick(canvas, "black",70,80,100,120)
# MAIN LOOP

while True:
    if not ball.hit_bottom:
        tk.update()
        ball.draw()
        paddle.draw()
    else:
        exit()
    '''
        the commands update_idletasks and update tell tkinterto
        hurry up and draw what is on the canvas.'''
    time.sleep(0.01)  # so that animation is not that fast
