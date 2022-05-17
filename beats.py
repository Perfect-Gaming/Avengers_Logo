import turtle 

turtle.Screen().bgcolor('white')
t = turtle.Turtle()
t.speed(10)
t.pensize(0)
t.penup()

def circle():
    t.setposition(0,-250)
    t.pendown()
    t.begin_fill()
    t.color('#e01f3d')
    t.circle(250)
    t.end_fill()
    t.penup()
    return

def logo():
    t.setposition(0,-100)
    t.pendown()
    t.pensize(50)
    t.color('white')
    t.circle(100)
    t.penup()
    t.setposition(-100,0)
    t.pendown()
    t.left(90)
    t.forward(250)
    return

circle()
logo()


t.hideturtle()
turtle.done()


#By Perfect Gaming (linktr.ee/Perfect_Gaming)
#Please like and subscribe