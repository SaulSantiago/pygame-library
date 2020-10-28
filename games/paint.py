import * from turtle
from freegames import vector

def line(start, end):
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start,end):
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    for i in range(4):
        forward(end.x-start.x)
        left(90)
    end_fill()