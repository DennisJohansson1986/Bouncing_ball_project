import tkinter as tk
import random
import time

class GameObject:
    def __init__(self,canvas, size):
        self.size = size
        self.canvas = canvas

class Move:
    def draw(self): #Ball
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        points = 0
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_heigt:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            self.y = -1
            self.x = random.randrange(-1,1) #skickar iväg bollen åt random håll vid paddelträff
        if pos[0] <= 0:
            self.x = 1
        if pos[2] >= self.canvas_width:
            self.x = -1
        if self.hit_brick(pos) == 4:
            self.x = 1
        if self.hit_brick(pos) == 3:
            self.x = -1
        if self.hit_brick(pos) == 1:
            self.y = -1
        if self.hit_brick(pos) == 2:
            self.y = 1

    def draw(self): #Paddle
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_left(self, evt):
        self.x = -3
    def turn_right(self, evt):
        self.x = 3
    def move_up(self, evt):
        self.y = -3
    def move_down(self, evt):
        self.y = 3
    def stop_paddle(self, evt):
        self.y = 0
        self.x = 0

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)

class Collide:
    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] < paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] < paddle_pos[3]:
                return True
        return False
    def hit_brick(self, pos):
        brick = 0
        for l in self.bricks: #iterate through list
            if pos[3] == l[1] and l[0] <= pos[0] <= l[2]: #for a hit from over
                brick += 1
            if pos[1] == l[3] and l[0] <= pos[0] <= l[2]: #for a hit from under
                brick += 2
            if pos[2] == l[0] and l[1] <= pos[1] <= l[3]: #for a hit from right side
                brick += 3
            if pos[0] == l[2] and l[1] <= pos[1] <= l[3]: #for a hit from left side
                brick += 4

        return brick


class Ball(GameObject):
    def __init__(self, canvas, color,size):
        super(Ball,self).__init__(canvas,size)
        self.size = size
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        starts = [-1, 1]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -2
        self.canvas_heigt = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False



class Paddle(GameObject):
    def __init__(self, canvas, color,size):
        super().__init__(canvas,size)
        self.size = size
        self.Canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.Canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width(self)

class Obstacle(GameObject):
    def __init__(self,canvas,size):
        super(Obstacle,self).__init__(canvas,size)
        self.canvas = canvas
        self.size = size

class Brick(Obstacle):
    def __init__(self,canvas,size):
        super().__init__(canvas,size)
        self.canvas = canvas
        self.size = size

class Level:
    def level(self, canvas):
        brick1 = [50, 85, 100, 100,"red"]
        brick2 = [100, 85, 150, 100,"blue"]
        brick3 = [150, 85, 200, 100,"white"]
        brick4 = [300, 85, 350, 100,"white"]
        brick5 = [200, 85, 250, 100,"white"]
        brick6 = [250, 85, 300, 100,"white"]
        brick7 = [50, 130, 100, 145,"white"]
        brick8 = [50, 55, 100, 70,"white"]
        brick9 = [50, 40, 100, 55,"white"]
        self.bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9]

        for l in self.bricks:
            pos1 = l[0]
            pos2 = l[1]
            pos3 = l[2]
            pos4 = l[3]
            color = l[4]
            canvas.create_rectangle(pos1, pos2, pos3, pos4, fill=color)

        return self.bricks

class GameStart(tk.Canvas):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        canvas = tk.Canvas(root)
        canvas.grid()
        root.title("Bouncing Ball Game")
        root.resizable(0, 0)
        root.wm_attributes("-topmost", 1)
        root.mainloop()


game = GameStart()

# while True:
#     if not ball.hit_bottom:
#         ball.draw()
#         paddle.draw()
#         update_idletasks()
#         update()
#     else:
#         exit()
#     time.sleep(0.01)
