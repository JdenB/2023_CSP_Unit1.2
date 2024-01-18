# |---Import Section---|
import turtle
import random as rand
import time
import turtle as trtl

#     Ideas
# 1.  Fighting game with player deflecting bullets with weapon "pong but you are a sword-fighter who has to tap to deflect"
# 2.  Bullet hell game where player must dodge bullets, and every 20 seconds gets their Action option list(MINI RPG)
# 3.  player must jump over obstacles as stage moves(chrome dinosaur game)
# 4.  player must navigate maze and CANT TOUCH SIDES or lose

# chosen = bullet hell game(mini rpg)

#  initialization
pause = 0.001
player = trtl.Turtle()
boss = trtl.Turtle()
playername = str("johndoe")
test_bullet  = trtl.Turtle()
test_bullet1  = trtl.Turtle()
test_bullet2  = trtl.Turtle()
test_bullet3 = trtl.Turtle()
playerhealth_writer = trtl.Turtle()
menu_printer = trtl.Turtle()
menu_printer1 = trtl.Turtle()
stage_drawer = turtle.Turtle()
bullet_type = []
wn = turtle.Screen()
wn.addshape("JEROM_bossB2_CC-BY-3_0.gif")
wn.bgcolor("black")
wn.bgpic('previewx2-parallax-space-backgoundv2.png')
repetitions = 1
randnum = rand.randint(1, 5)
player_health = 5
x_position = 0
y_position = 0
listlen = 0
bvar = 0
numerical_score = 0
wn.tracer(1)


# stage initialization

stage_drawer.speed(1000)
stage_drawer.hideturtle()
stage_drawer.fillcolor("white")
stage_drawer.color("white")
stage_drawer.penup()
stage_drawer.goto(-800, -300)
stage_drawer.pendown()
stage_drawer.goto(800, -300)


# player settings & initialization

player.speed(1000)
player.penup()
player.shape("circle")
player.shapesize(0.5)
player.color("white")

# menu initialization and settings
menu_printer.fillcolor("white")
menu_printer.color("white")
menu_printer.penup()
menu_printer.hideturtle()

menu_printer1.fillcolor("white")
menu_printer1.color("white")
menu_printer1.penup()
menu_printer1.hideturtle()


# writer initialization and settings

playerhealth_writer.fillcolor("white")
playerhealth_writer.color("white")
playerhealth_writer.penup()
playerhealth_writer.hideturtle()

# bullet settings & initialization
bullets = [test_bullet, test_bullet1, test_bullet2, test_bullet3]
for bullet in bullets:
    bullets[listlen].shape("triangle")
    listlen += 1
listlen = 0
for bullet1 in bullets:
    bullets[listlen].speed(10)
    listlen += 1
listlen = 0
for bullet2 in bullets:
    bullets[listlen].color("red")
    listlen += 1
listlen = 0
for bullet3 in bullets:
    bullets[listlen].penup()
    listlen += 1
listlen = 0
for bullet4 in bullets:
    bullets[listlen].shapesize(1.5)
    listlen += 1
listlen = 0
for bullet5 in bullets:
    bullets[listlen].hideturtle()
    listlen += 1
listlen = 0

# boss settings and initialization
boss.penup()
boss.speed(100)
boss.shape("JEROM_bossB2_CC-BY-3_0.gif")
boss.shapesize(5, 5)

# definitions

def playerhealth_display(switch):
    wn.listen()
    global score
    global numerical_score
    playerhealth_writer.goto((350, 300))
    if switch:
        playerhealth_writer.speed(1000)
        while switch:
            playerhealth_writer.pendown()
            time.sleep(0.001)
            playerhealth_writer.clear()
            playerhealth_writer.write(player_health, font=("Arial", 20, "normal"))

    else:
        playerhealth_writer.clear()


def checkhealth():
    if player_health <= 0:
        menu_printer.clear()
        menu_printer.write("Game Over", font=("Arial", 60, "normal"))
        menu_printer.goto(0, -100)
        menu_printer.write((str("score:"), numerical_score), font=("Arial", 60, "normal"))
        menu_printer1.goto(0, -200)
        while player_health <= 0:
            time.sleep(0.8)
            menu_printer1.clear()
            time.sleep(0.8)
            menu_printer1.write(':(', font=("Arial", 60, "normal"))


def bullet_move(id, edptx, edpty, speed):
    id.penup()
    id.hideturtle()
    id.speed(1000)
    wn.listen()
    bullet.settiltangle(rand.randint(0, 360))
    id.goto(rand.randint(-300, 300), 400)
    id.speed(speed)
    id.showturtle()
    id.goto(edptx, edpty)
    id.hideturtle()
    while id.xcor() != edptx:
        while id.ycor() != edpty:
            wn.listen()
            wn.update()


def bullet_beam(switch):
    while switch:
        wn.listen()
        wn.update()
        time.sleep(0.1)
        wn.listen()
        rand_bullet = bullets[rand.randint(0, 3)]
        for num in range(2):
            boss.goto(0, 320)
            boss.goto(0, 300)
        bullet_move(rand_bullet, player.xcor()-rand.randint(0, 0), player.ycor()-rand.randint(0, 0), 3)
        hit(15)
        print(player_health)

def hit(radius):
    global player_health
    global bvar
    global numerical_score
    numerical_score += 1
    print(numerical_score)
    bvar = 0
    for num in range(4):
        bullet1 = bullets[bvar]
        wn.listen()
        if abs(bullet1.ycor() - player.ycor()) <= radius:
            if abs(bullet1.xcor() - player.xcor()) <= radius:
                wn.listen()
                bullet1.hideturtle()
                bullet1.goto(rand.randint(-300, 300), 400)
                wn.bgcolor('red')
                wn.update()
                player_health -= 1
                time.sleep(0.1)
                wn.bgcolor('black')
                wn.update()
                checkhealth()
        bvar += 1


def fight_start():  # setup battle
    player.goto(0, 0)
    boss.goto(0, 300)



def player_right():  # move player right
    global x_position
    global player
    x_position = player.xcor()
    player.setx(x_position + 10)


def player_left():  # move player right
    global x_position
    x_position = player.xcor()
    player.setx(x_position - 10)


def player_up():  # Jump
    global y_position
    if player.ycor() == -300:
        wn.listen()
        wn.update()
        y_position = player.ycor()
        player.sety(y_position + 190)
        time.sleep(pause * 2)
        player.sety(y_position + 250)
        time.sleep(pause * 2)
        player.sety(y_position + 300)
        gravity(player, 5)


def player_crouch():  # Jump
    global y_position
    if player.ycor() >= -300:
        y_position = player.ycor()
        player.sety(-300)


def gravity(target, strength):  # pulls target object down by strength
    global y_position
    while target.ycor() > -300:
        wn.update()
        y_position = target.ycor() - strength
        target.sety(y_position)
        wn.listen()
        if target.ycor() <= -300:
            target.sety(-300)


def Display_Score():
    ...

# events

fight_start()

gravity(player, 10)
wn.onkeypress(player_up, ' ')
wn.onkeypress(player_left, 'a')
wn.onkeypress(player_right, 'd')
wn.onkeypress(player_crouch, 's')
wn.listen()

bullet_beam(True)

playerhealth_display(True)

# background settings
wn.setup(800, 600)
wn.update()


def play():
    while True:
        wn.update()

        time.sleep(pause)

