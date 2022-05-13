import turtle

turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.speed(10)
t.pensize(0)
t.penup()


def circle():
    t.setposition(0,-250)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.circle(250)
    t.end_fill()
    t.penup()
    return 

def ring():
    t.setposition(0,-150)
    t.pendown()
    t.pensize(8)
    t.pencolor('white')
    t.circle(150)
    t.penup()
    return 

def triangle():
    t.setposition(85,0)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.right(150)
    t.forward(160)
    t.right(120)
    t.forward(160)
    t.right(120)
    t.forward(160)
    t.end_fill()
    t.penup()
    return 

circle()
ring()
triangle()

t.hideturtle()
turtle.done()


#By Perfect Gaming (linktr.ee/Perfect_Gaming)
#Please like and subscribe