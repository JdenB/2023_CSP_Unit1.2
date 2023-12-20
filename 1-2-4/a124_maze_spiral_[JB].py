#  Configuration

# imports
import turtle as trtl
import random as rand

# variables
maze_painter = trtl
startd = (int(25))
incrementald = (int(25))
path_width = 10
size = path_width * 2
# setup
maze_painter.width(4)

# definitions
def door(distance, size):
    global maze_painter
    maze_painter.forward(distance)
    maze_painter.penup()
    maze_painter.forward(path_width * 2)
    maze_painter.pendown()
maze_painter.hideturtle()
maze_painter.speed(10000000)
def wall():
    global maze_painter
    global path_width
    global size
    distance = rand.randint(path_width * 2, incrementald)
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
        maze_painter.forward(distance)
        maze_painter.left(180)
        # maze_painter.pencolor("black")


def spiral(spiralnum):
    global maze_painter
    global startd
    global incrementald
    global path_width
    global size
    for num in range(spiralnum):
        maze_painter.forward((int(startd + incrementald))/10)
        door(10, 10)
        wall()
        maze_painter.forward((int(startd + incrementald)) - (int(startd + incrementald)) / 10)
        maze_painter.left(90)
        incrementald += 10

spiral(28)

input(maze_painter.onkeypress("enter"))