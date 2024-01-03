#  Configuration
import turtle
# imports
import turtle as trtl
import random as rand

# variables
maze_painter = trtl
maze_runner = trtl
startd = (int(25))
incrementald = (int(25))
path_width = 10
size = path_width * 2
forward = 1
angle = ()
walls = 28
distance = rand.randint(path_width * 2, incrementald)
door1 = int(1)
# setup
maze_painter.width(4)
shape=("triangle")
maze_runner.shape(shape)


# definitions
def door(distance):
    global maze_painter
    global randnum
    maze_painter.forward(distance)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()
maze_painter.hideturtle()
maze_painter.speed("fastest")
def wall(length):
    global incrementald
    global maze_painter
    global path_width
    global size
    global randnum
    # distance = 40
    if incrementald <= 65:
        return
    else:
        #   colour bits are for visually tracing wall location
       # maze_painter.pencolor("red")
        maze_painter.forward(distance)
        maze_painter.left(90)
        maze_painter.forward(size)
        maze_painter.right(180)
        maze_painter.forward(size)
        maze_painter.left(90)
        maze_painter.left(180)
        maze_painter.forward(length)
        maze_painter.left(180)
       # maze_painter.pencolor("black")
"""
def move_runner(forward):
  maze_runner.forward(forward)
def right():
    maze_runner.right(1)
def left():
    maze_runner.left(1)
def back():
    maze_runner.right(180)
    maze_runner.forward(1)
def forward():
    
    maze_runner.forward(1)
"""


def runner_forward():
    global wn
    global maze_runner
    maze_runner.tiltangle(0)
    maze_runner.forward(1)

def runner_left():
    global wn
    global maze_runner
    maze_runner.left(1)

def runner_right():
    global wn
    global maze_runner
    maze_runner.right(1)

def spiral(spiralnum):
    global maze_painter
    global startd
    global incrementald
    global path_width
    global size
    global distance
    for num in range(spiralnum):
        randnum = rand.randint(1, 40)
        randnum1 = rand.randint(1, 2)
        maze_painter.forward((int(startd + incrementald))/10)
        if randnum1 == 1:
            door(10)
            wall(distance)
        else:
            wall(distance)
            door(10)
        maze_painter.forward(((startd + incrementald) - (int(startd + incrementald)) / 10) - int(door1))
        maze_painter.left(90)
        incrementald += 10


spiral(walls)

maze_runner.penup()
maze_runner.goto(0,0)
maze_runner.showturtle()

wn = trtl
wn.onkeypress(runner_forward(), 'w')
wn.onkeypress(runner_left(), 'a')
wn.onkeypress(runner_right() ,'d')
# wn.onkeypress("s", runner_back())

wn.listen()
wn.mainloop()