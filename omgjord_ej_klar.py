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
        self.paddle = Paddle(self.canvas, "red")  # -||-
        self.ball = Ball(self.canvas, "blue")  # ta bort om detta inte funkar


    def start(self):
        self.master.mainloop()


    def create_window(self):  # bort för v.1
        self.width = 610
        self.height = 400
        self.master.title("Bouncing Ball Game")
        self.master.resizable(0, 0)
        self.master.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.master, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.pack()



    def update_(self):

        while 1:
            if not self.ball.hit_bottom:
                self.ball.move_ball()
                self.paddle.move_paddle()
                self.ball_paddle_hit()
                #if self.ball.throw_ball == True:
                self.master.update_idletasks()
                self.master.update()
                time.sleep(0.1)
            else:
                exit()

    def ball_paddle_hit(self):
        paddle_pos = self.canvas.coords(self.paddle.id)
        self.ball.paddle_hit(paddle_pos)


#   def get_position(self, item):
 #       return self.canvas.coords(item)

#    def move_(self, x, y):
#        self.canvas.move(self, x, y)

 #   def delete(self):
 #       self.canvas.delete(self)





class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 100, 10,fill=color)
        self.canvas.move(self.id, 200,300)
        self.x_dir = 0
        self.y_dir = 0
        self.paddle_pos = self.canvas.coords(self.id)

        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)



    def move_left(self, evt):
        self.x_dir = -3

    def move_right(self, evt):
        self.x_dir = 3

    def move_up(self, evt):
        self.y_dir = -3

    def move_down(self, evt):
        self.y_dir = 3

    def stop_paddle(self, evt):
        self.y_dir = 0
        self.x_dir = 0

    def move_paddle(self):
        self.canvas.move(self.id, self.x_dir, self.y_dir)
        paddle_pos = self.canvas.coords(self.id)
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

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        start = [-1, 1]
        random.shuffle(start)
        self.x = start[0]
        self.y = 1
        self.hit_bottom = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)
        self.throw_ball = False

    def paddle_hit(self, p_pos):
        paddle_pos = p_pos
        ball_pos = self.canvas.coords(self.id)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                self.y = -3
                self.x = random.randrange(-1,1)
        return False

    def move_ball(self):  # Ball
        #  testa sen när det funkar att ta bort self.item i metoden
        self.canvas.move(self.id, self.x, self.y)
        ball_pos = self.canvas.coords(self.id)

        if ball_pos[1] <= 0:
            self.y = 1
        if ball_pos[3] >= 400:
            self.hit_bottom = True
        if ball_pos[0] <= 0:
            self.x = 1
        if ball_pos[2] >= 610:
            self.x = -1

    def start_game(self, evt):
        self.throw_ball = True

    def collision_bricks(self, bricks):
        number_collision = 0
        ball_pos = self.canvas.coords(self.id)
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
#här låg tidigare collision




class Obstacle:
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


