from tkinter import *
from tkinter import ttk

import random
import time

#kanske skapa en default dict med level som key och lista med bricks som value

class Game:
    def __init__(self, master):
        self.master = master
        self.create_window()
        self.create_objects()
        self.update_()
        self.start()

    def create_objects(self):
        self.paddle = Paddle(self.canvas,self.width / 2, 346, "red")  # -||-
        self.ball = Ball(self.canvas, "blue")  # ta bort om detta inte funkar

    def start(self):
        self.master.mainloop()

    def update_(self):
        while 1:
            if not self.ball.hit_bottom:
                self.ball.move_ball()
  #              self.paddle.draw_paddle()           #nåt som är fel i metoden draw_paddle
                self.master.update_idletasks()
                self.master.update()
            else:
                exit()




    def create_window(self):  # bort för v.1
        self.width = 610
        self.height = 400
        self.master.title("Bouncing Ball Game")
        self.master.resizable(0, 0)
        self.master.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.master, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.pack()


class GameObject:
    def __init__(self, canvas, id):
        self.canvas = canvas
        self.id = id

    def get_position(self):
        return self.canvas.coords(self.id)

    def move_(self, x, y):
        self.canvas.move(self.id, x, y)

    def delete(self):
        self.canvas.delete(self.id)


class Ball(GameObject):
    def __init__(self, canvas, color):
        self.id = id
        super().__init__(canvas, self.id)
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        starts = [-1, 1]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.speed = 10
        self.hit_bottom = False
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def move_ball(self):  # Ball

        ball_pos = self.get_position()  # testa sen när det funkar att ta bort self.item i metoden

        if ball_pos[1] <= 0:
            self.y = 1
        if ball_pos[3] >= 400:
            self.hit_bottom = True
        if self.hit_paddle() == True:
            self.y = -1
            self.x = random.randrange(-1, 1)  # skickar iväg bollen åt random håll vid paddelträff
        if ball_pos[0] <= 0:
            self.x = 1
        if ball_pos[2] <= self.canvas_width:
            self.x = -1
        self.canvas.move(self.id, self.x, self.y)

    def hit_paddle(self):
        ball_pos = self.get_position()
        paddle = Paddle
        paddle = self.get_position()

        if ball_pos[2] >= paddle[0] and ball_pos[0] < paddle[2]:
            if ball_pos[3] >= paddle[1] and ball_pos[3] < paddle[3]:
                return True
        return False

    def collision(self, bricks):
        number_collision = 0
        ball_pos = self.get_position()
        for brick in bricks:  # iterate through list
            if ball_pos[3] == brick[1] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from over
                self.y = -1
            if ball_pos[1] == brick[3] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from under
                self.y = 1
            if ball_pos[2] == brick[0] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from right side
                self.x = -1
            if ball_pos[0] == brick[2] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from left side
                self.x = 1

        return number_collision


class Paddle(GameObject):
    def __init__(self, canvas,x,y, color):
        self.id = id
        self.canvas = canvas
        self.width = 80
        self.height = 10
        self.id = self.canvas.create_rectangle(x - self.width / 2,y - self.height / 2,x + self.width / 2,y + self.height / 2 ,fill=color)
        self.x_dir = 0
        self.y_dir = 0

        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)
        super().__init__(canvas, id)


    def turn_left(self, evt):
        self.x_dir = -3

    def turn_right(self, evt):
        self.x_dir = 3

    def move_up(self, evt):
        self.y_dir = -3

    def move_down(self, evt):
        self.y_dir = 3

    def stop_paddle(self, evt):
        self.y_dir = 0
        self.x_dir = 0

    def draw_paddle(self):
        self.canvas.move(self.id, self.x_dir, self.y_dir)
        paddle_pos = self.get_position()
        if paddle_pos[0] <= 0:
            self.x_dir = 0
        if paddle_pos[2] >= 610:
            self.x_dir = 0
        if paddle_pos[1] <= 0:
            self.y_dir = 0
        if paddle_pos[3] >= 400:
            self.y_dir = 0

 #   def set_ball(self, ball):
 #       self.ball = ball

class Obstacle(GameObject):
    def __init__(self, canvas, bricks):
        self.id = id
        super().__init__(canvas, id)
        self.canvas = canvas
        self.bricks = bricks
        item = self.bricks


    def create_level(self):
        level = 1
        row = 0
        self.bricks = []
        try:

            for line in open(str(level) + ".txt", "r"):
                row = row + 1
                data = line.split(";")
                for i in range(12):
                    if data[i] == ".":
                        pass
                    else:
                        brick = (0 + (50 * i), 20 + (row * 20), 50 + (50 * i), 40 + (row * 20), data[i])
                        self.bricks.append(brick)

        except IOError:
            pass

        for l in self.bricks:
            pos1 = l[0]
            pos2 = l[1]
            pos3 = l[2]
            pos4 = l[3]
            color = l[4]
            self.canvas.create_rectangle(pos1, pos2, pos3, pos4, fill=color)

        return self.bricks

#starts the game
root = Tk()
start = Game(root)


