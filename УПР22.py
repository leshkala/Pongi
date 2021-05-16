import turtle
t = turtle.Pen()
def s(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0,8):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
t.color(0.3, 0.75, 0)
s(50, True)
t.color(0, 0, 0)
s(50, False)