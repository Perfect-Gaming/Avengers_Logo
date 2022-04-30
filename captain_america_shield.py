import turtle

turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(10)
t.pensize(1)

def outer_circle():
    t.setposition(0,-280)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.circle(300)
    t.end_fill()
    t.penup()
    return 

def midlle_circle():
    t.setposition(0,-210)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.circle(230)
    t.end_fill()
    t.penup()
    return

def inner_circle():
    t.setposition(0,-140)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.circle(160)
    t.end_fill()
    t.penup()
    return

def core():
    t.setposition(0,-70)
    t.pendown()
    t.begin_fill()
    t.color('blue')
    t.circle(90)
    t.end_fill()
    t.penup()
    return

def star():
    t.setposition(21,48.25)
    angle = int(144)
    side= int(65)
    pointies = 5
    ROTATION = 360/pointies
    angle_left=angle
    angle_right=angle
    t.color('white')
    t.begin_fill()
    for p in range(pointies):
        t.forward(side)
        t.right(angle_right)
        t.forward(side)
        t.left(angle_left)
        t.right(ROTATION)
    t.end_fill()
    return

outer_circle()
midlle_circle()
inner_circle()
core()
star()

t.hideturtle()
turtle.done()


#By Perfect Gaming (linktr.ee/Perfect_Gaming)
#Please like and subscribe