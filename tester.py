import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)
canvas.grid()
item = canvas.create_rectangle(50,25,150,75, fill="blue")
def change_color():
    canvas.itemconfig(item,fill='red')
def delete():
    canvas.delete(item)
def add_box():
    item = canvas.create_rectangle(50, 25, 150, 75, fill="blue")
button_red = tk.Button(root,text='Push for red', width=30,command=change_color)
button_delete = tk.Button(root,text='push to delete button', width=30,command=delete)
button_add = tk.Button(root,text='push to add box', width=30,command=add_box)
button_add.grid(row=1,column=0)
button_delete.grid(row=2,column=0)
button_red.grid(row=3,column=0)
#root.update()
root.mainloop()
