from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color, paddle, block):
        self.canvas = canvas
        self.paddle = paddle
        self.block = block
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.canvas_height = 400
        self.canvas_width = 500
        starts = [1]
        random.shuffle(starts)
        self.x =  1  #starts[0]
        self.y = -1
        self.hit_bottom = False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        # returns coordinates of the ball ex.:[255.0, 29.0, 270.0, 44.0] first
        # two coordinates are top left coords and next two are bottom right
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -1
        if self.hit_paddle(pos):
            self.y = -1
        if self.hit_brick(pos) == 4:
            self.x = 1
        if self.hit_brick(pos) == 3:
            self.x = -1
        if self.hit_brick(pos) == 1:
            self.y = -1
        if self.hit_brick(pos) == 2:
            self.y = 1



    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def hit_brick(self,pos):

        brick1 = [50, 85, 100, 100, "red"]
        brick2 = [100, 85, 150, 100]
        brick3 = [150, 85, 200, 100]
        brick4 = [300, 85, 350, 100]
        brick5 = [200, 85, 250, 100]
        brick6 = [250, 85, 300, 100]
        brick7 = [50, 130, 100, 145]
        brick8 = [50,55,100,70]
        brick9 = [50,40,100,55]

        brick_pos = [brick1,brick2,brick3,brick4,brick5,brick6,brick7,brick8,brick9]
        for l in brick_pos: #iterate through list
            if pos[3] == l[1] and l[0] <= pos[0] <= l[2]: #for a hit from over
                return 1
            if pos[1] == l[3] and l[0] <= pos[0] <= l[2]: #for a hit from under
                return 2
            if pos[2] == l[0] and l[1] <= pos[1] <= l[3]: #for a hit from right side
                return 3
            if pos[0] == l[2] and l[1] <= pos[1] <= l[3]: #for a hit from left side
                return 4


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_height = 400
        self.canvas_width = 500
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= 500:
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def move_left(self, evt):
        self.x = -3

    def move_right(self, evt):
        self.x = 3

    def move_up(self, evt):
        self.y = -3

    def move_down(self, evt):
        self.y = 3

    def stop_paddle(self, evt):
        self.y = 0
        self.x = 0


class Obstacle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color


class Block(Obstacle):
    def __init__(self, pos1, pos2, pos3, pos4, color):
        super().__init__(canvas, color)
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(pos1,pos2,pos3,pos4, fill=color)

class Brick(Obstacle):
    pass


tk = Tk()

tk.title('Bouncing Ball')
tk.resizable(0, 0)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
block = Block
paddle = Paddle(canvas, color='black')
ball = Ball(canvas, color='blue', paddle=paddle, block=block)

brick8 = Block(50, 55, 100, 70, "green")
brick9 = Block(50, 40, 100, 55, "green")
brick1 = Block(50, 85, 100, 100, "green")
brick2 = Block(100, 85, 150, 100, "green")
brick3 = Block(150, 85, 200, 100, "green")
brick4 = Block(300, 85, 350, 100,"green")
brick5 = Block(200, 85, 250, 100, "green")
brick6 = Block(250, 85, 300, 100, "green")
brick7 = Block(50, 130, 100, 145, "black")


while True:
    if not ball.hit_bottom:
        tk.update()
        ball.draw()
        paddle.draw()
    else:
        exit()
    time.sleep(0.01)
