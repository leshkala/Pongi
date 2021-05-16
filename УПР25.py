from tkinter import *
import random
w = 500
h = 500
tk = Tk()
canvas = Canvas(tk, width=w, height=h)
canvas.pack()
colors = ['red','orange','blue','yellow','green','white','purple']
def random_triangle():
    p1 = random.randrange(w)
    p2 = random.randrange(h)
    p3 = random.randrange(w)
    p4 = random.randrange(h)
    p5 = random.randrange(w)
    p6 = random.randrange(h)
    color = random.choice(colors)
    canvas.create_polygon(p1, p2, p3, p4, p5, p6, fill=color, outline="black")

for x in range(0, 200):
    random_triangle()