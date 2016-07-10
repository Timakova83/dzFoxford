from turtle import Turtle

def init_drowmen():
    global t,x_current, y_current
    t=Turtle()
    t.penup()
    x_current=0
    y_current=0
    t.goto(x_current, y_current)

def test_drawman():
    pen_down()
    for i in range(5):
        on_vector(1, 2)
        on_vector(0, -2)
    pen_up()
    to_point(0,0)


def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(x,y):
    global x_current, y_current
    x_current+=dx
    y_current+=dy
    t.goto(x_current,y_current)

def to_point(x,y):
    global x_current, y_current
    x_current=x
    y_current=y
    t.goto(x_current,y_current)

init_drowmen()
if _name_ == '_main_':
    import time
    test_drawmen()
    time.sleep(100)