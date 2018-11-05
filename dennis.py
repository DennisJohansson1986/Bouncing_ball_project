from tkinter import *
import random
import time


class Ball:
    def __init__(self, canvas, color, paddle, block):
        self.canvas = canvas
        self.paddle = paddle
        self.block = block
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.ball_next = self.canvas.create_oval(10, 10, 25, 25, state="hidden")
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
        if self.hit_block_over(pos):
            self.y = -2
        if self.hit_block_under(pos):
            self.y = 2
        # if self.hit_block_test(pos):
        #     self.x = -2


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def hit_block_over(self, pos):
        block_pos = [[300, 85, 350, 100],[150, 85, 200,100],[100,85,150,100],[50, 85 , 100 , 100], [200, 85, 250,100], [250, 85, 300,100],[400,100,450,115]]

        for l in block_pos:
            if pos[2] >= l[0] and pos[0] <= l[2]:
                if pos[3] >= l[1] and pos[3] <= l[3]:
                    return True
                return False


    def hit_block_under(self, pos):
        block_pos = [[300, 85, 350, 100],[100,85,150,100],[150, 85, 200,100],[50, 85 , 100 , 100], [200, 85, 250,100], [250, 85, 300,100],[400,100,450,115]]
        #i = 0
        #while i < len(block_pos):

        for l in block_pos:
            if pos[1] == l[3] and l[0] <= pos[0] <= l[2]:
                return True
          #  i += 1

    def hit_block(self):
        pass
            # if pos[0] >= l[0] and pos[2] <= l[2]:
            #     if pos[1] <= l[3]:
            #         return True
            # return False

    # def hit_block_test(self, pos):
    #     block_pos = [50, 85 , 100 , 100]
    #     if pos[2] <= block_pos[0] and pos[0] >= block_pos[2]:
    #         if pos[3] <= block_pos[1] and pos[3] >= block_pos[3]:
    #             return True
    #         return False

    # def collison_counter(self, el1, el2):
    #     collisioncounter = 0
    #     object_coords = self.canvas.coords(el1)
    #     obstacle_coords = self.canvas.coords(el2)
    #
    #     if object_coords[2] < obstacle_coords[0] + 5:
    #         collisioncounter = 1
    #     if object_coords[3] < obstacle_coords[1] + 5:
    #         collisioncounter = 2
    #     if object_coords[0] > obstacle_coords[2] - 5:
    #         collisioncounter = 3
    #     if object_coords[1] > obstacle_coords[3] - 5:
    #         collisioncounter = 4
    #
    #     return collisioncounter



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
       # self.item = item


class Block(Obstacle):
    def __init__(self, pos1,pos2,pos3,pos4, color):
        super().__init__(canvas, color)
        self.canvas = canvas
        self.color = color
        self.id = canvas.create_rectangle(pos1,pos2,pos3,pos4, fill=color)

 #   def add_block(self):


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
block6 = Block(300, 85, 350, 100, "black")
block4 = Block(200, 85, 250,100, "white")
block5 = Block(250, 85, 300,100, "blue")
block_test = Block(400,100,450,115, "orange")

while True:
    if not ball.hit_bottom:
        tk.update()
        ball.draw()
        paddle.draw()
    else:
        exit()
    time.sleep(0.01)
