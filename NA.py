from tkinter import *
import random
import time
class Ball:
    def __init__(self, canvas, paddle, color, bricks):
        self.bricks = bricks
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        starts = [-1, 1]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -1
        self.canvas_heigt = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] < paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] < paddle_pos[3]:
                return True
        return False

    def hit_brick(self, pos):


        for l in self.bricks: #iterate through list
            if pos[3] == l[1] and l[0] <= pos[0] <= l[2]: #for a hit from over
                return 1
            if pos[1] == l[3] and l[0] <= pos[0] <= l[2]: #for a hit from under
                return 2
            if pos[2] == l[0] and l[1] <= pos[1] <= l[3]: #for a hit from right side
                return 3
            if pos[0] == l[2] and l[1] <= pos[1] <= l[3]: #for a hit from left side
                return 4

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_heigt:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -1
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

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

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


class Level:
    def level(self):
        brick1 = [50, 85, 100, 100, "red"]
        brick2 = [100, 85, 150, 100, "yellow"]
        brick3 = [150, 85, 200, 100, "red"]
        brick4 = [300, 85, 350, 100, "yellow"]
        brick5 = [200, 85, 250, 100, "red"]
        brick6 = [250, 85, 300, 100, "yellow"]
        brick7 = [50, 130, 100, 145, "red"]
        brick8 = [50, 55, 100, 70, "yellow"]
        brick9 = [50, 40, 100, 55, "red"]
        bricks = [brick1, brick2, brick3, brick4, brick5, brick6, brick7, brick8, brick9]
        return bricks

class Game(Canvas):
    def __init__(self):
        tk = Tk()
        tk.title("Bouncing Ball Game")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=800, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()

        bricks = Level.level(self)

        paddle = Paddle(canvas, 'blue')
        ball = Ball(canvas, paddle, 'green', bricks)

        while 1:
            if ball.hit_bottom == False:
                ball.draw()
                paddle.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)


def main():
    Game()

if __name__ == '__main__':
    main()

