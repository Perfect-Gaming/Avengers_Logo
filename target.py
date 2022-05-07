import turtle

turtle.Screen().bgcolor("white")
t = turtle.Turtle()
t.speed(10)
t.pensize(0)
t.penup()

def outer_circle():
    t.setposition(-42.5,-150)
    t.pendown()
    t.begin_fill()
    t.color('#E80018')
    t.circle(300)
    t.end_fill()
    t.penup()
    return 

def middle_circle():
    t.setposition(-42.5,-50)
    t.pendown()
    t.begin_fill()
    t.color('white')
    t.circle(200)
    t.end_fill()
    t.penup()
    return 

def inner_circle():
    t.setposition(-42.5,50)
    t.pendown()
    t.begin_fill()
    t.color('#E80018')
    t.circle(100)
    t.end_fill()
    t.penup()
    return 

def letters():
    t.setposition(-300,-200) #T
    t.pendown()
    t.pensize(17)
    t.pencolor('#E80018')
    t.forward(60)
    t.setposition(-270, -200) #T
    t.right(90)
    t.forward(80)
    t.penup()
    t.setposition(-200, -200) #A
    t.pendown()
    t.right(20)
    t.forward(85)
    t.penup()
    t.setposition(-200, -200) #A
    t.pendown()
    t.left(40)
    t.forward(85)
    t.penup()
    t.setposition(-220, -260) #A
    t.pendown()
    t.left(70)
    t.forward(40)
    t.penup()
    t.setposition(-140, -200) #R
    t.pendown()
    t.right(90)
    t.forward(80)
    t.penup()
    t.setposition(-140, -200) #R
    t.pendown()
    t.left(90)
    t.forward(30)
    t.circle(-20,180)
    t.penup()
    t.setposition(-140, -240) #R
    t.pendown()
    t.left(180)
    t.forward(30)
    t.penup()
    t.setposition(-130, -240) #R
    t.pendown()
    t.right(45)
    t.forward(55)
    t.left(225)
    t.penup()
    t.setposition(-15, -200) #G
    t.pendown()
    t.forward(10)
    t.circle(40,270)
    t.left(90)
    t.forward(30)
    t.right(180)
    t.forward(30)
    t.right(90)
    t.forward(40)
    t.penup()
    t.setposition(45, -200) #E
    t.pendown()
    t.forward(80)
    t.penup()
    t.setposition(45, -200) #E
    t.pendown()
    t.left(90)
    t.forward(55)
    t.penup()
    t.setposition(45, -240) #E
    t.pendown()
    t.forward(45)
    t.penup()
    t.setposition(45, -280) #E
    t.pendown()
    t.forward(55)
    t.penup()
    t.setposition(125, -200) #T
    t.pendown()
    t.forward(60)
    t.setposition(155, -200) #T
    t.right(90)
    t.forward(80)
    t.penup()
    return


outer_circle()
middle_circle()
inner_circle()
letters()

t.hideturtle()
turtle.done()


#By Perfect Gaming (linktr.ee/Perfect_Gaming)
#Please like and subscribe