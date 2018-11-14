from tkinter import *
<<<<<<< HEAD
=======
from tkinter import ttk
from collections import defaultdict

>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916
import random
import time

#kanske skapa en default dict med level som key och lista med bricks som value

class Game:
    def __init__(self, master):
<<<<<<< HEAD
=======
        self.lvl = 0
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916
        self.master = master
        self.create_window()
        self.create_objects()
        self.welcome_text = self.create_text(300,200,"press enter to start")
        self.game_update()
        self.start()


    def create_objects(self):
        self.paddle = Paddle(self.canvas, "red")  # -||-
        self.ball = Ball(self.canvas, "blue")  # ta bort om detta inte funkar
        self.lives = Lives(self.canvas,"blue", 3)
<<<<<<< HEAD
       # self.bricks = Obstacle(self.canvas)
=======
        self.level()
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916

    def start(self):
        self.master.mainloop()

    def create_text(self, x_pos, y_pos, text,size="40"):
        font = ('Helvetica', size)
        return self.canvas.create_text(x_pos, y_pos, text=text, font=font)

    def create_window(self):  # bort för v.1
        self.width = 600
        self.height = 400
        self.master.title("Bouncing Ball Game")
        self.master.resizable(0, 0)
        self.master.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.master, width=self.width, height=self.height, bd=0, highlightthickness=0)
        self.canvas.pack()
<<<<<<< HEAD
=======
        self.lvl_text = self.canvas.create_text(550, 10, text="Level:" + str(self.lvl), fill="blue", font=('Helvetica', 15))
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916

    def update_lives(self):

        if self.ball.get_position()[3] >= self.canvas.winfo_height():
            self.lives.life -= 1
            if self.lives.life == 0:
                self.ball.y = 0
                self.create_text(300, 200, "Game Over")
        if self.lives.life == 2:
            self.canvas.itemconfig(self.lives.id, text="Lives:" + str(self.lives.life), fill="blue", font=('Helvetica',15) )
        if self.lives.life == 1:
            self.canvas.itemconfig(self.lives.id ,text="Lives:" + str(self.lives.life), fill="red", font=('Helvetica', 15))

<<<<<<< HEAD
=======
    def change_level(self):
        if len(self.bricks) == 0:
            self.canvas.delete(self.lvl_text)
            self.lvl = self.lvl + 1
            self.level()
            self.lvl_text = self.canvas.create_text(550, 10, text="Level:" + str(self.lvl), fill="blue", font=('Helvetica', 15))



>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916

    def game_update(self):

        while 1:

            if not self.lives.life == 0:
                self.paddle.move_paddle()
                if self.ball.throw_ball:
                    self.canvas.delete(self.welcome_text)
                    self.ball.move_ball()
                    self.ball.update_dir()
                    self.ball_paddle_hit()
                    self.update_lives()
<<<<<<< HEAD
=======
                    self.change_level()
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916
                self.master.update_idletasks()
                self.master.update()
                time.sleep(0.01)
            else:
                time.sleep(2)
                exit()


    def ball_paddle_hit(self):
        paddle_pos = self.canvas.coords(self.paddle.id)
        self.ball.paddle_hit(paddle_pos)

<<<<<<< HEAD
    # def brick_collision(self):
    #     self.brick_pos = self.canvas.coords(self.bricks.id)
    #     self.brick_bounce = self.ball.collision_bricks(self.brick_pos)
    #     if self.brick_bounce == 4:
    #         self.ball.x = 1
    #     if self.brick_bounce == 3:                                                denna funkar inte än
    #         self.ball.x = -1
    #     if self.brick_bounce == 1:
    #         self.ball.y = -1
    #     if self.brick_bounce == 2:
    #         self.ball.y = 1
=======
#     def brick_collision(self):
#         self.brick_pos = self.canvas.coords(bricks.id)
#        self.brick_bounce = self.ball.collision_bricks(self.brick_pos)
#         if self.brick_bounce == 4:
#             self.ball.x = 1
#         if self.brick_bounce == 3:                                                denna funkar inte än
#             self.ball.x = -1
#         if self.brick_bounce == 1:
#             self.ball.y = -1
#         if self.brick_bounce == 2:
#             self.ball.y = 1

    def level(self):
        self.bricks = []
        row = 0
        try:
            for line in open(str(self.lvl) + ".txt", "r"):
                row = row +1
                data = line.split(";")
                for i in range(12):
                    if data[i] == ".":
                        pass
                    else:
                        self.brick_cord = (0 + (50 * i), 20 + (row * 20), 50 + (50 * i), 40 + (row * 20), data[i])
                        self.bricks.append(self.canvas.create_rectangle(self.brick_cord[0], self.brick_cord[1], self.brick_cord[2], self.brick_cord[3], fill=self.brick_cord[4], width=2, outline="#ffffff"))
        except IOError:
            if self.lvl == 0:
                pass
            else:
                self.create_text(300, 200, "You made it!")
                time.sleep(10)
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916


