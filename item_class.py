import tkinter as tk
import time


class Item:
    def __init__(self, pos, color):
        tk = Tk()
        tk.title("Bouncing Ball Game")
        tk.resizable(0, 0)
        tk.wm_attributes("-topmost", 1)
        canvas = Canvas(tk, width=800, height=400, bd=0, highlightthickness=0)
        canvas.pack()
        tk.update()

        paddle = Paddle(canvas, 'blue')
        ball = Ball(canvas, paddle, 'green')

# class Paddle:
#     def __init__(self, canvas, color):
#         self.canvas = canvas
#         self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
#         self.canvas.move(self.id, 200, 300)
#         self.xspeed = 0
#         self.yspeed = 0
#         self.canvas.bind_all('<KeyPress-Left>', self.move_left)
#         self.canvas.bind_all('<KeyPress-Right>', self.move_right)
#         self.canvas.bind_all('<KeyPress-Up>', self.move_up)
#         self.canvas.bind_all('<KeyPress-Down>', self.move_down)
#
#     def draw(self):
#         self.canvas.move(self.id, self.xspeed, self.yspeed)
#         pos = self.canvas.coords(self.id)
#         if pos[0] <= 0:
#             self.xspeed = 0
#         if pos[2] >= 500:
#             self.xspeed = 0
#         if pos[1] <= 0:
#             self.yspeed = 0
#         if pos[3] >= 200:
#             self.yspeed = 0
#
#     def move_left(self, evt):
#         self.xspeed = -4
#     def move_right(self, evt):
#         self.xspeed = 4
#     def move_up(self, evt):
#         self.yspeed = -4
#     def move_down(self, evt):
#         self.yspeed = 4


class Brick(Item):
    pass

class Block(Item):
    pass

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=400, background="yellow")
canvas.pack()
root.mainloop()
time.sleep(0.01)

# if __name__=='__main__':
#     main()
