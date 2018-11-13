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
        self.y = -2
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
        brick = 0
        self.hit = (0,)
        for l in self.bricks: #iterate through list
            bricka = self.canvas.coords(l)
            print("boll", pos)
            print("bricka", bricka)
            if pos[3] == bricka[1] and bricka[0] <= pos[0] <= bricka[2]: #for a hit from over
                brick += 1
                self.hit = self.canvas.find_closest(bricka[0], bricka[1], halo=5)
            if pos[1] == bricka[3] and bricka[0] <= pos[0] <= bricka[2]: #for a hit from under
                brick += 2
                self.hit = self.canvas.find_closest(bricka[0], bricka[1], halo=5)
            if pos[2] == bricka[0] and bricka[1] <= pos[1] <= bricka[3]: #for a hit from right side
                brick += 3
                self.hit = self.canvas.find_closest(bricka[0], bricka[1], halo=5)
            if pos[0] == bricka[2] and bricka[1] <= pos[1] <= bricka[3]: #for a hit from left side
                brick += 4
                self.hit = self.canvas.find_closest(bricka[0], bricka[1], halo=5)
   #         if brick > 0:

        return brick


    def draw(self):

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
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
            #self.canvas.delete(brick)
        if self.hit_brick(pos) == 1:
            self.y = -1
            #self.canvas.delete(brick)
        if self.hit_brick(pos) == 2:
            self.y = 1
            #self.canvas.delete(brick)
#        if self.hit_brick(pos) > 4:

        if self.bricks.count(self.hit[0]) > 0:
            test = self.hit[0]
            self.canvas.delete(test)
            while test in self.bricks: self.bricks.remove(test)
            print(self.bricks)




class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>', self.move_up)
        self.canvas.bind_all('<KeyPress-Down>', self.move_down)
        self.canvas.bind_all('<KeyPress-space>', self.stop_paddle)

    def draw(self):
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

class Obstacle:
    def __init__(self,canvas):
        self.canvas = canvas


class Brick(Obstacle):
    def __init__(self,canvas):
        self.canvas = canvas
        super(Brick, self).__init__(canvas)


class Level:
    def level(self, canvas):
        self.canvas = canvas
        level = 1
        row = 0
        bricks = []
        try:

            for line in open(str(level) + ".txt", "r"):
                row = row + 1
                data = line.split(";")
                for i in range(12):
                    if data[i] == ".":
                        pass
                    else:
                        brick_cord = (0 + (50 * i), 20 + (row * 20), 50 + (50 * i), 40 + (row * 20), data[i])

                        bricks.append(self.canvas.create_rectangle(brick_cord[0], brick_cord[1], brick_cord[2], brick_cord[3], fill=brick_cord[4], width=2, outline="#ffffff"))

        except IOError:
            pass

        print(bricks)
        return bricks


class Game():
    def __init__(self):
        tk = Tk()
        tk.title("Bouncing Ball Game")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=600, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()
        paddle = Paddle(canvas, 'blue')
        bricks = Level.level(self, canvas)
        ball = Ball(canvas, paddle, 'green', bricks)
        while True:
            if not ball.hit_bottom:
                ball.draw()

                paddle.draw()
                tk.update_idletasks()
                tk.update()

            else:
                exit()
            time.sleep(0.01)


def main():
    Game()

if __name__ == '__main__':
    main()