class Lives:
    def __init__(self, canvas, color, life):
        self.canvas = canvas
        self.life = life
        self.id = self.canvas.create_text(30, 10, text="Lives:" + str(self.life), fill=color, font=('Helvetica',15))


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 100, 10,fill=color)
        self.canvas.move(self.id, 250,300)
        self.x_dir = 0
        self.y_dir = 0


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
        if paddle_pos[2] >= 600:
            self.x_dir = 0
        if paddle_pos[1] <= 0:
            self.y_dir = 0
        if paddle_pos[3] >= 400:
            self.y_dir = 0

class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        start = [-1, 1]
        random.shuffle(start)
        self.x = start[0]
        self.y = 1
        self.canvas.bind_all('<KeyPress-Return>', self.throw_ball)
        self.throw_ball = False
        self.canvas.move(self.id, 285, 265)

    def paddle_hit(self, p_pos):
        paddle_pos = p_pos
        ball_pos = self.canvas.coords(self.id)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                self.y = -5
                self.x = random.randrange(-1,1)
        return False

    def get_position(self):
        return self.canvas.coords(self.id)

    def move_ball(self):
        self.canvas.move(self.id, self.x, self.y)

    def update_dir(self):  # Ball
        #  testa sen när det funkar att ta bort self.item i metoden
        ball_pos = self.canvas.coords(self.id)

        if ball_pos[1] <= 0:
            self.y = 2
        if ball_pos[3] >= 400:
            self.y = -20
            self.x = 0
        if ball_pos[0] <= 0:
            self.x = 2
        if ball_pos[2] >= 600:
            self.x = -2


    def throw_ball(self, evt):
        self.throw_ball = True

<<<<<<< HEAD
    # def collision_bricks(self, bricks):
    #     brick_hit = 0
    #     ball_pos = self.canvas.coords(self.id)
    #     for brick in bricks:  # iterate through list
    #         if ball_pos[3] == brick[1] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from over
    #             brick_hit += 1
    #             self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
    #         if ball_pos[1] == brick[3] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from under               funkar inte än
    #             brick_hit += 2
    #             self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
    #         if ball_pos[2] == brick[0] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from right side
    #             brick_hit += 3
    #             self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
    #         if ball_pos[0] == brick[2] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from left side
    #             brick_hit += 4
    #             self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
    #     return brick_hit

# class Obstacle:
#     def __init__(self, canvas):
#         self.canvas = canvas
#         self.id = self.level(self.canvas)
#
#     def level(self, canvas):
#         self.canvas = canvas
#         self.bricks = []
#         level = 1
#         row = 0
#
#
#         try:
#
#             for line in open(str(level) + ".txt", "r"):
#                 row = row +1
#                 data = line.split(";")
#                 for i in range(12):
#                     if data[i] == ".":
#                         pass
#                     else:
#                         self.brick_cord = (0 + (50 * i), 20 + (row * 20), 50 + (50 * i), 40 + (row * 20), data[i])
#                         self.bricks.append(self.canvas.create_rectangle(self.brick_cord[0], self.brick_cord[1], self.brick_cord[2], self.brick_cord[3], fill=self.brick_cord[4], width=2, outline="#ffffff"))
#
#         except IOError:
#             pass
#
#         return self.bricks

#starts the game
root = Tk()
Game(root)
=======
    def collision_bricks(self):
        brick_hit = 0
        ball_pos = self.canvas.coords(self.id)
        for brick in self.bricks:  # iterate through list
            if ball_pos[3] == brick[1] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from over
                brick_hit += 1
                self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
            if ball_pos[1] == brick[3] and brick[0] <= ball_pos[0] <= brick[2]:  # for a hit from under               funkar inte än
                brick_hit += 2
                self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
            if ball_pos[2] == brick[0] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from right side
                brick_hit += 3
                self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
            if ball_pos[0] == brick[2] and brick[1] <= ball_pos[1] <= brick[3]:  # for a hit from left side
                brick_hit += 4
                self.hit = self.canvas.find_closest(brick[0], brick[1], halo=5)
        return brick_hit

#class Obstacle:
#    def __init__(self, canvas, lvl):
#        self.lvl = lvl
#        self.canvas = canvas
#        self.level(canvas)
#        self.id = self.level(self.canvas)



#starts the game
root = Tk()
start = Game(root)
>>>>>>> be9567ef8226fdbddbfe1f8659baf75294ba0916
