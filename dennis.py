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



#    def hit_brick(self, pos):
#        block_pos = self.block.block_position()
#        if pos[0] >= block_pos[2] and pos[0] <= block_pos


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

    def get_position(self):
        return self.canvas.coords(self)

  #  def delete(self):
   #     self.canvas.delete(self.item)


class Block(Obstacle):
    def __init__(self, pos1,pos2,pos3,pos4, color):
        super().__init__(canvas, color)
        self.canvas = canvas
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
block1 = Block(50, 85 , 100 , 100, "blue")
block2 = Block(100,85,150,100, "white")
block3 = Block(150, 85, 200,100, "blue")
block4 = Block(200, 85, 250,100, "white")
block5 = Block(250, 85, 300,100, "blue")


while True:
    if not ball.hit_bottom:
        tk.update()
        ball.draw()
        paddle.draw()
    else:
        exit()
    time.sleep(0.01)
