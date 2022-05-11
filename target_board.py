import turtle 

turtle.Screen().bgcolor("white")
t = turtle.Turtle()
t.speed(10)
t.pensize(0)
t.penup()

def outer_circle():
    t.setposition(0,-300)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.pencolor('black')
    t.circle(300)
    t.end_fill()
    t.penup()
    return 

def black_layer():
    t.setposition(0,-240)
    t.pendown()
    t.begin_fill()
    t.color('black')
    t.circle(240)
    t.end_fill()
    t.penup()
    return 

def blue_layer():
    t.setposition(0,-180)
    t.pendown()
    t.begin_fill()
    t.color('#0004ff')
    t.circle(180)
    t.end_fill()
    t.penup()
    return 

def red_layer():
    t.setposition(0,-120)
    t.pendown()
    t.begin_fill()
    t.color('red')
    t.circle(120)
    t.end_fill()
    t.penup()
    return 

def inner_circle():
    t.setposition(0,-60)
    t.pendown()
    t.begin_fill()
    t.color('yellow')
    t.circle(60)
    t.end_fill()
    t.penup()
    return 

outer_circle()
black_layer()
blue_layer()
red_layer()
inner_circle()


t.hideturtle()
turtle.done()


#By Perfect Gaming (linktr.ee/Perfect_Gaming)
#Please like and subscribe